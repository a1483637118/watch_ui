from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime


Base = declarative_base()


class Device(Base):
    """设备表"""

    __tablename__ = "device"

    id = Column(Integer, primary_key=True)
    uid = Column(Integer, default=0)
    product_id = Column(String(50), default="HJKGD01")
    device_name = Column(String(100))
    device_sn = Column(String(100))
    ota_version = Column(String(100), default="")
    bind_status = Column(Integer, default=0)
    status = Column(Integer, default=0)
    gmt_created = Column(DateTime, default=datetime.now)
    gmt_modified = Column(DateTime, default=datetime.now)
    is_deleted = Column(Integer, default=0)
    version = Column(Integer, default=0)
    device_secret = Column(String(100))
    device_detail = Column(String(500), default="auto_virtual")




class UserDevice(Base):
    """设备绑定表"""

    __tablename__ = "user_device"

    id = Column(Integer, primary_key=True)
    uid = Column(Integer, default=0)
    product_id = Column(String(50), default="HJKGD01")
    device_sn = Column(String(100))
    person_id = Column(String(50))
    gmt_created = Column(DateTime, default=datetime.now)
    gmt_modified = Column(DateTime, default=datetime.now)
    is_deleted = Column(Integer, default=0)
    version = Column(Integer, default=0)
    device_secret = Column(String(100))
    device_detail = Column(String(500), default="auto_virtual")
    bind_status = Column(Integer, default=0)
    qr_image = Column(String(36), default="")


class UserOtp(Base):
    """短信验证码"""

    __tablename__ = "user_otp"

    id = Column(Integer, primary_key=True)
    uid = Column(Integer, default=0)
    receiver =  Column(String(50))
    receiver_phone = Column(String(50))
    verify_code = Column(String(50))
    expired_time = Column(Integer)
    gmt_created = Column(DateTime, default=datetime.now)
    gmt_modified = Column(DateTime, default=datetime.now)
    is_deleted = Column(Integer, default=0)
    version = Column(Integer, default=0)


