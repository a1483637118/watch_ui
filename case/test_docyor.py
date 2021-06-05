from operation.doctorOfficeOperation import DoctorOfficeOperation
from utils.session import PocoSession
from pages.DoctorOfficePage import DoctorOfficePage
from conf.default import DefaultConfig
from pages.HomePage import HomePage
from airtest.core.api import *
import pytest
import allure



class TestDoctor:

    def setup_class(self):

        self.poco_session = PocoSession().get_poco()
        self.home = HomePage(self.poco_session)
        self.doctor_office_page = DoctorOfficePage(self.poco_session)
        self.doctor_office_operation = DoctorOfficeOperation(self.poco_session)

    def setup_method(self):
        start_app(DefaultConfig.app_package_name)
        self.home.cancel.wait_for_appearance(10)
        if self.home.cancel.wait():
            self.home.cancel.click()


    def teardown_method(self):
        # TODO 要保证回到首页
        stop_app(DefaultConfig.app_package_name)

    @pytest.mark.parametrize("name", ["心内科", "肿瘤内科"])
    def test_in_doctor(self, name):

        with allure.step("点击首页的科室名字"):
            self.doctor_office_operation.get_into_doctor_office(name)

        with allure.step("判断是否出现对应的科室页面"):
            if name == "全部科室":
                exists(self.doctor_office_page.all_office)
            else:
                self.doctor_office_page.ask_doctor.exists()

        with allure.step("点击返回到首页"):
            self.doctor_office_page.click_back()

