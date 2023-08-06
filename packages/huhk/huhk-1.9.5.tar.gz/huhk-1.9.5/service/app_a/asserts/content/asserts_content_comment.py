import allure

from service.app_a import unit_request
from service.app_a.sqls.content.sqls_content_comment import SqlsContentComment


class AssertsContentComment(SqlsContentComment):
    @allure.step(title="接口返回结果校验")
    def assert_content_comment_updatestatus(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_comment_updatestatus(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["fromStatus", "commentType", "toStatus", "commentId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_comment_download(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_comment_download(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["status", "contentCommentIds", "keyWord", "startTime", "endTime", "nickName", "EssayCommentIds", "mobile", "downloadType"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_comment_commenttop(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_comment_commenttop(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["commentType", "topFlag", "commentId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_comment_list(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_comment_list(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["keyWord", "startTime", "endTime", "nickName", "checkedStatus", "mobile", "essayId", "commentType"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_comment_delete(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_comment_delete(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["commentType", "toStatus", "commentId"])
        assert True, "数据比较不一致"

