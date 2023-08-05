#!/usr/bin/env python

import functools
import importlib
import pickle
import signal
from functools import partial
from multiprocessing.connection import Listener
from multiprocessing import current_process
from pprint import pprint

import numpy as np

current_process()._inheriting = False

BASIC_TYPES = (int, float, str, bool, bytes, type(None))

REMOTE_OBJECT_PROXY = 1
ND_ARRAY = 2
LOCAL_OBJECT_PROXY = 3
PICKLE = 4


class ClientObjectMapper:
    def __init__(self, pipe_2):
        self.map_ = {}
        self.pipe_2 = pipe_2

    def register(self, data):
        id_ = (0, id(data))
        if id_ not in self.map_:
            self.map_[id_] = data
        return id_

    def unregister(self, id_):
        del self.map_[id_]

    def get_registered(self, id_):
        try:
            return self.map_[id_]
        except KeyError:
            pprint({hex(id_): value for id_, value in self.map_.items()})
            raise

    def unwrap(self, data):
        try:
            type_, item = data
        except Exception:
            traceback.print_stack()
            raise
        if type_ == 0:
            if isinstance(item, BASIC_TYPES):
                return item
            if isinstance(item, list):
                return [self.unwrap(ii) for ii in item]
            if isinstance(item, tuple):
                return tuple(self.unwrap(ii) for ii in item)
            if isinstance(item, set):
                return set(self.unwrap(ii) for ii in item)
            if isinstance(item, dict):
                return {
                    self.unwrap(key): self.unwrap(value) for key, value in item.items()
                }
        if type_ is PICKLE:
            return pickle.loads(item)
        if type_ is REMOTE_OBJECT_PROXY:
            return self.get_registered(item)
        if type_ == LOCAL_OBJECT_PROXY:
            return ObjectProxy(self, self.pipe_2, item)
        if type_ is ND_ARRAY:
            bytes_, shape, dtype = item
            return np.ndarray(shape, dtype, bytes_)

        return item
        raise NotImplementedError(f"don't know how to unwrap {type(item)} {repr(item)}")

    def wrap(self, data):
        if isinstance(data, BASIC_TYPES):
            return 0, data
        if isinstance(data, slice):
            return 0, data
        if isinstance(data, list):
            return 0, [self.wrap(ii) for ii in data]
        if isinstance(data, tuple):
            return 0, tuple(self.wrap(ii) for ii in data)
        if isinstance(data, set):
            return 0, set(self.wrap(ii) for ii in data)
        if isinstance(data, dict):
            return 0, {self.wrap(key): self.wrap(value) for key, value in data.items()}

        if isinstance(data, np.ndarray):
            return ND_ARRAY, (data.tobytes(), data.shape, data.dtype.name)

        return REMOTE_OBJECT_PROXY, self.register(data)


def handle_result(function):
    @functools.wraps(function)
    def wrapped(*a, **kw):
        function(*a, **kw)
        error, res = self._recv()
        if error:
            raise res
        else:
            return res
    return wrapped

class ObjectProxy:
    def __init__(self, mapper, pipe, id_):
        self._mapper = mapper
        self._pipe = pipe
        self._id = id_

    def _submit(self, cmd, *args):
        self._send(cmd, *args)
        error, res = self._recv()
        if error:
            raise res
        else:
            return res

    def __getattr__(self, name):
        return self._submit("GETATTR", self._id, name)

    def __call__(self, *args, **kw_args):
        return self._submit("CALL", self._id, args, kw_args)

    def __getitem__(self, arg):
        return self._submit("GETITEM", self._id, arg)

    def __len__(self):
        return self._submit("LEN", self._id)

    def _send(self, cmd, *args):
        payload = self._mapper.wrap(args)
        self._pipe.send((cmd, payload))

    def _recv(self):
        return self._mapper.unwrap(self._pipe.recv())


optimizations = {}


def main(pipe, pipe_2):

    current_process()._identity = ()

    signal.signal(signal.SIGINT, signal.SIG_IGN)

    mapper = ClientObjectMapper(pipe_2)

    commands = {
        "SETITEM": setitem_command,
        "GETITEM": getitem_command,
        "GETATTR": getattr_command,
        "CALL": call_command,
        "ITER": iter_command,
        "NEXT": next_command,
        "DIR": dir_command,
        "INIT_OPTIMIZATIONS": init_optimizations_command,
    }

    KILLPILL = "KILLPILL"

    while True:
        try:
            command, args = pipe.recv()
        except EOFError:
            break
        if command == KILLPILL:
            break
        if command == "IMPORT":
            try:
                module = importlib.import_module(args)
                id_ = mapper.register(module)
            except ImportError:
                id_ = None
            pipe.send(id_)
            continue
        args = mapper.unwrap(args)
        if command == "DELETE":
            mapper.unregister(args)
            continue

        response = commands[command](*args)
        if response is not None:
            error, result = response
            pipe.send((error, mapper.wrap(result)))


def init_optimizations_command(path):
    global optimizations
    error = None
    try:
        module = {}
        exec(open(path).read(), module)
        optimizations.update(module["optimizations"])
    except Exception as e:
        error = e

    return error, None


def call_command(obj, args, kwargs):
    error = None
    result = None
    try:
        r = obj(*args, **kwargs)
        # handle pyopnms style "call by ref":
        result = (r, args)
    except Exception as e:
        error = e

    return error, result


def getattr_command(obj, name):
    key = f"{obj.__class__.__name__}.{name}"
    if key in optimizations:
        result = optimizations[key]
        if not key.startswith("module."):
            result = partial(result, obj)

        return None, result

    error = None
    result = None
    try:
        result = getattr(obj, name)
    except Exception as e:
        error = e

    return error, result


def dir_command(obj):
    error = None
    result = None
    try:
        result = dir(obj)
    except Exception as e:
        error = e

    return error, result


def setitem_command(obj, key, value):
    return _call(obj, "__setitem__", key, value)


def getitem_command(obj, key):
    return _call(obj, "__getitem__", key)


def iter_command(obj):
    return _call(obj, "__iter__")


def next_command(obj):
    return _call(obj, "__next__")


def _call(obj, method, *args, **kwargs):
    error = None
    result = None
    try:
        result = getattr(obj, method)(*args, **kwargs)
    except Exception as e:
        error = e.__class__(
            f"calling {obj}.{method} with args {args} {kwargs} failed: {e}"
        )

    return error, result
