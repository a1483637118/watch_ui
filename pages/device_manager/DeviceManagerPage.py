from pages.base import BasePage


class DeviceManagerPage(BasePage):

    def __init__(self, poco):
        self.poco = poco
        super().__init__(poco)

    @property
    def back(self):
        """返回按钮"""
        return self.poco("android:id/content").offspring("  ")

    @property
    def watch_name(self):
        """手表名字"""
        return self.poco("澔医健康运动卫士手表")

    @property
    def add_device(self):
        """添加设备"""
        return self.poco("添加设备")

    @property
    def system_alarm_manager(self):
        """系统提示管理"""
        return self.poco("系统提示管理")
