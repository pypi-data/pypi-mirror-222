import allure

from service.app_a.asserts.content.asserts_content_essay import AssertsContentEssay
from service.app_a.apis.content import apis_content_essay


class FunsContentEssay(AssertsContentEssay):
    @allure.step(title="专题-后台APP专题文章删除-Y")
    def content_essay_delete_(self, essayId="$None$", _assert=True, _all_is_None=False,  **kwargs):
        """
            url=/content/essay/delete/{essayId}
                params: essayId :  : 文章id
                params: headers : 请求头
        """
        essayId = self.get_value_choice(essayId, list_or_dict=None, key=None, _all_is_None=_all_is_None)

        _kwargs = self.get_kwargs(locals())
        self.res = apis_content_essay.content_essay_delete_(**_kwargs)

        self.assert_content_essay_delete_(_assert, **_kwargs)
        self.set_value(_kwargs)


    @allure.step(title="专题-后台App文章关键词搜索-Y")
    def content_essay_searchbykey(self, size=10, Key="$None$", current=1, _assert=True,  **kwargs):
        """
            url=/content/essay/searchByKey
                params: Key :  : 关键词
                params: size :  : 条数
                params: current :  : 当前页
                params: headers : 请求头
        """
        Key = self.get_list_choice(Key, list_or_dict=None, key="Key")

        _kwargs = self.get_kwargs(locals())
        self.res = apis_content_essay.content_essay_searchbykey(**_kwargs)

        self.assert_content_essay_searchbykey(_assert, **_kwargs)
        self.set_output_value(_kwargs)
        self.set_value(_kwargs)


    @allure.step(title="后台管理-内容审核列表1030-Y")
    def content_essay_checklist(self, author="$None$", subjectId="$None$", StatusSortType="$None$", essayId="$None$", current=1, PublishTimeSortType="$None$", keyWord="$None$", endTime="$None$", startTime="$None$", status="$None$", CreateTimeSortType="$None$", recommend="$None$", size=10, _assert=True,  **kwargs):
        """
            url=/content/essay/checkList
                params: essayId :  : 文章主键
                params: keyWord :  : 文章搜索关键字
                params: author :  : 作者
                params: startTime :  : 搜索开始时间
                params: endTime :  : 搜索结束时间
                params: subjectId :  : 专题主键
                params: status :  : 文章状态1：待上架2：已上架3：已下架4：已删除 5 待审核 6 审核不通过 7草稿
                params: size :  : 每页条数
                params: current :  : 当前页数
                params: recommend :  : 是否推荐 1：推荐页0：非推荐页
                params: PublishTimeSortType :  : 发布时间排序方式 默认倒序，正序  ASC 倒序 DESC
                params: CreateTimeSortType :  : 创建时间排序方式 默认倒序，  正序  ASC 倒序 DESC
                params: StatusSortType :  : 状态排序方式 默认倒序，  正序  ASC 倒序 DESC
                params: headers : 请求头
        """
        author = self.get_list_choice(author, list_or_dict=None, key="author")
        subjectId = self.get_list_choice(subjectId, list_or_dict=None, key="subjectId")
        StatusSortType = self.get_list_choice(StatusSortType, list_or_dict=None, key="StatusSortType")
        essayId = self.get_list_choice(essayId, list_or_dict=None, key="essayId")
        PublishTimeSortType = self.get_list_choice(PublishTimeSortType, list_or_dict=None, key="PublishTimeSortType")
        keyWord = self.get_list_choice(keyWord, list_or_dict=None, key="keyWord")
        endTime = self.get_list_choice(endTime, list_or_dict=None, key="endTime")
        startTime = self.get_list_choice(startTime, list_or_dict=None, key="startTime")
        status = self.get_list_choice(status, list_or_dict=None, key="status")
        CreateTimeSortType = self.get_list_choice(CreateTimeSortType, list_or_dict=None, key="CreateTimeSortType")
        recommend = self.get_list_choice(recommend, list_or_dict=None, key="recommend")

        _kwargs = self.get_kwargs(locals())
        self.res = apis_content_essay.content_essay_checklist(**_kwargs)

        self.assert_content_essay_checklist(_assert, **_kwargs)
        self.set_output_value(_kwargs)
        self.set_value(_kwargs)


    @allure.step(title="后台管理-内容管理列表1030-Y")
    def content_essay_list(self, author="$None$", subjectId="$None$", StatusSortType="$None$", essayId="$None$", current=1, PublishTimeSortType="$None$", keyWord="$None$", endTime="$None$", startTime="$None$", status="$None$", CreateTimeSortType="$None$", recommend="$None$", size=10, _assert=True,  **kwargs):
        """
            url=/content/essay/list
                params: essayId :  : 文章主键
                params: keyWord :  : 文章搜索关键字
                params: author :  : 作者
                params: startTime :  : 搜索开始时间
                params: endTime :  : 搜索结束时间
                params: subjectId :  : 专题主键
                params: status :  : 文章状态1：待上架2：已上架3：已下架4：已删除 5 待审核 6 审核不通过 7草稿
                params: size :  : 每页条数
                params: current :  : 当前页数
                params: recommend :  : 是否推荐 1：推荐页0：非推荐页
                params: PublishTimeSortType :  : 发布时间排序方式 默认倒序，正序  ASC 倒序 DESC
                params: CreateTimeSortType :  : 创建时间排序方式 默认倒序，  正序  ASC 倒序 DESC
                params: StatusSortType :  : 状态排序方式 默认倒序，  正序  ASC 倒序 DESC
                params: headers : 请求头
        """
        author = self.get_list_choice(author, list_or_dict=None, key="author")
        subjectId = self.get_list_choice(subjectId, list_or_dict=None, key="subjectId")
        StatusSortType = self.get_list_choice(StatusSortType, list_or_dict=None, key="StatusSortType")
        essayId = self.get_list_choice(essayId, list_or_dict=None, key="essayId")
        PublishTimeSortType = self.get_list_choice(PublishTimeSortType, list_or_dict=None, key="PublishTimeSortType")
        keyWord = self.get_list_choice(keyWord, list_or_dict=None, key="keyWord")
        endTime = self.get_list_choice(endTime, list_or_dict=None, key="endTime")
        startTime = self.get_list_choice(startTime, list_or_dict=None, key="startTime")
        status = self.get_list_choice(status, list_or_dict=None, key="status")
        CreateTimeSortType = self.get_list_choice(CreateTimeSortType, list_or_dict=None, key="CreateTimeSortType")
        recommend = self.get_list_choice(recommend, list_or_dict=None, key="recommend")

        _kwargs = self.get_kwargs(locals())
        self.res = apis_content_essay.content_essay_list(**_kwargs)

        self.assert_content_essay_list(_assert, **_kwargs)
        self.set_output_value(_kwargs)
        self.set_value(_kwargs)


    @allure.step(title="后台管理-新建&修改内容1030-Y")
    def content_essay_add(self, videoUrl="$None$", author="$None$", title="$None$", subjectId="$None$", essayId="$None$", publishTime="$None$", essPicUrl="$None$", status="$None$", content="$None$", publishType="$None$", recommend="$None$", essayType="$None$", _assert=True, _all_is_None=False,  **kwargs):
        """
            url=/content/essay/add
                params: essayId : string : 文章主键
                params: title : string : 标题
                params: author : string : 作者
                params: publishType : number : 发布类型1：立即发布2：定时发布
                params: publishTime : string : 发布时间
                params: content : string : 富文本内容
                params: status : string : 状态 新增状态为待审核 1：待上架2：已上架 3 ：已下架4：已删除 5待审核 6 审核不通过 7 草稿
                params: essayType : string : 文章类型1：图文2：视频
                params: subjectId : array : 专题主键
                type : string : None
                params: recommend : number : 是否推荐 1：推荐页0：非推荐页
                params: essPicUrl : string : 封面
                params: videoUrl : string : 视频路径
                params: headers : 请求头
        """
        videoUrl = self.get_value_choice(videoUrl, list_or_dict=None, key=None, _all_is_None=_all_is_None)
        author = self.get_value_choice(author, list_or_dict=None, key=None, _all_is_None=_all_is_None)
        title = self.get_value_choice(title, list_or_dict=None, key=None, _all_is_None=_all_is_None)
        subjectId = self.get_value_choice(subjectId, list_or_dict=None, key=None, _all_is_None=_all_is_None)
        essayId = self.get_value_choice(essayId, list_or_dict=None, key=None, _all_is_None=_all_is_None)
        publishTime = self.get_value_choice(publishTime, list_or_dict=None, key=None, _all_is_None=_all_is_None)
        essPicUrl = self.get_value_choice(essPicUrl, list_or_dict=None, key=None, _all_is_None=_all_is_None)
        status = self.get_value_choice(status, list_or_dict=None, key=None, _all_is_None=_all_is_None)
        content = self.get_value_choice(content, list_or_dict=None, key=None, _all_is_None=_all_is_None)
        publishType = self.get_value_choice(publishType, list_or_dict=None, key=None, _all_is_None=_all_is_None)
        recommend = self.get_value_choice(recommend, list_or_dict=None, key=None, _all_is_None=_all_is_None)
        essayType = self.get_value_choice(essayType, list_or_dict=None, key=None, _all_is_None=_all_is_None)

        _kwargs = self.get_kwargs(locals())
        self.res = apis_content_essay.content_essay_add(**_kwargs)

        self.assert_content_essay_add(_assert, **_kwargs)
        self.set_value(_kwargs)


    @allure.step(title="文章-生成文章主键-Y")
    def content_essay_createid(self, _assert=True,  **kwargs):
        """
            url=/content/essay/createId
                params: headers : 请求头
        """
        _kwargs = self.get_kwargs(locals())
        self.res = apis_content_essay.content_essay_createid(**_kwargs)

        self.assert_content_essay_createid(_assert, **_kwargs)
        self.set_output_value(_kwargs)
        self.set_value(_kwargs)


    @allure.step(title="后台管理-内容详情1030-Y")
    def content_essay_getbyid(self, essayId="$None$", _assert=True,  **kwargs):
        """
            url=/content/essay/getById
                params: essayId :  : 文章主键
                params: headers : 请求头
        """
        essayId = self.get_list_choice(essayId, list_or_dict=None, key="essayId")

        _kwargs = self.get_kwargs(locals())
        self.res = apis_content_essay.content_essay_getbyid(**_kwargs)

        self.assert_content_essay_getbyid(_assert, **_kwargs)
        self.set_output_value(_kwargs)
        self.set_value(_kwargs)


    @allure.step(title="后台管理-内容审核1030-Y")
    def content_essay_updatestatus(self, _assert=True, _all_is_None=False,  **kwargs):
        """
            url=/content/essay/updateStatus
                params: headers : 请求头
        """
        _kwargs = self.get_kwargs(locals())
        self.res = apis_content_essay.content_essay_updatestatus(**_kwargs)

        self.assert_content_essay_updatestatus(_assert, **_kwargs)
        self.set_value(_kwargs)


    @allure.step(title="后台管理-评论信息1030-Y")
    def content_essay_getcommentlist(self, essayId="$None$", commentId="$None$", parentId="$None$", current=1, keyWord="$None$", endTime="$None$", checkedStatus="$None$", startTime="$None$", size=10, _assert=True,  **kwargs):
        """
            url=/content/essay/getCommentList
                params: essayId :  : 文章主键
                params: keyWord :  : 关键词
                params: checkedStatus :  : 审核状态 审核状态 0待审核 1.已上架 2.审核未通过3：已下架 5已删除
                params: startTime :  : 开始时间
                params: endTime :  : 结束时间
                params: commentId :  : 评论id
                params: parentId :  : 父级id
                params: size :  : 每页数量
                params: current :  : 当前页
                params: headers : 请求头
        """
        essayId = self.get_list_choice(essayId, list_or_dict=None, key="essayId")
        commentId = self.get_list_choice(commentId, list_or_dict=None, key="commentId")
        parentId = self.get_list_choice(parentId, list_or_dict=None, key="parentId")
        keyWord = self.get_list_choice(keyWord, list_or_dict=None, key="keyWord")
        endTime = self.get_list_choice(endTime, list_or_dict=None, key="endTime")
        checkedStatus = self.get_list_choice(checkedStatus, list_or_dict=None, key="checkedStatus")
        startTime = self.get_list_choice(startTime, list_or_dict=None, key="startTime")

        _kwargs = self.get_kwargs(locals())
        self.res = apis_content_essay.content_essay_getcommentlist(**_kwargs)

        self.assert_content_essay_getcommentlist(_assert, **_kwargs)
        self.set_output_value(_kwargs)
        self.set_value(_kwargs)


