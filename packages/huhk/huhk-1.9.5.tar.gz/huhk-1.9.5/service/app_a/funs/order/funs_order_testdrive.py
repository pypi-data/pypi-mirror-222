import allure

from service.app_a.asserts.order.asserts_order_testdrive import AssertsOrderTestdrive
from service.app_a.apis.order import apis_order_testdrive


class FunsOrderTestdrive(AssertsOrderTestdrive):
    @allure.step(title="导出试驾表单-Y")
    def order_testdrive_exportlist(self, startTime="$None$", endTime="$None$", id="$None$", createByName="$None$", shopName="$None$", phoneNumber="$None$", createTime="$None$", channel="$None$", _assert=True,  **kwargs):
        """
            url=/order/testDrive/exportList
                params: phoneNumber :  : 手机号
                params: createByName :  :
                params: id :  : 主键
                params: channel :  : 渠道(1:移动应用 2:小程序 3:官方网站)
                params: startTime :  :
                params: endTime :  :
                params: shopName :  : 门店名称
                params: createTime :  : 创建时间
                params: headers : 请求头
        """
        startTime = self.get_list_choice(startTime, list_or_dict=None, key="startTime")
        endTime = self.get_list_choice(endTime, list_or_dict=None, key="endTime")
        id = self.get_list_choice(id, list_or_dict=None, key="id")
        createByName = self.get_list_choice(createByName, list_or_dict=None, key="createByName")
        shopName = self.get_list_choice(shopName, list_or_dict=None, key="shopName")
        phoneNumber = self.get_list_choice(phoneNumber, list_or_dict=None, key="phoneNumber")
        createTime = self.get_list_choice(createTime, list_or_dict=None, key="createTime")
        channel = self.get_list_choice(channel, list_or_dict=None, key="channel")

        _kwargs = self.get_kwargs(locals())
        self.res = apis_order_testdrive.order_testdrive_exportlist(**_kwargs)

        self.assert_order_testdrive_exportlist(_assert, **_kwargs)
        self.set_output_value(_kwargs)
        self.set_value(_kwargs)


    @allure.step(title="用户中心-预约信息")
    def order_testdrive_userlist(self, createBy="$None$", modelId="$None$", size=10, current=1, _assert=True,  **kwargs):
        """
            url=/order/testDrive/userList
                params: current :  : 当前页数
                params: size :  : 每页数据数
                params: createBy :  :
                params: modelId :  :
                params: headers : 请求头
        """
        createBy = self.get_list_choice(createBy, list_or_dict=None, key="createBy")
        modelId = self.get_list_choice(modelId, list_or_dict=None, key="modelId")

        _kwargs = self.get_kwargs(locals())
        self.res = apis_order_testdrive.order_testdrive_userlist(**_kwargs)

        self.assert_order_testdrive_userlist(_assert, **_kwargs)
        self.set_output_value(_kwargs)
        self.set_value(_kwargs)


