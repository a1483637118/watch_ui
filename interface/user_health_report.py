from interface.base import BaseRequest
from constants.pomr_api_url import PomrApiUrl

class UserHealthReportApi(BaseRequest):
    """健康报告相关"""

    def create_or_upate(self, person_id, measure_date=None, health_states=None):
        """创建健康报告"""
        params = dict(person_id=person_id, measure_date=measure_date, id_delete=0)
        res = self.get(PomrApiUrl.report, params=params)

        #如果已经有了，就更新
        if self.check_count(res):
            pk = self.get_result(res)[0].get("id")
            params.update(health_states=health_states)
            return self.put(self.get_full_url(PomrApiUrl.report, pk), data=params)
        else:
            return self.post(PomrApiUrl.report, data=params)

    def clear(self, person_id, measure_data=None, health_states=None):
        """删除健康报告"""
        params = dict(person_id=person_id, measure_data=measure_data, health_states=health_states, id_delete=0)
        res = self.get(PomrApiUrl.report, params=params)
        if self.check_count(res):
            delete_list = [x.get("id") for x in self.get_result(res)]
            for _id in delete_list:
                self.delete(self.get_full_url(PomrApiUrl.report, _id))
        return True


if __name__ =="__main__":
    import datetime
    r = UserHealthReportApi()
    res_ = r.create_or_upate("2238151311360508", measure_date=datetime.date.today(), health_states=-3)
    print(res_)
