from pages.base import BasePage
from airtest.core.api import touch


class MyFriendPage(BasePage):
    """我的亲友"""

    def __init__(self, poco):
        super().__init__(poco)

    # def my_friend(self):
    #     """点击我的亲友"""
    #     return touch(self.get_image_element(MyFriendPage.__name__, "my_friend"))
    #   自行添加的

    def click_back(self):
        """点击返回按钮"""
        return touch(self.get_image_element(MyFriendPage.__name__, "back"))

    @property
    def title(self):
        """标题"""
        return self.poco(text="我的亲友")

    @property
    def add_friend(self):
        """添加亲友"""
        return self.poco(text="添加亲友")
