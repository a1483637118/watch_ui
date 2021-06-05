from interface.base import BaseRequest
from constants.pomr_api_url import PomrApiUrl


class DeviceInterface(BaseRequest):

    def get_bind_device_by_person(self, person_id):
        """根据person_id获取绑定的设备"""
        parms = {
            "person_id": person_id,
            "bind_status": 1
        }
        res = self.get_first_result(self.get(PomrApiUrl.report, parms=parms))
        device_sn = res.get("device_sn")
        return device_sn
