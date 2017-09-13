import executive_engine_api as api

def runMission():
    api.activateBehavior('SELF_LOCALIZE_BY_ODOMETRY')
    api.executeBehavior('TAKE_OFF')
    api.inhibitBehavior('SELF_LOCALIZE_BY_ODOMETRY')

    api.activateBehavior('SELF_LOCALIZE_BY_VISUAL_MARKER')
    api.executeBehavior('GO_TO_POINT', coordinates=[0, -1.25, 1.3])
    api.executeBehavior('GO_TO_POINT', coordinates=[3.75, -1.25, 1.3])
    api.executeBehavior('GO_TO_POINT', coordinates=[3.75, -2.25, 1.3])
    api.executeBehavior('ROTATE', angle=90)
    api.executeBehavior('ROTATE', angle=180)
    api.executeBehavior('GO_TO_POINT', coordinates=[3.75, -1.25, 1.3])
    api.executeBehavior('GO_TO_POINT', coordinates=[0, -1.25, 1.3])
    api.executeBehavior('LAND_ON_STATIC_PLATFORM')
    api.inhibitBehavior('SELF_LOCALIZE_BY_VISUAL_MARKER')
    # api.inhibitBehavior('SELF_LOCALIZE_BY_ODOMETRY')
    api.executeBehavior('LAND')
