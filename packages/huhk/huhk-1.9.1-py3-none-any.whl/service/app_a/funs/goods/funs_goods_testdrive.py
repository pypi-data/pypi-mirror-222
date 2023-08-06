import allure

from service.app_a.asserts.goods.asserts_goods_testdrive import AssertsGoodsTestdrive
from service.app_a.apis.goods import apis_goods_testdrive


class FunsGoodsTestdrive(AssertsGoodsTestdrive):
    @allure.step(title="试驾列表文件导出接口-Y")
    def goods_testdrive_driveexports(self, userName="$None$", testDriveIdStr="$None$", shopName="$None$", startTime="$None$", endTime="$None$", exportType="$None$", mobile="$None$", channel="$None$", _assert=True,  **kwargs):
        """
            url=/goods/testDrive/driveExports
                params: mobile :  : 手机号
                params: userName :  : 用户名
                params: shopName :  : 店名
                params: channel :  : 渠道
                params: startTime :  : 开始时间
                params: endTime :  : 结束时间
                params: exportType :  : 导出类型
                params: testDriveIdStr :  : 订单集合字符串
                params: headers : 请求头
        """
        userName = self.get_list_choice(userName, list_or_dict=None, key="userName")
        testDriveIdStr = self.get_list_choice(testDriveIdStr, list_or_dict=None, key="testDriveIdStr")
        shopName = self.get_list_choice(shopName, list_or_dict=None, key="shopName")
        startTime = self.get_list_choice(startTime, list_or_dict=None, key="startTime")
        endTime = self.get_list_choice(endTime, list_or_dict=None, key="endTime")
        exportType = self.get_list_choice(exportType, list_or_dict=None, key="exportType")
        mobile = self.get_list_choice(mobile, list_or_dict=None, key="mobile")
        channel = self.get_list_choice(channel, list_or_dict=None, key="channel")

        _kwargs = self.get_kwargs(locals())
        self.res = apis_goods_testdrive.goods_testdrive_driveexports(**_kwargs)

        self.assert_goods_testdrive_driveexports(_assert, **_kwargs)
        self.set_output_value(_kwargs)
        self.set_value(_kwargs)


    @allure.step(title="试驾查询接口-Y")
    def goods_testdrive_page(self, pageSize="$None$", userName="$None$", shopName="$None$", startTime="$None$", endTime="$None$", pageNum=1, mobile="$None$", channel="$None$", _assert=True,  **kwargs):
        """
            url=/goods/testDrive/page
                params: mobile :  : 手机号
                params: userName :  : 客户名
                params: shopName :  : 店名
                params: channel :  : 渠道
                params: startTime :  : 开始时间
                params: endTime :  : 结束时间
                params: pageNum :  : 当前页数
                params: pageSize :  : 每页数据数
                params: headers : 请求头
        """
        pageSize = self.get_list_choice(pageSize, list_or_dict=None, key="pageSize")
        userName = self.get_list_choice(userName, list_or_dict=None, key="userName")
        shopName = self.get_list_choice(shopName, list_or_dict=None, key="shopName")
        startTime = self.get_list_choice(startTime, list_or_dict=None, key="startTime")
        endTime = self.get_list_choice(endTime, list_or_dict=None, key="endTime")
        mobile = self.get_list_choice(mobile, list_or_dict=None, key="mobile")
        channel = self.get_list_choice(channel, list_or_dict=None, key="channel")

        _kwargs = self.get_kwargs(locals())
        self.res = apis_goods_testdrive.goods_testdrive_page(**_kwargs)

        self.assert_goods_testdrive_page(_assert, **_kwargs)
        self.set_output_value(_kwargs)
        self.set_value(_kwargs)


