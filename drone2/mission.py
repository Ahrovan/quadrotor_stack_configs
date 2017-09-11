import executive_engine_api as api

def runMission():
    api.activateBehavior('SELF_LOCALIZE_BY_ODOMETRY')
    api.executeBehavior('TAKE_OFF')
    api.inhibitBehavior('SELF_LOCALIZE_BY_ODOMETRY')
    # api.executeBehavior('ROTATE', angle=90)
    # api.executeBehavior('GO_TO_POINT', relative_coordinates=[0, 0, 1])
    # for i in range(10):
    # api.executeBehavior('GO_TO_POINT', relative_coordinates=[2, 0, 0])
    api.executeBehavior('DROP_OBJECT')
    api.executeBehavior('LAND')
