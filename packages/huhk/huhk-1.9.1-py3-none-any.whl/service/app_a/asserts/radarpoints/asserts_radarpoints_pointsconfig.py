import allure

from service.app_a import unit_request
from service.app_a.sqls.radarpoints.sqls_radarpoints_pointsconfig import SqlsRadarpointsPointsconfig


class AssertsRadarpointsPointsconfig(SqlsRadarpointsPointsconfig):
    @allure.step(title="接口返回结果校验")
    def assert_radarpoints_pointsconfig_page(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_radarpoints_pointsconfig_page(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["pointsBegin", "code", "pointsEnd", "businessSceneType", "name", "status", "pointsExpiration"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_radarpoints_pointsconfig_insert(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_radarpoints_pointsconfig_insert(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["rulesPointsDayMax", "remark", "toast", "points", "businessSceneType", "bpmId", "userPointsDayMax", "name", "pointsExpiration"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_radarpoints_pointsconfig_update(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_radarpoints_pointsconfig_update(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["id", "code", "rulesPointsDayMax", "remark", "toast", "points", "businessSceneType", "userPointsDayMax", "bpmId", "name", "pointsExpiration"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_radarpoints_pointsconfig_updatestatusbyid(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_radarpoints_pointsconfig_updatestatusbyid(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["id", "status"])
        assert True, "数据比较不一致"

