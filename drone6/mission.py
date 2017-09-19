import executive_engine_api as api
import time

QR_LOCATION = [13.1, 1]

def runMission():
    api.activateBehavior('SELF_LOCALIZE_BY_VISUAL_MARKER')
    # api.activateBehavior('SELF_LOCALIZE_BY_ODOMETRY')

    print("Taking off..")
    result = api.executeBehavior('TAKE_OFF')
    print("TAKE_OFF ended with status %s" % result)

    point_a = [5.6, 11.51, 1.4]
    print("Going to %s ..." % point_a)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_a)
    print("GO_TO_POINT ended with status %s" % result)

    api.inhibitBehavior('SELF_LOCALIZE_BY_VISUAL_MARKER')
    # api.inhibitBehavior('SELF_LOCALIZE_BY_ODOMETRY')
    api.executeBehavior('LAND')
