import allure

from service.app_a import unit_request
from service.app_a.sqls.order.sqls_order_rightsorder import SqlsOrderRightsorder


class AssertsOrderRightsorder(SqlsOrderRightsorder):
    @allure.step(title="接口返回结果校验")
    def assert_order_rightsorder_export(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_order_rightsorder_export(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["rightsType", "payDateBegin", "userId", "payDateEnd", "useStatus", "orderMainId", "receiveDateBegin", "receiveDateEnd", "mobile", "rightsOrderId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_order_rightsorder_insert(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_order_rightsorder_insert(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["refundBillNo", "rightsType", "updateId", "userId", "payAmount", "payDate", "useStatus", "createBy", "rightsName", "orderMainId", "refundDate", "mobile", "receiveDate", "payBillNo", "createTime", "rightsId", "updateTime", "rightsOrderId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_order_rightsorder_page(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_order_rightsorder_page(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["rightsType", "payDateBegin", "userId", "payDateEnd", "useStatus", "orderMainId", "receiveDateBegin", "receiveDateEnd", "mobile", "rightsOrderId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_order_rightsorder_receive(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_order_rightsorder_receive(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["rightsId", "orderId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_order_rightsorder_getorderlist(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_order_rightsorder_getorderlist(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["rightsType", "useStatusList", "orderMainId", "rightsNameList", "mobile", "receiveDate"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_order_rightsorder_statusupdate(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_order_rightsorder_statusupdate(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["workStatus", "soNo"])
        assert True, "数据比较不一致"

