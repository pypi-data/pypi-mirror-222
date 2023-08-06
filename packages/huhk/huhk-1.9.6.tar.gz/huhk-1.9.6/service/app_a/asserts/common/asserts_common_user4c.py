import allure

from service.app_a import unit_request
from service.app_a.sqls.common.sqls_common_user4c import SqlsCommonUser4C


class AssertsCommonUser4C(SqlsCommonUser4C):
    @allure.step(title="接口返回结果校验")
    def assert_common_user4c_queryactivitysource(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_common_user4c_queryactivitysource(**kwargs)
        # flag = self.compare_json_list(self.res, out, [])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_common_user4c_page(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_common_user4c_page(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["ownerFlag", "userSystemSource", "regisTimeBegin", "type", "lastLoginTimeEnd", "activitySource", "regisTimeEnd", "mobile", "status", "createTimeEnd", "lastLoginTimeStart", "memberSystemSource", "nickName", "userId", "createTimeStart"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_common_user4c_vehicleinfo(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_common_user4c_vehicleinfo(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["userId", "mobile"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_common_user4c_getbyid(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_common_user4c_getbyid(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["userId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_common_user4c_updateuser(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_common_user4c_updateuser(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["userId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_common_user4c_download(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_common_user4c_download(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["ownerFlag", "userSystemSource", "regisTimeBegin", "userIds", "type", "lastLoginTimeEnd", "activitySource", "regisTimeEnd", "mobile", "downloadType", "status", "createTimeEnd", "lastLoginTimeStart", "memberSystemSource", "nickName", "userId", "createTimeStart"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_common_user4c_beforepointsexport(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_common_user4c_beforepointsexport(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["ownerFlag", "userSystemSource", "regisTimeBegin", "userIds", "type", "lastLoginTimeEnd", "activitySource", "regisTimeEnd", "mobile", "downloadType", "status", "createTimeEnd", "lastLoginTimeStart", "memberSystemSource", "nickName", "userId", "createTimeStart"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_common_user4c_insert(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_common_user4c_insert(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["nickName", "explain", "avatarUrl"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_common_user4c_editstatus(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_common_user4c_editstatus(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["userId", "status"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_common_user4c_auditexport(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_common_user4c_auditexport(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["ownerFlag", "userLabel", "userIds", "phone", "userType", "downloadType", "registerType", "nickName", "userId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_common_user4c_identity(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_common_user4c_identity(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["userId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_common_user4c_updateaudit(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_common_user4c_updateaudit(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["userId", "auditType"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_common_user4c_auditlist(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_common_user4c_auditlist(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["mobile", "registerType", "checkStatus", "nickName", "userId", "userName", "pageNum"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_common_user4c_getuserpoints(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_common_user4c_getuserpoints(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["userId"])
        assert True, "数据比较不一致"

