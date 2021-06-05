import inspect
from airtest.core.android.recorder import *
from airtest.core.android.adb import *
from conf.default import BASE_PROJECT
import logging
logging.basicConfig(level=logging.NOTSET)


def get_record_out_dir(class_name, func_name, task_id=None):
    file_name = f"{class_name}_{func_name}_{task_id}.mp4"
    return file_name



def get_attr(func):
    def wrapper(*args, **kwargs):
        func.__name__, func.__doc__
        #发个HTTP请求包含函数名，注释
        func(*args, **kwargs)
    return wrapper


def record(poco, task_id=None):
    def outer(func):
        class_name = inspect.stack()[1][3]
        _idr = os.path.join(BASE_PROJECT, "report")
        filename = get_record_out_dir(class_name, func.__name__, task_id=task_id)
        outfile = os.path.join(_idr, filename)


        def inner(*args, **kwargs):
            _device = poco.device.get_default_device()
            adb = ADB(serialno=_device)
            recorder = Recorder(adb)
            recorder.start_recording()
            try:
                func(*args, **kwargs)
            finally:
                recorder.stop_recording(output=outfile)
        return inner
    return outer