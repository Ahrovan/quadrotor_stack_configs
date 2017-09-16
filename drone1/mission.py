import executive_engine_api as api
import time

QR_LOCATION = [13.1, 1]

def runMission():
    api.activateBehavior('SELF_LOCALIZE_BY_VISUAL_MARKER')
    # api.activateBehavior('SELF_LOCALIZE_BY_ODOMETRY')

    # time.sleep(120)

    print("Taking off..")
    result = api.executeBehavior('TAKE_OFF')
    print("TAKE_OFF ended with status %s" % result)

    # Pose: [0, 0, 0.47, 0]
    # goThroughWindow()

    # Pose: [3.5, 0.3, 0, 0]
    goThroughPoles()

    # Pose: [7.7, -0.5, 0]
    goThroughVegetation()

    # Pose: [12.2, 0, 0, 180]
    lookForQR()

    api.inhibitBehavior('SELF_LOCALIZE_BY_VISUAL_MARKER')
    # api.inhibitBehavior('SELF_LOCALIZE_BY_ODOMETRY')
    api.executeBehavior('LAND')

def goThroughWindow():
    point_a = [-0.5, 0, 1.2]
    point_a_2 = [-0.5, 4.75, 1.2]
    print("Going to %s ..." % point_a)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_a)
    print("GO_TO_POINT ended with status %s" % result)
    print("Going to %s ..." % point_a_2)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_a_2)
    print("GO_TO_POINT ended with status %s" % result)

    point_b = [3.5, 4.75, 1.2]
    print("Going to %s ..." % point_b)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_b)
    print("GO_TO_POINT ended with status %s" % result)

def goThroughPoles():
    point_b = [3.8, 5.3, 1.2]
    print("Going to %s ..." % point_b)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_b)
    print("GO_TO_POINT ended with status %s" % result)

    point_c = [7.8, 4, 1.2]
    print("Going to %s ..." % point_c)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_c)
    print("GO_TO_POINT ended with status %s" % result)

def goThroughVegetation():
    # print("Rotating...")
    # result = api.executeBehavior('ROTATE', angle=45)
    # print("ROTATE ended with status %s" % result)
    # time.sleep(1)
    # print("Rotating...")
    # result = api.executeBehavior('ROTATE', angle=90)
    # print("ROTATE ended with status %s" % result)
    # time.sleep(1)
    # print("Rotating...")
    # result = api.executeBehavior('ROTATE', angle=135)
    # print("ROTATE ended with status %s" % result)
    # time.sleep(1)
    # print("Rotating...")
    # result = api.executeBehavior('ROTATE', angle=180)
    # print("ROTATE ended with status %s" % result)

    # point_d = [10.5, 0.5, 1.25]
    # print("Going to %s ..." % point_d)
    # result = api.executeBehavior('GO_TO_POINT', coordinates=point_d)
    # print("GO_TO_POINT ended with status %s" % result)

    point_e = [12.5, 4.8, 1.25]
    print("Going to %s ..." % point_e)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_e)
    print("GO_TO_POINT ended with status %s" % result)

    # print("Rotating...")
    # result = api.executeBehavior('ROTATE', angle=180)
    # print("ROTATE ended with status %s" % result)


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
