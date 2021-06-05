from pages.base import BasePage


class DeviceDetailPage(BasePage):

    @property
    def back(self):
        """返回"""
        return self.poco("android:id/content").offspring("  ")

