from pages.base import BasePage

class RealTimePage(BasePage):
    """心率、血压、血氧实时数据页面"""


    def __init__(self, poco):
        super().__init__(poco)

    @property
    def consult_my_doctor(self):
        """咨询我的专家医生"""
        return self.poco(text="咨询我的专家医生")

    @property
    def history_data(self):
        """历史数据"""
        return self.poco(text="历史数据")

    @property
    def real_time_title(self):
        """实时数据-标题"""
        return self.poco(text="手表实时数据")

    @property
    def tab_heart_rate(self):
        """tab-心率"""
        return self.poco(text="心率")

    @property
    def tab_blood_pressure(self):
        """tab-血压"""
        return self.poco(text="手腕血压")

    @property
    def tab_blood_oxygen(self):
        """tab-血氧"""
        return self.poco(text="血氧")

    @property
    def graph_title_heart_rate(self):
        """日心率曲线图"""
        return self.poco(text="日心率曲线图")

    @property
    def graph_title_blood_pressure(self):
        """日血压曲线图"""
        return self.poco(text="日血压曲线图")

    @property
    def graph_title_blood_oxygen(self):
        """日血氧曲线图"""
        return self.poco(text="日血氧曲线图")
