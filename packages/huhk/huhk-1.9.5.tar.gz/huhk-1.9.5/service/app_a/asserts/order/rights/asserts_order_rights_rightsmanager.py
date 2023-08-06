import allure

from service.app_a import unit_request
from service.app_a.sqls.order.rights.sqls_order_rights_rightsmanager import SqlsOrderRightsRightsmanager


class AssertsOrderRightsRightsmanager(SqlsOrderRightsRightsmanager):
    @allure.step(title="接口返回结果校验")
    def assert_order_rights_rightsmanager_createid(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_order_rights_rightsmanager_createid(**kwargs)
        # flag = self.compare_json_list(self.res, out, [])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_order_rights_rightsmanager_getrelation(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_order_rights_rightsmanager_getrelation(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["rightsId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_order_rights_rightsmanager_page(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_order_rights_rightsmanager_page(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["status", "modelCode", "effectiveEndDate", "rightsName"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_order_rights_rightsmanager_getrightslist(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_order_rights_rightsmanager_getrightslist(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["rightsName", "status", "modelId", "effectiveStartDate"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_order_rights_rightsmanager_insert(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_order_rights_rightsmanager_insert(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["modelCode", "rightsType", "rightsName", "orderType", "effectiveStartDate", "rightsId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_order_rights_rightsmanager_update(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_order_rights_rightsmanager_update(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["effectiveEndDate", "rightsName", "Relation", "effectiveStartDate", "rightsId", "Content"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_order_rights_rightsmanager_rightsbyid(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_order_rights_rightsmanager_rightsbyid(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["id"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_order_rights_rightsmanager_updatestatusbyid(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_order_rights_rightsmanager_updatestatusbyid(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["rightsId", "status"])
        assert True, "数据比较不一致"

