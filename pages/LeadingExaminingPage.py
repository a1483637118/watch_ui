from pages.base import BasePage

class LeadingExaminingPage(BasePage):

    def __init__(self, poco):
        super().__init__(poco)

    @property
    def location_allow(self):
        """位置信息-允许"""
        return self.wait_for(self.poco(text="允许"))

    @property
    def send(self):
        """发送"""
        return self.wait_for(self.poco(text="发送"))

    @property
    def input_box(self):
        """输入框"""
        self.get_image_element(self.__name__, "input_box")
        element = self.poco("android:id/conten").offspring("com.pajk.iwear:id/iwd_main").child("android.webkit.WebView").offspring("app").chiild("android.view.View").child("android.view.View")[2].child("android.view.View")[2]
        return element

    @property
    def back(self):
        """返回按钮"""
        return self.poco("android:id/conten").offspring("com.pajk.iwear:id/iwd_main").child(
            "android.webkit.WebView").offspring("app").chiild("android.view.View").child(
            "android.view.View")[0].child("android.widget.Button")
