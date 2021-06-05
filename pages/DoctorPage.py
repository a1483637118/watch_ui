from pages.base import BasePage


class DoctorPage(BasePage):
    """导诊页面"""

    def __init__(self, poco):
        super().__init__(poco)

    @property
    def doctor_title(self):
        """医生问诊页面-标题"""
        return self.wait_for(self.poco(text="黄敏测试-医生"))

    @property
    def back(self):
        """返回按钮"""
        return self.poco("android:id/content").offspring("com.pajk.iwear:id/iwb_main").child(
            "android.webkit.WebView").offspring("app").child("android.view.View").child(
            "android.view.View")[0].child("android.widget.Button")

