import threading
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.iot_gate_way import Device
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


def init_poco():
    return AndroidUiautomationPoco()


class PocoSession:
    __instance = None
    __instance_lock = threading.Lock()

    @classmethod
    def get_poco(cls):
        """获取poco"""
        with PocoSession.__instance_lock:
            if not PocoSession.__instance:
                PocoSession.__instance = init_poco()
        return PocoSession.__instance


class DatebaseSession:

    @classmethod
    def __new__(cls, database, *args, **kwargs):
        db_engine = create_engine(
            f"mysql+pymysql://{database}:{database}@testdbmb4-m1.db.pajkdc.com:3306/{database}?charset=utf8",
            max_overflow=5
        )
        _session = sessionmaker(bind=db_engine)
        cls._session = _session()
        return cls.session


if __name__ == "__main__":
    db = DatebaseSession(database="iotgateway")

    res = db.query(Device).first().device_sn
    print(res)

