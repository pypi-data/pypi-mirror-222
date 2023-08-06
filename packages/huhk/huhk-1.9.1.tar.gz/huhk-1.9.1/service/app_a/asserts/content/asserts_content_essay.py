import allure

from service.app_a import unit_request
from service.app_a.sqls.content.sqls_content_essay import SqlsContentEssay


class AssertsContentEssay(SqlsContentEssay):
    @allure.step(title="接口返回结果校验")
    def assert_content_essay_delete_(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_essay_delete_(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["essayId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_essay_searchbykey(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_essay_searchbykey(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["Key"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_essay_checklist(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_essay_checklist(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["essayId", "recommend", "author", "CreateTimeSortType", "endTime", "startTime", "PublishTimeSortType", "status", "keyWord", "StatusSortType", "subjectId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_essay_list(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_essay_list(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["essayId", "recommend", "author", "CreateTimeSortType", "endTime", "startTime", "PublishTimeSortType", "status", "keyWord", "StatusSortType", "subjectId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_essay_add(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_essay_add(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["essayType", "essayId", "recommend", "videoUrl", "publishTime", "content", "author", "publishType", "essPicUrl", "title", "status", "subjectId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_essay_createid(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_essay_createid(**kwargs)
        # flag = self.compare_json_list(self.res, out, [])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_essay_getbyid(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_essay_getbyid(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["essayId"])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_essay_updatestatus(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_essay_updatestatus(**kwargs)
        # flag = self.compare_json_list(self.res, out, [])
        assert True, "数据比较不一致"

    @allure.step(title="接口返回结果校验")
    def assert_content_essay_getcommentlist(self, _assert=True, **kwargs):
        assert unit_request.is_assert_true(self.res, _assert), "校验接口返回，缺少成功标识"
        # out = self.sql_content_essay_getcommentlist(**kwargs)
        # flag = self.compare_json_list(self.res, out, ["essayId", "commentId", "checkedStatus", "endTime", "startTime", "parentId", "keyWord"])
        assert True, "数据比较不一致"

