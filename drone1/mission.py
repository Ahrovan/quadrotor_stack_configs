import executive_engine_api as api

def runMission():
    api.activateBehavior('SELF_LOCALIZE_BY_ODOMETRY')
    api.executeBehavior('TAKE_OFF')
    api.inhibitBehavior('SELF_LOCALIZE_BY_ODOMETRY')
    api.activateBehavior('SELF_LOCALIZE_BY_VISUAL_MARKER')
    api.executeBehavior('GO_TO_POINT', coordinates=[0, 0.55, 1.2])
    api.executeBehavior('GO_TO_POINT', coordinates=[3, 0.55, 1.2])
    api.executeBehavior('GO_TO_POINT', coordinates=[8, 0, 1.2])
    api.executeBehavior('ROTATE', angle=180)
    api.inhibitBehavior('SELF_LOCALIZE_BY_VISUAL_MARKER')
    api.executeBehavior('LAND')
