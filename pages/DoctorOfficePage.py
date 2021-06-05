from pages.base import BasePage
from airtest.core.api import *


class DoctorOfficePage(BasePage):

    def __init__(self, poco):
        super().__init__(poco)

    @property
    def all_office(self):
        """全科"""
        return self.get_image_element(DoctorOfficePage.__name__, "all_office")

    @property
    def ask_doctor(self):
        """问医生"""
        return self.poco(text="问医生")

    @property
    def click_back(self):
        """点击返回"""
        return touch(self.get_image_element(DoctorOfficePage.__name__, "back"))

