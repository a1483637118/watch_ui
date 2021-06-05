from pages.base import BasePage


class RealTimeHistoryListPage(BasePage):
    """实时数据-历史数据列表"""

    def __init__(self, poco):
        super().__init__(poco)

    @property
    def back(self):
        """返回按钮"""
        return self.poco("android:id/content").offspring("com.pajk.iwear:id/iwb_main").child(
            "android.webkit.WebView").child("android.webkit.WebView").offspring("root").child(
            "android.view.View").child("android.view.View")[0].child("android.view.View").child("android.view.View")[0]


    @property
    def not_data_content(self):
        """无数据显示内容"""
        return self.poco(text="抱歉，您暂无监测数据")

    @property
    def title(self):
        """标题"""
        return self.poco(text="历史数据")

    @property
    def select_box(self):
        """时间下拉框"""
        return self.poco("android:id/content").offspring("com.pajk.iwear:id/iwb_main").child(
            "android.webkit.WebView").child("android.webkit.WebView").offspring("root").child(
            "android.view.View").child("android.view.View")[0].child("android.view.View").child(
            "android.view.View")[2].child("android.view.View")[1]

    @property
    def cancel(self):
        """历史数据页面-时间控件-取消"""
        return self.poco(text="取消")

    @property
    def confirm(self):
        """历史数据页面-时间控件-确定"""
        return self.poco(text="确定")
