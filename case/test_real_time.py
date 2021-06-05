from utils.deviceUtil import record
from utils.session import PocoSession
from operation.real_timeOperation import RealTimeOperation
from operation.consultOperation import ConsultOperation
import pytest
import allure


@allure.feature("health-center")
@allure.story("real_time")
class TestRealTime:
    """手表实时数据"""


    def setup_class(self):
        self.consult = ConsultOperation(PocoSession().get_poco())
        self.real_time_operation = RealTimeOperation(PocoSession().get_poco())


    @allure.description("实时数据-心率-咨询医生")
    @pytest.mark.back
    @pytest.mark.smoke
    def test_consult_my_doctor(self):

        with allure.step("从实时数据-心率-进入问诊页面"):
            self.real_time_operation.consult_my_doctor_by_heart_rate()


        with allure.step("导诊输入"):
            self.consult.input_consult_content()

        with allure.step("判断是否进入医生页面"):
            assert self.consult.doctor_title is True


    @record(PocoSession.get_poco())
    def test_heart_rate_history(self):
        """点击进入历史数据-没有数据"""
        """心率   历史数据"""

        self.real_time_operation.enter_history()

        #判断是否进入历史页面
        self.assertTure(self.real_time_operation.history_list_page.title.get_text(), "历史数据")

        #点击时间控件下拉框
        self.real_time_operation.history_list_page.select_box.click()

        #先取消
        self.real_time_operation.history_list_page.cancel.click()

        #再次打开确认
        self.real_time_operation.history_list_page.select_box.click()
        self.real_time_operation.history_list_page.confirm.click()

        #返回-可返回至曲线图页面
        self.real_time_operation.history_list_page.back.click()
        assert self.real_time_operation.real_time_title.exists() is True


    def test_heart_rate_history_exists_data(self):
        """点击进入历史数据-有数据"""
        # TODO
        pass

    def test_swith_blood_pressure(self):
        """切换至血压"""
        self.real_time_operation.in_real_time_page()

        self.real_time_operation.switch_tab(1)

        #判断是否切换
        self.assertTrue(self.real_time_operation.graph_title_blood_pressure.exists())

    def test_swith_blood_oxgen(self):
        """切换至血氧"""
        self.real_time_operation.in_real_time_page()

        self.real_time_operation.switch_tab(2)

        # 判断是否切换
        self.assertTrue(self.real_time_operation.graph_title_blood_oxygen.exists())


if __name__ == "main":
    pytest.main()
