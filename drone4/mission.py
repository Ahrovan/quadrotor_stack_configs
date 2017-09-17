import executive_engine_api as api
import time

LAND_POINT=[0, 0, 0]

def runMission():
     api.activateBehavior('SELF_LOCALIZE_BY_VISUAL_MARKER')
    # api.activateBehavior('SELF_LOCALIZE_BY_ODOMETRY')

    # time.sleep(120)

    print("Taking off..")
    result = api.executeBehavior('TAKE_OFF')
    print("TAKE_OFF ended with status %s" % result)

    # Pose: [0, 0, 0.47, 0]
    goThroughWindow()

    # Pose: [3.5, 0.3, 0, 0]
    goThroughPoles()

    goToLandPoint()

    dropObject()

    goAway()
    

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


def goToLandPoint():
    print("Rotating...")
    result = api.executeBehavior('ROTATE', angle=180)
    print("ROTATE ended with status %s" % result)

    point = [7.8, 4, 1.2]
    print("Going to %s ..." % point)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point)
    print("GO_TO_POINT ended with status %s" % result)

    print("Rotating...")
    result = api.executeBehavior('ROTATE', angle=135)
    print("ROTATE ended with status %s" % result)

    print("Going to %s ..." % LAND_POINT)
    result = api.executeBehavior('GO_TO_POINT', coordinates=LAND_POINT)
    print("GO_TO_POINT ended with status %s" % result)

    print("Rotating...")
    result = api.executeBehavior('ROTATE', angle=135)
    print("ROTATE ended with status %s" % result)


def dropObject():
    api.executeBehavior('LAND_ON_STATIC_PLATFORM')
    time.sleep(5)

def goAway():
    api.executeBehavior('TAKE_OFF')
    api.executeBehavior('GO_TO_POINT', coordinates=[8, -4.2, 1.3])

