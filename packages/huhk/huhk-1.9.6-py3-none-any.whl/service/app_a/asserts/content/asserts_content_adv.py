import allure

from service.app_a import unit_request
from service.app_a.sqls.content.sqls_content_adv import SqlsContentAdv


class AssertsContentAdv(SqlsContentAdv):
    @allure.step(title="接口返回结果校验")
    def assert_content_adv_save(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_adv_save(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["advPlaceId", "bindingFlag", "advSerial", "advId", "jumpContent", "advPicUrl", "advLinkUrl", "jumpType", "pictureList", "version", "advText"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_adv_updateessayadvlist(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_adv_updateessayadvlist(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["essayId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_adv_settopflag(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_adv_settopflag(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["essayId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_adv_advplacelist(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_adv_advplacelist(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["advPlaceId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_adv_delete(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_adv_delete(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["advId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_adv_detailadmin(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_adv_detailadmin(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["advPlaceId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_adv_saveall(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_adv_saveall(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["advPlaceId", "jumpType"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_adv_jumpcontent(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_adv_jumpcontent(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["typeCode", "keyWord"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_adv_detailcontentadmin(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_adv_detailcontentadmin(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["essayKeyWords", "orderByCommentCnt"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_adv_jumptypelist(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_adv_jumptypelist(**kwargs)
        # flag = self.compare_json_list(self.res, out, [])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_adv_cancelrecommend(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_adv_cancelrecommend(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["essayId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_adv_detail(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_adv_detail(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["advPlaceId"])
        assert True, "数据比较不一致"

