from operation.consultOperation import ConsultOperation
from operation.real_timeOperation import RealTimeOperation
from utils.session import PocoSession
from utils.deviceUtil import record
from case.base import BaseTest
import pytest
import allure


class TestTry(BaseTest):


    def setup_class(self):
        self.consult = ConsultOperation(PocoSession().get_poco())
        self.real_time_operation = RealTimeOperation(PocoSession.get_poco())
        self.consult.check_env_message()


    @allure.description("实时数据-心率-咨询医生")
    @pytest.mark.back
    @pytest.mark.smoke
    @record(BaseTest._poco)

    def test_consult_my_doctor(self):

        with allure.step("从实时数据-心率-问诊界面"):
            self.real_time_operation.consult_my_doctor_by_heart_rate()

        with allure.step("导诊输入"):
            self.consult.input_consult_content()

        with allure.step("判断是否进入医生页面"):
            assert self.consult.doctor_title is True


if __name__ == "__main__":
    pytest.main()

