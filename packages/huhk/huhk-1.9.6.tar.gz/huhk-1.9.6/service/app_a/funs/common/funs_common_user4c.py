import allure

from service.app_a.asserts.common.asserts_common_user4c import AssertsCommonUser4C
from service.app_a.apis.common import apis_common_user4c


class FunsCommonUser4C(AssertsCommonUser4C):
    @allure.step(title="用户列表-活动来源-Y")
    def common_user4c_queryactivitysource(self, _assert=True,  **kwargs):
        """
            url=/common/user4C/queryActivitySource
                params: headers : 请求头
        """
        _kwargs = self.get_kwargs(locals())
        self.res = apis_common_user4c.common_user4c_queryactivitysource(**_kwargs)

        self.assert_common_user4c_queryactivitysource(_assert, **_kwargs)
        self.set_output_value(_kwargs)
        self.set_value(_kwargs)


    @allure.step(title="用户列表-查询-Y")
    def common_user4c_page(self, ownerFlag="$None$", userSystemSource="$None$", regisTimeBegin="$None$", type="$None$", lastLoginTimeEnd="$None$", current=1, activitySource="$None$", regisTimeEnd="$None$", mobile="$None$", status="$None$", createTimeEnd="$None$", lastLoginTimeStart="$None$", memberSystemSource="$None$", nickName="$None$", userId="$None$", size=10, createTimeStart="$None$", _assert=True,  **kwargs):
        """
            url=/common/user4C/page
                params: mobile :  : 用户手机号码
                params: nickName :  : 用户昵称
                params: status :  : 会员状态 0：禁用 1：启用
                params: type :  : 用户类型 0：注册 1：非注册
                params: memberSystemSource :  : 会员来源系统： 1：APP、2：微信小程序、3：官网、4：H5
                params: size :  : 每页数据数
                params: current :  : 当前页数
                params: userSystemSource :  : 用户来源系统： 1：APP、2：微信小程序、3：官网、4：H5、5：SCRM、6：DMS
                params: activitySource :  : 用户活动来源 0：0元购、1：预约试驾、2：蓝牙共享车主、3：邀请好友、4：SCRM、5：DMS
                params: ownerFlag :  : 1：车主、2：使用人、3：共享车主、4：非车主；可多个标签叠加
                params: createTimeStart :  : 用户创建开始时间
                params: createTimeEnd :  : 用户创建结束时间
                params: regisTimeBegin :  : 会员注册开始时间
                params: regisTimeEnd :  : 会员注册结束时间
                params: lastLoginTimeStart :  : 用户最近登录开始时间
                params: lastLoginTimeEnd :  : 用户最近登录结束时间
                params: headers : 请求头
        """
        ownerFlag = self.get_list_choice(ownerFlag, list_or_dict=None, key="ownerFlag")
        userSystemSource = self.get_list_choice(userSystemSource, list_or_dict=None, key="userSystemSource")
        regisTimeBegin = self.get_list_choice(regisTimeBegin, list_or_dict=None, key="regisTimeBegin")
        type = self.get_list_choice(type, list_or_dict=None, key="type")
        lastLoginTimeEnd = self.get_list_choice(lastLoginTimeEnd, list_or_dict=None, key="lastLoginTimeEnd")
        activitySource = self.get_list_choice(activitySource, list_or_dict=None, key="activitySource")
        regisTimeEnd = self.get_list_choice(regisTimeEnd, list_or_dict=None, key="regisTimeEnd")
        mobile = self.get_list_choice(mobile, list_or_dict=None, key="mobile")
        status = self.get_list_choice(status, list_or_dict=None, key="status")
        createTimeEnd = self.get_list_choice(createTimeEnd, list_or_dict=None, key="createTimeEnd")
        lastLoginTimeStart = self.get_list_choice(lastLoginTimeStart, list_or_dict=None, key="lastLoginTimeStart")
        memberSystemSource = self.get_list_choice(memberSystemSource, list_or_dict=None, key="memberSystemSource")
        nickName = self.get_list_choice(nickName, list_or_dict=None, key="nickName")
        userId = self.get_list_choice(userId, list_or_dict=None, key="userId")
        createTimeStart = self.get_list_choice(createTimeStart, list_or_dict=None, key="createTimeStart")

        _kwargs = self.get_kwargs(locals())
        self.res = apis_common_user4c.common_user4c_page(**_kwargs)

        self.assert_common_user4c_page(_assert, **_kwargs)
        self.set_output_value(_kwargs)
        self.set_value(_kwargs)


    @allure.step(title="用户列表-详情-车辆信息-Y")
    def common_user4c_vehicleinfo(self, userId="$None$", size=10, mobile="$None$", current=1, _assert=True,  **kwargs):
        """
            url=/common/user4C/vehicleInfo
                params: mobile :  : 用户手机号码
                params: current :  : 页码
                params: size :  : 每页大小
                params: headers : 请求头
        """
        userId = self.get_list_choice(userId, list_or_dict=None, key="userId")
        mobile = self.get_list_choice(mobile, list_or_dict=None, key="mobile")

        _kwargs = self.get_kwargs(locals())
        self.res = apis_common_user4c.common_user4c_vehicleinfo(**_kwargs)

        self.assert_common_user4c_vehicleinfo(_assert, **_kwargs)
        self.set_output_value(_kwargs)
        self.set_value(_kwargs)


    @allure.step(title="用户中心-用户基本信息-Y")
    def common_user4c_getbyid(self, userId="$None$", _assert=True,  **kwargs):
        """
            url=/common/user4C/getById
                params: headers : 请求头
        """
        userId = self.get_list_choice(userId, list_or_dict=None, key="userId")

        _kwargs = self.get_kwargs(locals())
        self.res = apis_common_user4c.common_user4c_getbyid(**_kwargs)

        self.assert_common_user4c_getbyid(_assert, **_kwargs)
        self.set_output_value(_kwargs)
        self.set_value(_kwargs)


    @allure.step(title="用户中心-编辑官方账号-Y")
    def common_user4c_updateuser(self, userId="$None$", _assert=True, _all_is_None=False,  **kwargs):
        """
            url=/common/user4C/updateUser
                params: headers : 请求头
        """
        userId = self.get_value_choice(userId, list_or_dict=None, key=None, _all_is_None=_all_is_None)

        _kwargs = self.get_kwargs(locals())
        self.res = apis_common_user4c.common_user4c_updateuser(**_kwargs)

        self.assert_common_user4c_updateuser(_assert, **_kwargs)
        self.set_value(_kwargs)


    @allure.step(title="用户列表-导出-Y")
    def common_user4c_download(self, ownerFlag="$None$", userSystemSource="$None$", regisTimeBegin="$None$", userIds="$None$", type="$None$", lastLoginTimeEnd="$None$", activitySource="$None$", regisTimeEnd="$None$", mobile="$None$", downloadType="$None$", status="$None$", createTimeEnd="$None$", lastLoginTimeStart="$None$", memberSystemSource="$None$", nickName="$None$", userId="$None$", createTimeStart="$None$", _assert=True,  **kwargs):
        """
            url=/common/user4C/download
                params: mobile :  : 用户手机号
                params: nickName :  : 用户昵称
                params: status :  : 会员状态 0：禁用 1：启用
                params: type :  : 用户类型 0：注册 1：非注册
                params: memberSystemSource :  : 会员来源系统： 1：APP、2：微信小程序、3：官网、4：H5
                params: userSystemSource :  : 用户来源系统： 1：APP、2：微信小程序、3：官网、4：H5、5：SCRM、6：DMS
                params: activitySource :  : 用户活动来源 0：0元购、1：预约试驾、2：蓝牙共享车主、3：邀请好友、4：SCRM、5：DMS
                params: ownerFlag :  : 1：车主、2：使用人、3：共享车主、4：非车主；可多个标签叠加
                params: createTimeStart :  : 用户创建开始时间
                params: createTimeEnd :  : 用户创建结束时间
                params: regisTimeBegin :  : 会员注册开始时间
                params: regisTimeEnd :  : 会员注册结束时间
                params: lastLoginTimeStart :  : 会员最近登录开始时间
                params: lastLoginTimeEnd :  : 会员最近登录结束时间
                params: downloadType :  : 导出类型 1: 条件导出 2: 批量导出
                params: headers : 请求头
        """
        ownerFlag = self.get_list_choice(ownerFlag, list_or_dict=None, key="ownerFlag")
        userSystemSource = self.get_list_choice(userSystemSource, list_or_dict=None, key="userSystemSource")
        regisTimeBegin = self.get_list_choice(regisTimeBegin, list_or_dict=None, key="regisTimeBegin")
        userIds = self.get_list_choice(userIds, list_or_dict=None, key="userIds")
        type = self.get_list_choice(type, list_or_dict=None, key="type")
        lastLoginTimeEnd = self.get_list_choice(lastLoginTimeEnd, list_or_dict=None, key="lastLoginTimeEnd")
        activitySource = self.get_list_choice(activitySource, list_or_dict=None, key="activitySource")
        regisTimeEnd = self.get_list_choice(regisTimeEnd, list_or_dict=None, key="regisTimeEnd")
        mobile = self.get_list_choice(mobile, list_or_dict=None, key="mobile")
        downloadType = self.get_list_choice(downloadType, list_or_dict=None, key="downloadType")
        status = self.get_list_choice(status, list_or_dict=None, key="status")
        createTimeEnd = self.get_list_choice(createTimeEnd, list_or_dict=None, key="createTimeEnd")
        lastLoginTimeStart = self.get_list_choice(lastLoginTimeStart, list_or_dict=None, key="lastLoginTimeStart")
        memberSystemSource = self.get_list_choice(memberSystemSource, list_or_dict=None, key="memberSystemSource")
        nickName = self.get_list_choice(nickName, list_or_dict=None, key="nickName")
        userId = self.get_list_choice(userId, list_or_dict=None, key="userId")
        createTimeStart = self.get_list_choice(createTimeStart, list_or_dict=None, key="createTimeStart")

        _kwargs = self.get_kwargs(locals())
        self.res = apis_common_user4c.common_user4c_download(**_kwargs)

        self.assert_common_user4c_download(_assert, **_kwargs)
        self.set_output_value(_kwargs)
        self.set_value(_kwargs)


    @allure.step(title="用户列表-导出前置判断-Y")
    def common_user4c_beforepointsexport(self, ownerFlag="$None$", userSystemSource="$None$", regisTimeBegin="$None$", userIds="$None$", type="$None$", lastLoginTimeEnd="$None$", activitySource="$None$", regisTimeEnd="$None$", mobile="$None$", downloadType="$None$", status="$None$", createTimeEnd="$None$", lastLoginTimeStart="$None$", memberSystemSource="$None$", nickName="$None$", userId="$None$", createTimeStart="$None$", _assert=True,  **kwargs):
        """
            url=/common/user4C/beforePointsExport
                params: mobile :  : 用户手机号
                params: nickName :  : 用户昵称
                params: status :  : 账号状态 0：禁用 1：启用
                params: type :  : 用户类型 0：注册 1：非注册
                params: memberSystemSource :  : 用户来源系统： 1：APP、2：微信小程序、3：官网、4：H5
                params: userSystemSource :  : 用户来源系统： 1：APP、2：微信小程序、3：官网、4：H5、5：SCRM、6：DMS
                params: activitySource :  : 用户活动来源 0：0元购、1：预约试驾、2：蓝牙共享车主、3：邀请好友、4：SCRM、5：DMS
                params: ownerFlag :  :  1：车主、2：使用人、3：共享车主、4：非车主；可多个标签叠加
                params: createTimeStart :  : 用户创建开始时间
                params: createTimeEnd :  : 用户创建结束时间
                params: regisTimeBegin :  : 会员注册开始时间
                params: regisTimeEnd :  : 会员注册结束时间
                params: lastLoginTimeStart :  : 会员最近登录开始时间
                params: lastLoginTimeEnd :  : 会员最近登录结束时间
                params: downloadType :  : 1：条件导出 2：批量导出
                params: headers : 请求头
        """
        ownerFlag = self.get_list_choice(ownerFlag, list_or_dict=None, key="ownerFlag")
        userSystemSource = self.get_list_choice(userSystemSource, list_or_dict=None, key="userSystemSource")
        regisTimeBegin = self.get_list_choice(regisTimeBegin, list_or_dict=None, key="regisTimeBegin")
        userIds = self.get_list_choice(userIds, list_or_dict=None, key="userIds")
        type = self.get_list_choice(type, list_or_dict=None, key="type")
        lastLoginTimeEnd = self.get_list_choice(lastLoginTimeEnd, list_or_dict=None, key="lastLoginTimeEnd")
        activitySource = self.get_list_choice(activitySource, list_or_dict=None, key="activitySource")
        regisTimeEnd = self.get_list_choice(regisTimeEnd, list_or_dict=None, key="regisTimeEnd")
        mobile = self.get_list_choice(mobile, list_or_dict=None, key="mobile")
        downloadType = self.get_list_choice(downloadType, list_or_dict=None, key="downloadType")
        status = self.get_list_choice(status, list_or_dict=None, key="status")
        createTimeEnd = self.get_list_choice(createTimeEnd, list_or_dict=None, key="createTimeEnd")
        lastLoginTimeStart = self.get_list_choice(lastLoginTimeStart, list_or_dict=None, key="lastLoginTimeStart")
        memberSystemSource = self.get_list_choice(memberSystemSource, list_or_dict=None, key="memberSystemSource")
        nickName = self.get_list_choice(nickName, list_or_dict=None, key="nickName")
        userId = self.get_list_choice(userId, list_or_dict=None, key="userId")
        createTimeStart = self.get_list_choice(createTimeStart, list_or_dict=None, key="createTimeStart")

        _kwargs = self.get_kwargs(locals())
        self.res = apis_common_user4c.common_user4c_beforepointsexport(**_kwargs)

        self.assert_common_user4c_beforepointsexport(_assert, **_kwargs)
        self.set_output_value(_kwargs)
        self.set_value(_kwargs)


    @allure.step(title="用户列表-新增-Y")
    def common_user4c_insert(self, nickName="$None$", explain="$None$", avatarUrl="$None$", _assert=True, _all_is_None=False,  **kwargs):
        """
            url=/common/user4C/insert
                params: avatarUrl : text : String；图片地址
                params: explain : text : String；简介
                params: nickName : text : String；昵称
                params: headers : 请求头
        """
        nickName = self.get_value_choice(nickName, list_or_dict=None, key=None, _all_is_None=_all_is_None)
        explain = self.get_value_choice(explain, list_or_dict=None, key=None, _all_is_None=_all_is_None)
        avatarUrl = self.get_value_choice(avatarUrl, list_or_dict=None, key=None, _all_is_None=_all_is_None)

        _kwargs = self.get_kwargs(locals())
        self.res = apis_common_user4c.common_user4c_insert(**_kwargs)

        self.assert_common_user4c_insert(_assert, **_kwargs)
        self.set_value(_kwargs)


    @allure.step(title="用户中心-禁用/启用用户-Y")
    def common_user4c_editstatus(self, userId="$None$", status="$None$", _assert=True, _all_is_None=False,  **kwargs):
        """
            url=/common/user4C/editStatus
                params: status : number : 是否启用0：禁用 1：启用
                params: headers : 请求头
        """
        userId = self.get_value_choice(userId, list_or_dict=None, key=None, _all_is_None=_all_is_None)
        status = self.get_value_choice(status, list_or_dict=None, key=None, _all_is_None=_all_is_None)

        _kwargs = self.get_kwargs(locals())
        self.res = apis_common_user4c.common_user4c_editstatus(**_kwargs)

        self.assert_common_user4c_editstatus(_assert, **_kwargs)
        self.set_value(_kwargs)


    @allure.step(title="导出用户审核列表-Y")
    def common_user4c_auditexport(self, ownerFlag="$None$", userLabel="$None$", userIds="$None$", phone="$None$", userType="$None$", downloadType="$None$", registerType="$None$", nickName="$None$", userId="$None$", _assert=True,  **kwargs):
        """
            url=/common/user4C/auditExport
                params: phone :  : 手机号
                params: nickName :  : 昵称
                params: ownerFlag :  : 是否车主认证1：是0：否
                params: userLabel :  : 用户标签
                params: registerType :  : 用户来源
                params: userType :  : 用户类型
                params: downloadType :  : 下载类型1：根据搜索条件导出2：多选导出
                params: headers : 请求头
        """
        ownerFlag = self.get_list_choice(ownerFlag, list_or_dict=None, key="ownerFlag")
        userLabel = self.get_list_choice(userLabel, list_or_dict=None, key="userLabel")
        userIds = self.get_list_choice(userIds, list_or_dict=None, key="userIds")
        phone = self.get_list_choice(phone, list_or_dict=None, key="phone")
        userType = self.get_list_choice(userType, list_or_dict=None, key="userType")
        downloadType = self.get_list_choice(downloadType, list_or_dict=None, key="downloadType")
        registerType = self.get_list_choice(registerType, list_or_dict=None, key="registerType")
        nickName = self.get_list_choice(nickName, list_or_dict=None, key="nickName")
        userId = self.get_list_choice(userId, list_or_dict=None, key="userId")

        _kwargs = self.get_kwargs(locals())
        self.res = apis_common_user4c.common_user4c_auditexport(**_kwargs)

        self.assert_common_user4c_auditexport(_assert, **_kwargs)
        self.set_output_value(_kwargs)
        self.set_value(_kwargs)


    @allure.step(title="根据id查询用户身份-Y")
    def common_user4c_identity(self, userId="$None$", _assert=True,  **kwargs):
        """
            url=/common/user4C/identity
                params: headers : 请求头
        """
        userId = self.get_list_choice(userId, list_or_dict=None, key="userId")

        _kwargs = self.get_kwargs(locals())
        self.res = apis_common_user4c.common_user4c_identity(**_kwargs)

        self.assert_common_user4c_identity(_assert, **_kwargs)
        self.set_output_value(_kwargs)
        self.set_value(_kwargs)


    @allure.step(title="更新审核状态-Y")
    def common_user4c_updateaudit(self, userId="$None$", auditType="$None$", _assert=True, _all_is_None=False,  **kwargs):
        """
            url=/common/user4C/updateAudit
                params: auditType : integer : 认证类型（1：注销审核单据，2：车主认证审核单据）
                params: headers : 请求头
        """
        userId = self.get_value_choice(userId, list_or_dict=None, key=None, _all_is_None=_all_is_None)
        auditType = self.get_value_choice(auditType, list_or_dict=None, key=None, _all_is_None=_all_is_None)

        _kwargs = self.get_kwargs(locals())
        self.res = apis_common_user4c.common_user4c_updateaudit(**_kwargs)

        self.assert_common_user4c_updateaudit(_assert, **_kwargs)
        self.set_value(_kwargs)


    @allure.step(title="根据用户审核状态搜索列表-Y")
    def common_user4c_auditlist(self, pageSize="$None$", mobile="$None$", registerType="$None$", checkStatus="$None$", nickName="$None$", userId="$None$", userName="$None$", pageNum=1, _assert=True,  **kwargs):
        """
            url=/common/user4C/auditList
                params: mobile :  : 手机号
                params: nickName :  : 用户昵称
                params: userName :  : 用户实名姓名
                params: registerType :  : 用户来源
                params: pageSize :  : 每页数量
                params: pageNum :  : 当前页数
                params: checkStatus :  : 状态 0-正常 1-审核中 2-通过3-审核不通过
                params: headers : 请求头
        """
        pageSize = self.get_list_choice(pageSize, list_or_dict=None, key="pageSize")
        mobile = self.get_list_choice(mobile, list_or_dict=None, key="mobile")
        registerType = self.get_list_choice(registerType, list_or_dict=None, key="registerType")
        checkStatus = self.get_list_choice(checkStatus, list_or_dict=None, key="checkStatus")
        nickName = self.get_list_choice(nickName, list_or_dict=None, key="nickName")
        userId = self.get_list_choice(userId, list_or_dict=None, key="userId")
        userName = self.get_list_choice(userName, list_or_dict=None, key="userName")

        _kwargs = self.get_kwargs(locals())
        self.res = apis_common_user4c.common_user4c_auditlist(**_kwargs)

        self.assert_common_user4c_auditlist(_assert, **_kwargs)
        self.set_output_value(_kwargs)
        self.set_value(_kwargs)


    @allure.step(title="用户信息积分详情-？历史接口")
    def common_user4c_getuserpoints(self, userId="$None$", _assert=True,  **kwargs):
        """
            url=/common/user4C/getUserPoints
                params: headers : 请求头
        """
        userId = self.get_list_choice(userId, list_or_dict=None, key="userId")

        _kwargs = self.get_kwargs(locals())
        self.res = apis_common_user4c.common_user4c_getuserpoints(**_kwargs)

        self.assert_common_user4c_getuserpoints(_assert, **_kwargs)
        self.set_output_value(_kwargs)
        self.set_value(_kwargs)


