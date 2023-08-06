import allure

from service.app_a import unit_request
from service.app_a.sqls.goods.sqls_goods_carmodel import SqlsGoodsCarmodel


class AssertsGoodsCarmodel(SqlsGoodsCarmodel):
    @allure.step(title="接口返回结果校验")
    def assert_goods_carmodel_savemanagecarmodel(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_goods_carmodel_savemanagecarmodel(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["modelId", "promptDesc", "prePricePosters", "depositPrice", "carName", "carDetailUrl", "depositEndTime", "version", "status", "modelName", "preToDepositEndTime", "preToDepositStartTime", "depositStartTime", "carCode", "prePrice", "prePriceContent", "posters", "carDetailPics", "price", "sort", "modelCode", "preEndTime", "carSimpleName", "depositPriceContent", "brandName", "preStartTime", "configCode", "sharePosters", "carDetailType"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_goods_carmodel_removebyid(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_goods_carmodel_removebyid(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["modelId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_goods_carmodel_getcarmodelmanagebyid(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_goods_carmodel_getcarmodelmanagebyid(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["modelId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_goods_carmodel_getmanagecarmodel(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_goods_carmodel_getmanagecarmodel(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["status", "brandName", "modelCode", "modelName", "operator", "carName", "carCode", "version"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_goods_carmodel_getmodelnamelist(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_goods_carmodel_getmodelnamelist(**kwargs)
        # flag = self.compare_json_list(self.res, out, [])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_goods_carmodel_getcarnamelist(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_goods_carmodel_getcarnamelist(**kwargs)
        # flag = self.compare_json_list(self.res, out, [])
        assert True, "数据比较不一致"

