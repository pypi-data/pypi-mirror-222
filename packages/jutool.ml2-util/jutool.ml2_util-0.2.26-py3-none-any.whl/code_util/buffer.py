from functools import wraps
import os, pickle, atexit
from code_util.env import get_config_obj
from code_util.str_adv import hash_obj_strbase, hash_str
from code_util.log import log_error

_buffer_items = {}
_buffer_oper_queue = []


@atexit.register
def _flush_all_oper_queue():
    queue_set = set(_buffer_oper_queue)
    for item in queue_set:
        _save_buffer_file(item)
    print("atexit oper finished")


def _get_hash_key_(fun_name, *args, **kwargs):
    key_buffer_ = [hash_str(fun_name)]
    if len(args) > 0:
        key_buffer_.append([hash_obj_strbase(arg) for arg in args])
    if len(kwargs) > 0:
        key_buffer_.append([hash_obj_strbase(kwarg) for kwarg in kwargs])
    return fun_name + "_" + hash_obj_strbase(key_buffer_)


def _load_buffer_file(key):
    buffer_folder=get_config_obj().get_config("buffer_folder")
    path = os.path.join(os.getcwd(), buffer_folder, key)
    with open(path, 'rb') as f:
        saved_item = pickle.load(f)
    _buffer_items[key] = saved_item


def _save_buffer_file(key):
    buffer_folder = get_config_obj().get_config("buffer_folder")
    path = os.path.join(os.getcwd(), buffer_folder, key)
    folder = os.path.join(os.getcwd(), buffer_folder)
    if not os.path.exists(folder):
        os.mkdir(folder)
    with open(path, 'wb') as f:
        pickle.dump(_buffer_items[key], f)


def _delete_buffer_file(key):
    buffer_folder = get_config_obj().get_config("buffer_folder")
    path = os.path.join(os.getcwd(), buffer_folder, key)
    if os.path.exists(path):
        os.remove(path)


def _has_buffer_file(key):
    buffer_folder = get_config_obj().get_config("buffer_folder")
    path = os.path.join(os.getcwd(), buffer_folder, key)
    return os.path.exists(path)


def buffer_item(key: str, value):
    """
    缓存一个对象
    :param key: 对象的key
    :param value: 对象的value
    :return: 无返回
    """
    nkey = _get_hash_key_(key)
    _buffer_items[nkey] = value
    # _save_buffer_file(nkey)
    _buffer_oper_queue.append(nkey)


def get_buffer_item(key: str):
    """
    获得一个对象的缓存
    :param key: 对象的key
    :return: 对象，查找不到会抛出异常
    """
    nkey = _get_hash_key_(key)

    if nkey in _buffer_items:
        return _buffer_items[nkey]

    if _has_buffer_file(nkey):
        _load_buffer_file(nkey)
        return _buffer_items[nkey]

    log_error("没有此buffer item")


def has_item_key(key: str):
    """
    是否存在某个key的缓存对象
    :param key: 缓存的key
    :return: True标识存在
    """
    nkey = _get_hash_key_(key)

    if nkey in _buffer_items:
        return True

    if _has_buffer_file(nkey):
        return True

    return False


def remove_item(key: str):
    """
    删除某个缓存对象
    :param key: 需要删除对象的key
    :return: 无返回
    """
    nkey = _get_hash_key_(key)

    if nkey in _buffer_items:
        del _buffer_items[nkey]
    if _has_buffer_file(nkey):
        _delete_buffer_file(nkey)


def buffer(version=1.0):
    '''
    缓存方法的标识符
    :param permanent: 是否永久化存储
    :return: 无
    '''

    def dector(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            global _buffer_items
            nkey = _get_hash_key_(func.__name__, args, kwargs)
            if has_item_key(nkey):
                buffer_value = get_buffer_item(nkey)
                if buffer_value['version'] == version:
                    return buffer_value['value']

            func_result = func(*args, **kwargs)
            buffer_item(nkey, {'version': version, 'value': func_result})

            return func_result

        return wrapper

    return dector
