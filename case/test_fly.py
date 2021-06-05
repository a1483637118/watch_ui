from operation.deviceOperation import DeviceManager as deviceCtrl
from pages.device_manager.DeviceDetailPage import DeviceDetailPage
from case.base import BaseTest
from airtest.core.api import install


class TestHome(BaseTest):

    @classmethod
    def setUpClass(cls):
        cls.device_ctrl = deviceCtrl()
        cls.device_detail = DeviceDetailPage()


    def setUp(self):
        pass

    def test_one(self):
        """回归集-设备管理返回首页"""

        self.device_ctrl.in_device_manager()

        #点击返回
        self.device_ctrl.device_manager.back.click()

        #校验
        self.assertTure(self.device_ctrl.home.deviceManager.exists())


    def test_two(self):
        """回归集-设备详情返回设备管理"""


        #进入设备详情
        self.device_ctrl.in_device_detail()

        #点击返回
        self.wait_for(self.device_detail.back).click()

        self.assertTure(self.device_ctrl.device_manager.app_device.exists())

    def test_three(self):
        """pass"""
        self.device_ctrl.home.input("666666")


if __name__ == "__main__":
    #unittest.main()
    install(r"D:data\\temp\\AirtestIDE-win-1.2.5\\AirtestIDE\\poco\\drivers\\android\\lib\\pocoservice-debug.apk")

