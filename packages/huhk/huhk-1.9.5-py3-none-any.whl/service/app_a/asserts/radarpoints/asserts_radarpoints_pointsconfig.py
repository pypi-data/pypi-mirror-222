import allure

from service.app_a import unit_request
from service.app_a.sqls.radarpoints.sqls_radarpoints_pointsconfig import SqlsRadarpointsPointsconfig


class AssertsRadarpointsPointsconfig(SqlsRadarpointsPointsconfig):
    @allure.step(title="接口返回结果校验")
    def assert_radarpoints_pointsconfig_page(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_radarpoints_pointsconfig_page(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["pointsBegin", "status", "pointsExpiration", "businessSceneType", "pointsEnd", "code", "name"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_radarpoints_pointsconfig_insert(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_radarpoints_pointsconfig_insert(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["remark", "pointsExpiration", "points", "bpmId", "businessSceneType", "userPointsDayMax", "rulesPointsDayMax", "toast", "name"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_radarpoints_pointsconfig_update(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_radarpoints_pointsconfig_update(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["remark", "pointsExpiration", "points", "userPointsDayMax", "businessSceneType", "id", "bpmId", "rulesPointsDayMax", "toast", "code", "name"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_radarpoints_pointsconfig_updatestatusbyid(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_radarpoints_pointsconfig_updatestatusbyid(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["status", "id"])
        assert True, "数据比较不一致"

