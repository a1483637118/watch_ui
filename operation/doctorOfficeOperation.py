from pages.HomePage import HomePage


class DoctorOfficeOperation(HomePage):

    def __init__(self, poco):
        super().__init__(poco)


    def get_into_doctor_office(self, office_name="全部科室"):
        """从首页进入某个科室"""
        print(f"传进来的科室:{office_name}")
        #向上滑动到中间位置
        self.up()
        self.poco(text=office_name).click()
