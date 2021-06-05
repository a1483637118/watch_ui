from pages.base import BasePage

class SystemAlarmManagerPage(BasePage):
    """系统提示管理页面"""
    def __init__(self, poco):
        super().__init__(poco)

    @property
    def title(self):
        """标题"""
        return self.poco(text="系统提示管理")
