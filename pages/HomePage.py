from pages.base import BasePage


class HomePage(BasePage):
    """首页"""


    def __init__(self, poco):
        super().__init__(poco)


    @property
    def cancel(self):
        """环境弹窗-取消"""
        return self.poco(text="取消")

    @property
    def device_manager(self):
        """设备管理"""
        return self.poco(text="设备管理")

    @property
    def heart_rate(self):
        """实时数据-心率"""
        return self.poco(text="心率")

    @property
    def blood_pressure(self):
        """实时数据-血压"""
        return self.poco(text="血压")

    @property
    def blood_oxygen(self):
        """实时数据-血氧"""
        return self.poco(text="血氧")

    @property
    def temperature(self):
        """实时数据-体温"""
        return self.poco(text="体温")

    @property
    def sleep_data(self):
        """器官睡眠"""
        return self.poco(text="器官睡眠")

    @property
    def brain_death_warning(self):
        """脑卒中预警"""
        return self.poco(text="脑卒中预警")

    @property
    def myocardial_infarction_warning(self):
        """心梗预警"""
        return self.poco(text="心梗预警")

    @property
    def close_service(self):
        """贴心服务"""
        return self.poco(text="贴心服务")

    @property
    def analyzing_situation(self):
        """分析状况"""
        return self.poco(text="分析状况")

    @property
    def history_report_by_view(self):
        """历史健康统计-查看分析"""
        return self.poco(text="查看分析")

    @property
    def consult_my_doctor(self):
        """咨询我的专家医生"""
        return self.poco(text="咨询我的专家医生")

    @property
    def xin_nei_ke(self):
        """心内科"""
        return self.poco(text="心内科")

    @property
    def my_friend(self):
        """我的亲友入口"""
        return self.get_image_element(HomePage.__name__, "my_friend")

    @property
    def house(self):
        """首页NATIVE_BAR"""
        return self.get_image_element(HomePage.__name__, "huose")
