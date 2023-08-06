import allure

from service.app_a.asserts.radarpoints.asserts_radarpoints_userpoints import AssertsRadarpointsUserpoints
from service.app_a.apis.radarpoints import apis_radarpoints_userpoints
from service.app_a.funs.radarpoints.userpoints.funs_radarpoints_userpoints_exchangeinfo import FunsRadarpointsUserpointsExchangeinfo
from service.app_a.funs.radarpoints.userpoints.funs_radarpoints_userpoints_pointsinfo import FunsRadarpointsUserpointsPointsinfo


class FunsRadarpointsUserpoints(AssertsRadarpointsUserpoints, FunsRadarpointsUserpointsExchangeinfo, FunsRadarpointsUserpointsPointsinfo):
    @allure.step(title="用户积分 - 分页查询")
    def radarpoints_userpoints_pagelist(self, size=10, conversionFrequencyLeast="$None$", registrationTimeBegin="$None$", physicalIntegralLeast="$None$", cumulativeConsumptionLeast="$None$", current=1, freezeQtyMost="$None$", cumulativeConsumptionMost="$None$", conversionFrequencyMost="$None$", nickName="$None$", userId="$None$", physicalIntegralMost="$None$", registrationTimeEnd="$None$", cumulativeAcquisitionLeast="$None$", cumulativeAcquisitionMost="$None$", freezeQtyLeast="$None$", mobile="$None$", _assert=True,  **kwargs):
        """
            url=/radarpoints/userPoints/pageList
                params: mobile :  : 用户手机号
                params: nickName :  : 用户昵称
                params: registrationTimeBegin :  : 注册时间 - 开始
                params: registrationTimeEnd :  : 注册时间 - 结束
                params: physicalIntegralLeast :  : 持有积分 - 最少
                params: physicalIntegralMost :  : 持有积分 - 最多
                params: cumulativeAcquisitionLeast :  : 累计获取 - 最少
                params: cumulativeAcquisitionMost :  : 累计获取 - 最多
                params: cumulativeConsumptionLeast :  : 累计消耗 - 最少
                params: cumulativeConsumptionMost :  : 累计消耗 - 最多
                params: conversionFrequencyLeast :  : 兑换次数 - 最少
                params: conversionFrequencyMost :  : 兑换次数 - 最多
                params: freezeQtyLeast :  : 冻结积分 - 最少
                params: freezeQtyMost :  : 冻结积分 - 最多
                params: current :  : 页码
                params: size :  : 每页大小
                params: headers : 请求头
        """
        conversionFrequencyLeast = self.get_list_choice(conversionFrequencyLeast, list_or_dict=None, key="conversionFrequencyLeast")
        registrationTimeBegin = self.get_list_choice(registrationTimeBegin, list_or_dict=None, key="registrationTimeBegin")
        physicalIntegralLeast = self.get_list_choice(physicalIntegralLeast, list_or_dict=None, key="physicalIntegralLeast")
        cumulativeConsumptionLeast = self.get_list_choice(cumulativeConsumptionLeast, list_or_dict=None, key="cumulativeConsumptionLeast")
        freezeQtyMost = self.get_list_choice(freezeQtyMost, list_or_dict=None, key="freezeQtyMost")
        cumulativeConsumptionMost = self.get_list_choice(cumulativeConsumptionMost, list_or_dict=None, key="cumulativeConsumptionMost")
        conversionFrequencyMost = self.get_list_choice(conversionFrequencyMost, list_or_dict=None, key="conversionFrequencyMost")
        nickName = self.get_list_choice(nickName, list_or_dict=None, key="nickName")
        userId = self.get_list_choice(userId, list_or_dict=None, key="userId")
        physicalIntegralMost = self.get_list_choice(physicalIntegralMost, list_or_dict=None, key="physicalIntegralMost")
        registrationTimeEnd = self.get_list_choice(registrationTimeEnd, list_or_dict=None, key="registrationTimeEnd")
        cumulativeAcquisitionLeast = self.get_list_choice(cumulativeAcquisitionLeast, list_or_dict=None, key="cumulativeAcquisitionLeast")
        cumulativeAcquisitionMost = self.get_list_choice(cumulativeAcquisitionMost, list_or_dict=None, key="cumulativeAcquisitionMost")
        freezeQtyLeast = self.get_list_choice(freezeQtyLeast, list_or_dict=None, key="freezeQtyLeast")
        mobile = self.get_list_choice(mobile, list_or_dict=None, key="mobile")

        _kwargs = self.get_kwargs(locals())
        self.res = apis_radarpoints_userpoints.radarpoints_userpoints_pagelist(**_kwargs)

        self.assert_radarpoints_userpoints_pagelist(_assert, **_kwargs)
        self.set_output_value(_kwargs)
        self.set_value(_kwargs)


    @allure.step(title="用户积分 - 导出excel")
    def radarpoints_userpoints_export(self, conversionFrequencyLeast="$None$", registrationTimeBegin="$None$", physicalIntegralLeast="$None$", cumulativeConsumptionLeast="$None$", pageSize="$None$", cumulativeConsumptionMost="$None$", conversionFrequencyMost="$None$", currentPage="$None$", nickName="$None$", cumulativeAcquisitionLeast="$None$", physicalIntegralMost="$None$", registrationTimeEnd="$None$", cumulativeAcquisitionMost="$None$", _assert=True,  **kwargs):
        """
            url=/radarpoints/userPoints/export
                params: nickName :  : 用户昵称
                params: registrationTimeBegin :  : 注册时间 - 开始
                params: registrationTimeEnd :  : 注册时间 - 结束
                params: physicalIntegralLeast :  : 持有积分 - 最少
                params: physicalIntegralMost :  : 持有积分 - 最多
                params: cumulativeAcquisitionLeast :  : 累计获取 - 最少
                params: cumulativeAcquisitionMost :  : 累计获取 - 最多
                params: cumulativeConsumptionLeast :  : 累计消耗 - 最少
                params: cumulativeConsumptionMost :  : 累计消耗 - 最多
                params: conversionFrequencyLeast :  : 兑换次数 - 最少
                params: conversionFrequencyMost :  : 兑换次数 - 最多
                params: currentPage :  : 当前页码
                params: pageSize :  : 每页大小
                params: headers : 请求头
        """
        conversionFrequencyLeast = self.get_list_choice(conversionFrequencyLeast, list_or_dict=None, key="conversionFrequencyLeast")
        registrationTimeBegin = self.get_list_choice(registrationTimeBegin, list_or_dict=None, key="registrationTimeBegin")
        physicalIntegralLeast = self.get_list_choice(physicalIntegralLeast, list_or_dict=None, key="physicalIntegralLeast")
        cumulativeConsumptionLeast = self.get_list_choice(cumulativeConsumptionLeast, list_or_dict=None, key="cumulativeConsumptionLeast")
        pageSize = self.get_list_choice(pageSize, list_or_dict=None, key="pageSize")
        cumulativeConsumptionMost = self.get_list_choice(cumulativeConsumptionMost, list_or_dict=None, key="cumulativeConsumptionMost")
        conversionFrequencyMost = self.get_list_choice(conversionFrequencyMost, list_or_dict=None, key="conversionFrequencyMost")
        currentPage = self.get_list_choice(currentPage, list_or_dict=None, key="currentPage")
        nickName = self.get_list_choice(nickName, list_or_dict=None, key="nickName")
        cumulativeAcquisitionLeast = self.get_list_choice(cumulativeAcquisitionLeast, list_or_dict=None, key="cumulativeAcquisitionLeast")
        physicalIntegralMost = self.get_list_choice(physicalIntegralMost, list_or_dict=None, key="physicalIntegralMost")
        registrationTimeEnd = self.get_list_choice(registrationTimeEnd, list_or_dict=None, key="registrationTimeEnd")
        cumulativeAcquisitionMost = self.get_list_choice(cumulativeAcquisitionMost, list_or_dict=None, key="cumulativeAcquisitionMost")

        _kwargs = self.get_kwargs(locals())
        self.res = apis_radarpoints_userpoints.radarpoints_userpoints_export(**_kwargs)

        self.assert_radarpoints_userpoints_export(_assert, **_kwargs)
        self.set_output_value(_kwargs)
        self.set_value(_kwargs)


