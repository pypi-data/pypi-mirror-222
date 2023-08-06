import allure

from service.app_a import http_requester
from huhk.unit_request import get_url


@allure.step(title="调接口：/order/rightsOrder/receive/update")
def order_rightsorder_receive_update(refundBillNo=None, receiveDate=None, payDate=None, rightsId=None, payBillNo=None, updateTime=None, updateId=None, payAmount=None, useStatus=None, userId=None, mobile=None, refundDate=None, createTime=None, orderMainId=None, createBy=None, rightsOrderId=None, rightsType=None, rightsName=None, headers=None, **kwargs):
    """
    权益-编辑权益订单-Y
    up_time=1675660709

    params: rightsOrderId : string : 
    params: rightsId : string : 
    params: rightsType : string : 
    params: rightsName : string : 
    params: orderMainId : string : 
    params: userId : string : 
    params: mobile : string : 
    params: payAmount : string : 
    params: useStatus : string : 
    params: receiveDate : string : 
    params: payDate : string : 
    params: refundDate : string : 
    params: payBillNo : string : 
    params: refundBillNo : string : 
    params: createTime : string : 
    params: createBy : string : 
    params: updateTime : string : 
    params: updateId : string : 
    params: headers : 请求头
    ====================返回======================
    params: code : integer : 0失败 1成功
    params: msg : string : 
    params: field_203 : string : 
    """
    _method = "POST"
    _url = "/order/rightsOrder/receive/update"

    _headers = {
        "Content-Type": "application/json",
    }
    _headers.update({"headers": headers})

    _data = {
        "rightsOrderId": rightsOrderId,
        "rightsId": rightsId,
        "rightsType": rightsType,
        "rightsName": rightsName,
        "orderMainId": orderMainId,
        "userId": userId,
        "mobile": mobile,
        "payAmount": payAmount,
        "useStatus": useStatus,
        "receiveDate": receiveDate,
        "payDate": payDate,
        "refundDate": refundDate,
        "payBillNo": payBillNo,
        "refundBillNo": refundBillNo,
        "createTime": createTime,
        "createBy": createBy,
        "updateTime": updateTime,
        "updateId": updateId,
    }

    _params = {
    }

    return http_requester(_method, _url, params=_params, data=_data, headers=_headers, **kwargs)


