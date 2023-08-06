import allure

from service.app_a.asserts.order.asserts_order_testdrive import AssertsOrderTestdrive
from service.app_a.apis.order import apis_order_testdrive


class FunsOrderTestdrive(AssertsOrderTestdrive):
    @allure.step(title="导出试驾表单-Y")
    def order_testdrive_exportlist(self, phoneNumber="$None$", createByName="$None$", channel="$None$", shopName="$None$", endTime="$None$", startTime="$None$", createTime="$None$", id="$None$", _assert=True,  **kwargs):
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
        phoneNumber = self.get_list_choice(phoneNumber, list_or_dict=None, key="phoneNumber")
        createByName = self.get_list_choice(createByName, list_or_dict=None, key="createByName")
        channel = self.get_list_choice(channel, list_or_dict=None, key="channel")
        shopName = self.get_list_choice(shopName, list_or_dict=None, key="shopName")
        endTime = self.get_list_choice(endTime, list_or_dict=None, key="endTime")
        startTime = self.get_list_choice(startTime, list_or_dict=None, key="startTime")
        createTime = self.get_list_choice(createTime, list_or_dict=None, key="createTime")
        id = self.get_list_choice(id, list_or_dict=None, key="id")

        _kwargs = self.get_kwargs(locals())
        self.res = apis_order_testdrive.order_testdrive_exportlist(**_kwargs)

        self.assert_order_testdrive_exportlist(_assert, **_kwargs)
        self.set_output_value(_kwargs)
        self.set_value(_kwargs)


    @allure.step(title="用户中心-预约信息")
    def order_testdrive_userlist(self, modelId="$None$", createBy="$None$", size=10, current=1, _assert=True,  **kwargs):
        """
            url=/order/testDrive/userList
                params: current :  : 当前页数
                params: size :  : 每页数据数
                params: createBy :  :
                params: modelId :  :
                params: headers : 请求头
        """
        modelId = self.get_list_choice(modelId, list_or_dict=None, key="modelId")
        createBy = self.get_list_choice(createBy, list_or_dict=None, key="createBy")

        _kwargs = self.get_kwargs(locals())
        self.res = apis_order_testdrive.order_testdrive_userlist(**_kwargs)

        self.assert_order_testdrive_userlist(_assert, **_kwargs)
        self.set_output_value(_kwargs)
        self.set_value(_kwargs)


