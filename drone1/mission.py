import executive_engine_api as api
import time

def runMission():
    api.activateBehavior('SELF_LOCALIZE_BY_VISUAL_MARKER')

    print("Taking off..")
    result = api.executeBehavior('TAKE_OFF')
    print("TAKE_OFF ended with status %s" % result)

    #goThroughWindow()
    #goThroughPoles()
    goThroughVegetation()
    lookForQR()

    api.inhibitBehavior('SELF_LOCALIZE_BY_VISUAL_MARKER')
    api.executeBehavior('LAND')

def goThroughWindow():
    point_a = [0, 0.6, 1.2]
    print("Going to %s ..." % point_a)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_a)
    print("GO_TO_POINT ended with status %s" % result)

    point_b = [3, 0.6, 1.2]
    print("Going to %s ..." % point_b)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_b)
    print("GO_TO_POINT ended with status %s" % result)

def goThroughPoles():
    point_c = [8, 0, 1.2]
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

    point_d = [10.5, 0.5, 1.25]
    print("Going to %s ..." % point_d)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_d)
    print("GO_TO_POINT ended with status %s" % result)

    point_e = [13.5, 0.5, 1.25]
    print("Going to %s ..." % point_e)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_e)
    print("GO_TO_POINT ended with status %s" % result)

    point_f = [12.5, -2.5, 1.25]
    print("Going to %s ..." % point_f)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_f)
    print("GO_TO_POINT ended with status %s" % result)

def lookForQR():
    print("Looking for QR...")
    result = api.executeBehavior('RECOGNIZE_QR')
    if result != 'GOAL_ACHIEVED':
        print("QR not found")
        api.executeBehavior('GO_TO_POINT', coordinates=[13, -2.5, 1.5])
    else:
        print("QR found!")
    result = api.executeBehavior('RECOGNIZE_QR')
    print("QR found!" if result == "GOAL_ACHIEVED" else "QR not found")
