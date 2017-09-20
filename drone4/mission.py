import executive_engine_api as api
import time

LAND_POINT=[12.5, 2.27, 1.6]

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
    point_a = [2, 4.8, 1.4]
    print("Going to %s ..." % point_a)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_a)
    print("GO_TO_POINT ended with status %s" % result)

    point_a_2 = [5, 4.8, 1.4]
    print("Going to %s ..." % point_a_2)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_a_2)
    print("GO_TO_POINT ended with status %s" % result)

def goThroughPoles():
    point_b = [6.8, 6.36, 1.4]
    print("Going to %s ..." % point_b)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_b)
    print("GO_TO_POINT ended with status %s" % result)

    point_c = [9.7, 6.36, 1.4]
    print("Going to %s ..." % point_c)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_c)
    print("GO_TO_POINT ended with status %s" % result)

    point_c = [9.7, 3, 1.4]
    print("Going to %s ..." % point_c)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_c)
    print("GO_TO_POINT ended with status %s" % result)



def goToLandPoint():
    print("Going to %s ..." % LAND_POINT)
    result = api.executeBehavior('GO_TO_POINT', coordinates=LAND_POINT)
    print("GO_TO_POINT ended with status %s" % result)


def dropObject():
    api.executeBehavior('LAND_ON_STATIC_PLATFORM')
    time.sleep(5)

def goAway():
    api.executeBehavior('TAKE_OFF')
    api.executeBehavior('GO_TO_POINT', relative_coordinates=[-2, 0, 0])
