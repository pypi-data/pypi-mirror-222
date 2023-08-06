from service.app_a.funs.radarpoints.funs_radarpoints_adjustpoints import FunsRadarpointsAdjustpoints
from service.app_a.funs.radarpoints.funs_radarpoints_pointsconfig import FunsRadarpointsPointsconfig
from service.app_a.funs.radarpoints.funs_radarpoints_pointstask import FunsRadarpointsPointstask
from service.app_a.funs.radarpoints.funs_radarpoints_summarystatistics import FunsRadarpointsSummarystatistics
from service.app_a.funs.radarpoints.funs_radarpoints_userpoints import FunsRadarpointsUserpoints


class FunsRadarpoints(FunsRadarpointsAdjustpoints, FunsRadarpointsPointsconfig, FunsRadarpointsPointstask, FunsRadarpointsSummarystatistics, FunsRadarpointsUserpoints):
    pass

