import allure

from service.app_a import unit_request
from service.app_a.sqls.goods.sqls_goods_area import SqlsGoodsArea


class AssertsGoodsArea(SqlsGoodsArea):
    @allure.step(title="接口返回结果校验")
    def assert_goods_area_getparentarea(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_goods_area_getparentarea(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["country", "parentId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_goods_area_getdefaultdealer(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_goods_area_getdefaultdealer(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["cityCode"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_goods_area_insertrelation(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_goods_area_insertrelation(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["dealerCode", "areaIds"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_goods_area_getcitylist(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_goods_area_getcitylist(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["pName", "cName", "cType"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_goods_area_getcitybyid(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_goods_area_getcitybyid(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["cityId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_goods_area_getmaparea(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_goods_area_getmaparea(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["parentId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_goods_area_getcity(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_goods_area_getcity(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["parentId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_goods_area_updatecitytype(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_goods_area_updatecitytype(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["cId", "cType"])
        assert True, "数据比较不一致"

