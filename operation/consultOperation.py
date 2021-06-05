from pages.LeadingExaminingPage import LeadingExaminingPage
from pages.DoctorPage import DoctorPage

class ConsultOperation(LeadingExaminingPage, DoctorPage):
    """问诊流程"""
    def __init__(self, poco):
        super().__init__(poco)

    def input_consult_content(self, message="头疼"):
        """输入问诊并发送"""

        self.input_box.set_text(message)

        self.send.click()
