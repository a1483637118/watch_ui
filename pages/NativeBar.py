from pages.base import BasePage


class NativeBar(BasePage):

    @property
    def home(self):
        """首页"""
        return self.poco("com.pajk.iwear:id/tab_main")

    @property
    def support(self):
        """运动"""
        return self.poco("com.pajk.iwear:id/tab_sport")

    @property
    def food(self):
        """饮食"""
        return self.poco("com.pajk.iwear:id/tab_food")

    @property
    def my(self):
        """我的"""
        return self.poco("com.pajk.iwear:id/tab_my")
