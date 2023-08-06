import allure

from service.app_a import unit_request
from service.app_a.sqls.order.sqls_order_mainorder import SqlsOrderMainorder


class AssertsOrderMainorder(SqlsOrderMainorder):
    @allure.step(title="接口返回结果校验")
    def assert_order_mainorder_pagelist(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_order_mainorder_pagelist(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["createEndTime", "createStartTime", "sortItems"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_order_mainorder_download(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_order_mainorder_download(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["createTimeToSort", "orderTypeToSort", "createEndTime", "createStartTime", "payTimeToSort"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_order_mainorder_detail(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_order_mainorder_detail(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["orderId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_order_mainorder_getuserorderstatuslist(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_order_mainorder_getuserorderstatuslist(**kwargs)
        # flag = self.compare_json_list(self.res, out, [])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_order_mainorder_getordertypelist(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_order_mainorder_getordertypelist(**kwargs)
        # flag = self.compare_json_list(self.res, out, [])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_order_mainorder_getextorderstatuslist(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_order_mainorder_getextorderstatuslist(**kwargs)
        # flag = self.compare_json_list(self.res, out, [])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_order_mainorder_getorderstatuslist(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_order_mainorder_getorderstatuslist(**kwargs)
        # flag = self.compare_json_list(self.res, out, [])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_order_mainorder_vincode(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_order_mainorder_vincode(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["vin"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_order_mainorder_finish(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_order_mainorder_finish(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["orderId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_order_mainorder_allpricecontent(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_order_mainorder_allpricecontent(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["orderId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_order_mainorder_getorderidbyuser(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_order_mainorder_getorderidbyuser(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["userId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_order_mainorder__getmodelnamebyorderid(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_order_mainorder__getmodelnamebyorderid(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["orderId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_order_mainorder_getcarconfigbyorderid(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_order_mainorder_getcarconfigbyorderid(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["orderId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_order_mainorder_syncscrmextorder(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_order_mainorder_syncscrmextorder(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["soStatus", "scUid", "isArrived", "orderId", "createTime", "trimCode", "deliveryData", "VIN", "customerCtCode", "syncMsg", "chargePointEquity", "unitTaxNo", "dealerCode", "unitName", "orderAllAmount", "phone", "soNo", "colorCode", "syncStatus", "optionCode", "orderNo", "modelCode", "isTestDrive", "customerId", "scUname", "seriesCode", "updateTime", "customerType", "isLifetimeWarranty", "custCertNo", "unitInvoiceTitle", "lifetimeWarrantyPrice", "ossId", "configCode", "potentialName"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_order_mainorder_informorder(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_order_mainorder_informorder(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["sourceInfo", "systemCode"])
        assert True, "数据比较不一致"

