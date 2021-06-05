from pages.HomePage import HomePage
from pages.device_manager.DeviceManagerPage import DeviceManagerPage


class DeviceManager:

    def __init__(self, poco):
        self.home = HomePage(poco)
        self.device_manager = DeviceManagerPage(poco)

    def in_device_manager(self):
        """进入设备管理"""

        #点击设备管理
        self.home.device_manager.click()

    def in_device_detail(self):
        """进入设备详情"""
        self.in_device_manager()

        self.device_manager.watch_name.click()

    def in_find_device(self):
        """进入查找手表"""
        self.in_device_detail()


        #点击查找手表

    def in_system_alarm_manager(self):
        """进入系统提示管理"""
        self.device_manager.system_alarm_manager.click()

