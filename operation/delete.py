import sys
import os
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "pages"))


def func1(*args, **kwargs):
    poco = AndroidUiautomationPoco()
    return poco(**kwargs)


dict_ = {
    "text": func1
}

def get_obj(page, title):
    #从DB里面取到对应page和title的类型和value
    _type = "text"
    value = "设备管理"
    _temp = {}

    if _type != "image":
        _temp[_type] = value

    res = dict_[_type](**_temp)


if __name__ =="__main__":

    p_ = __import__("HelloPage")
    page_ = getattr(p_, "Hello")()
    print(page_.deviceManager)
    from models.iot_gate_way import UserDevice
