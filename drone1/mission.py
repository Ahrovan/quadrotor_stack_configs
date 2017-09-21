import executive_engine_api as api
import time

QR_LOCATION = [11.79, 4.3]

def runMission():
    api.activateBehavior('SELF_LOCALIZE_BY_VISUAL_MARKER')

    print("Taking off..")
    result = api.executeBehavior('TAKE_OFF')
    print("TAKE_OFF ended with status %s" % result)

    goThroughWindow()

    goThroughPoles()

    goThroughVegetation()

    lookForQR()

    api.inhibitBehavior('SELF_LOCALIZE_BY_VISUAL_MARKER')
    api.executeBehavior('LAND')

def goThroughWindow():
    point_a = [2, 4.8, 1.4]
    print("Going to %s ..." % point_a)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_a)
    print("GO_TO_POINT ended with status %s" % result)

    point_a_2 = [5, 4.8, 1.4]
    print("Going to %s ..." % point_a_2)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_a_2)
    print("GO_TO_POINT ended with status %s" % result)

def goThroughPoles():
    point_b = [6.18, 6.39, 1.4]
    print("Going to %s ..." % point_b)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_b)
    print("GO_TO_POINT ended with status %s" % result)

    point_c = [8.21, 4.74, 1.4]
    print("Going to %s ..." % point_c)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_c)
    print("GO_TO_POINT ended with status %s" % result)

    point_c = [9.85, 7.8, 1.4]
    print("Going to %s ..." % point_c)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_c)
    print("GO_TO_POINT ended with status %s" % result)

    point_c = [10.91, 10.47, 0.5]
    print("Going to %s ..." % point_c)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_c)
    print("GO_TO_POINT ended with status %s" % result)

def goThroughVegetation():
    point_e = [12, 9.48, 0.5]
    print("Going to %s ..." % point_e)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_e)
    print("GO_TO_POINT ended with status %s" % result)

    point_e = [13.19, 7.6, 0.5]
    print("Going to %s ..." % point_e)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_e)
    print("GO_TO_POINT ended with status %s" % result)

    point_e = [14, 7.1, 0.5]
    print("Going to %s ..." % point_e)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_e)
    print("GO_TO_POINT ended with status %s" % result)

    print("Rotating...")
    result = api.executeBehavior('ROTATE', angle=180)
    print("ROTATE ended with status %s" % result)

    point_f = [QR_LOCATION[0]+1, QR_LOCATION[1]+1, 0.5]
    print("Going to %s ..." % point_f)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_f)
    print("GO_TO_POINT ended with status %s" % result)


def lookForQR():
    point_f = [QR_LOCATION[0], QR_LOCATION[1], 1.25]
    print("Going to %s ..." % point_f)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_f)
    print("GO_TO_POINT ended with status %s" % result)

    print("Looking for QR...")
    result = api.executeBehavior('RECOGNIZE_QR')
    if result != 'GOAL_ACHIEVED':
        print("QR not found")
        api.executeBehavior('GO_TO_POINT', coordinates=[QR_LOCATION[0], QR_LOCATION[1], 2])
    else:
        print("QR found!")
    result = api.executeBehavior('RECOGNIZE_QR')
    print("QR found!" if result == "GOAL_ACHIEVED" else "QR not found")
