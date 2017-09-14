import executive_engine_api as api

def runMission():
    api.activateBehavior('SELF_LOCALIZE_BY_ODOMETRY')

    print("Taking off..")
    result = api.executeBehavior('TAKE_OFF')
    print("TAKE_OFF ended with status %s" % result)

    api.activateBehavior('SELF_LOCALIZE_BY_VISUAL_MARKER')

    point_a = [0, 0.6, 1.2]
    print("Going to %s ..." % point_a)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_a)
    print("GO_TO_POINT ended with status %s" % result)

    point_b = [3, 0.6, 1.2]
    print("Going to %s ..." % point_b)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_b)
    print("GO_TO_POINT ended with status %s" % result)

    point_c = [8, 0, 1.2]
    print("Going to %s ..." % point_c)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_c)
    print("GO_TO_POINT ended with status %s" % result)

    point_d = [12.5, -2.5, 1.2]
    print("Going to %s ..." % point_d)
    result = api.executeBehavior('GO_TO_POINT', coordinates=point_d)
    print("GO_TO_POINT ended with status %s" % result)

    # print("Turning around...")
    # result = api.executeBehavior('ROTATE', angle=180)
    # print("GO_TO_POINT ended with status %s" % result)
    #
    # print("Goint to QR point")
    # result = api.executeBehavior('GO_TO_POINT', coordinates=[8, -3, 1.2])
    # print("GO_TO_POINT ended with status %s" % result)
    #
    print("Looking for QR...")
    result = api.executeBehavior('RECOGNIZE_QR')
    if result != 'GOAL_ACHIEVED':
        print("QR not found")
        api.executeBehavior('GO_TO_POINT', coordinates=[13, -2.5, 1.5])
    else:
        print("QR found!")
    result = api.executeBehavior('RECOGNIZE_QR')
    print("QR found!" if result == "GOAL_ACHIEVED" else "QR not found")

    api.inhibitBehavior('SELF_LOCALIZE_BY_VISUAL_MARKER')
    api.inhibitBehavior('SELF_LOCALIZE_BY_ODOMETRY')
    api.executeBehavior('LAND')
