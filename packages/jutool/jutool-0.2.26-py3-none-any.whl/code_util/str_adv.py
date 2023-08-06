import hashlib
import time

from code_util.structures import func_check
from collections import Iterable


@func_check
def hash_str(target_str: str) -> str:
    """
    使用MD5对str进行hash编码
    :param target_str: 需要编码的str
    :return: 无返回
    """
    return hashlib.md5(target_str.encode("utf8")).hexdigest()


def hash_obj_strbase(obj) -> str:
    """
    对对象进行迭代编码
    :param obj: 需要进行编码的对象
    :return: hash值
    """
    if isinstance(obj, str) or isinstance(obj, int) or isinstance(obj, float):
        return hash_str(str(obj))

    if isinstance(obj, dict):
        items_hashed_list = [hash_obj_strbase(list(obj.keys())), hash_obj_strbase(list(obj.values()))]
        return hash_str("".join(items_hashed_list))
    elif isinstance(obj, Iterable) or isinstance(obj, list) or isinstance(obj, tuple):
        items_hashed_list = [hash_obj_strbase(x) for x in obj]
        return hash_str("".join(items_hashed_list))
    else:
        return hash_str(str(obj.__class__))

