from pages.HomePage import HomePage
from pages.real_time.RealTimePage import RealTimePage
from pages.real_time.RealTimeHistoryListPage import RealTimeHistoryListPage


class RealTimeOperation(RealTimePage):
    """实时数据操作类"""

    def __init__(self, poco):
        super().__init__(poco)
        self.home = HomePage(self._poco)
        self.history_list_page = RealTimeHistoryListPage(self._poco)

    def in_real_time_page(self):
        """进入手表实时数据页面"""

        #首页点击心率
        self.home.heart_rate.click()

    def consult_my_doctor_by_heart_rate(self):
        """通过心率标签咨询我的专家医生"""

        #进入手表实时数据页面

        self.in_real_time_page()

        self.wait_for(self._poco(text="今日"))

        #向上滑动
        self.up()
        self.wait_for(self.consult_my_doctor)

        #点击咨询医生按钮
        self.consult_my_doctor.click()

    def enter_history(self):
        """进入历史数据"""

        #进入手表实时数据页面
        self.in_real_time_page()

        #点击历史数据
        self.history_data.click()

    def switch_tab(self, tab_index):
        """手表实时数据页面，切换tab"""
        if tab_index == 0:
            self.tab_heart_rate.click()
        elif tab_index == 1:
            self.tab_blood_pressure.click()
        elif tab_index == 2:
            self.tab_blood_oxygen.click()

