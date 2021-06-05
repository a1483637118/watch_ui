from operation.consultOperation import ConsultOperation
from operation.deviceOperation import DeviceManager
from pages.user_center.MyFriendPage import MyFriendPage
from utils.session import PocoSession
from utils.deviceUtil import record
from pages.HomePage import HomePage
from airtest.core.api import *
import allure


class TestHome:
    """最小回归集"""

    def setup_class(self):
        self.poco_session = PocoSession().get_poco()
        self.home = HomePage(self.poco_session)
        self.my_friend = MyFriendPage(self.poco_session)
        self.consult_operation = ConsultOperation(self.poco_session)
        self.device_manager = DeviceManager(self.poco_session)

    @record(PocoSession.get_poco(), 2)
    def test_goto_my_friend(self):
        """进入我的亲友"""
        with allure.step("顶部亲友状态栏点击左侧人物图标"):
            touch(self.home.my_friend)

        with allure.step("查看是否跳转至我的亲友页面"):
            assert self.my_friend.title.get_text() == "我的亲友"

        with allure.step("点击返回"):
            self.my_friend.click_back()

        with allure.step("校验返回首页了"):
            """判断文件my_friend存不存在"""
            exists(self.home.my_friend)

    @record(PocoSession().get_poco())
    def test_history_health_count(self):
        """当月历史健康报告详情"""
        with allure.step("点击历史统计"):
            self.home.history_report_by_view.click()

