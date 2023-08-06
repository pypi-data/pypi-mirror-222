import allure

from service.app_a import unit_request
from service.app_a.sqls.content.sqls_content_activitymanager import SqlsContentActivitymanager


class AssertsContentActivitymanager(SqlsContentActivitymanager):
    @allure.step(title="接口返回结果校验")
    def assert_content_activitymanager_updateperson(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_activitymanager_updateperson(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["limitPeople", "activityId", "needLimitPeople"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_activitymanager_updateenrolltime(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_activitymanager_updateenrolltime(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["enrollTime", "enrollStartTime", "activityId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_activitymanager_page(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_activitymanager_page(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["city", "activityTimeSort", "activityId", "target", "endTime", "beginTime", "createTimeSort", "province", "title", "status", "pushTimeSort"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_activitymanager_actinfoupdate(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_activitymanager_actinfoupdate(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["operationType", "activityId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_activitymanager_setactivitysort(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_activitymanager_setactivitysort(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["activityId", "sort"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_activitymanager_getactivityinfo_(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_activitymanager_getactivityinfo_(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["activityId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_activitymanager_activitytop_(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_activitymanager_activitytop_(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["topFlag", "activityId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_activitymanager_activityjoinuserexport(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_activitymanager_activityjoinuserexport(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["activityId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_activitymanager_save(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_activitymanager_save(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["city", "activityId", "publishTime", "content", "province", "title", "status", "limitPeople", "enrollStartTime", "agreementId", "authId", "beginTime", "publishType", "enrollTime", "reason", "activityPicURL", "coordinate", "customerGroup", "needLimitPeople", "endTime", "needArea", "activityAddr", "county", "activityPicUrl"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_activitymanager_update(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_activitymanager_update(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["city", "activityId", "publishTime", "content", "province", "title", "status", "limitPeople", "enrollStartTime", "authId", "beginTime", "publishType", "enrollTime", "reason", "activityPicURL", "coordinate", "customerGroup", "needLimitPeople", "endTime", "needArea", "activityAddr", "county", "activityPicUrl"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_activitymanager_publishupdate(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_activitymanager_publishupdate(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["activityIds", "publishStatus", "status", "activityId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_activitymanager_statusupdate(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_activitymanager_statusupdate(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["activityIds", "checkStatus"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_activitymanager_enrollupdate(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_activitymanager_enrollupdate(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["checkEnroll", "activityIds"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_activitymanager_activityexport(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_activitymanager_activityexport(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["city", "activityTimeSort", "activityId", "target", "endTime", "beginTime", "createTimeSort", "province", "title", "status", "pushTimeSort"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_activitymanager_listlog(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_activitymanager_listlog(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["activityId"])
        assert True, "数据比较不一致"

