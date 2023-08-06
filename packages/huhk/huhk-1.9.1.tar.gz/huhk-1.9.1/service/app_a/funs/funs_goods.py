from service.app_a.funs.goods.funs_goods_area import FunsGoodsArea
from service.app_a.funs.goods.funs_goods_carmodel import FunsGoodsCarmodel
from service.app_a.funs.goods.funs_goods_configure import FunsGoodsConfigure
from service.app_a.funs.goods.funs_goods_ordermain import FunsGoodsOrdermain
from service.app_a.funs.goods.funs_goods_testdrive import FunsGoodsTestdrive


class FunsGoods(FunsGoodsArea, FunsGoodsCarmodel, FunsGoodsConfigure, FunsGoodsOrdermain, FunsGoodsTestdrive):
    pass

