import executive_engine_api as api

def runMission():
    print "Starting mission..."

    print "Activating Localization by odometry"
    activated, localization_uid = api.activateBehavior('SELF_LOCALIZE_BY_ODOMETRY')
    print "Odometry activated"

    print "Taking off..."
    result = api.executeBehavior('TAKE_OFF')
    print "Take off finished with status: %s" % str(result)

    print "Move to a higher position"
    result = api.executeBehavior('GO_TO_POINT', relative_coordinates=[0, 0, 0.5])
    print "Go to point finished with status: %s" % str(result)

    print "Memorizing current point..."
    success, unification = api.consultBelief('position(self, (?X, ?Y, ?Z))')
    if success:
        print "Position memorized correctly"
        x, y, z = unification['X'], unification['Y'], unification['Z']
        #print x, y, z
    else:
        print "Position unknown, landing..."
        result = api.executeBehavior('LAND')
        print "Landed with status: %s" % str(result)
        return

    print "Moving to desired point..."
    result = api.executeBehavior('GO_TO_POINT', coordinates=[2, 6.5, 1.2])
    print "Go to point finished with status: %s" % str(result)

    print "Rotating 180 degrees..."
    result = api.executeBehavior('ROTATE', angle=-90)
    print "Go to point finished with status: %s" % str(result)

    print "Going back to initial point..."
    result = api.executeBehavior('GO_TO_POINT', coordinates=[x, y, z])
    print "Go to point ended with status: %s" % str(result)

    print "Landing..."
    result = api.executeBehavior('LAND')
    print "Landed with status: %s" % str(result)

    # print "Deactivating Localization by odometry"
    # api.inhibitBehavior(localization_uid)
    # print "Odometry deactivated"

    print "Mission ended"
