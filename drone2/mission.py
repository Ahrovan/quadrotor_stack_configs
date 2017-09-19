import executive_engine_api as api

def runMission():
    api.activateBehavior('SELF_LOCALIZE_BY_VISUAL_MARKER')
    api.executeBehavior('TAKE_OFF')

    api.executeBehavior('GO_TO_POINT', coordinates=[0, -1.3, 1.3])
    api.executeBehavior('GO_TO_POINT', coordinates=[3.4, -1.3, 1.3])
   
    api.executeBehavior('ROTATE', angle=180)
    
    api.executeBehavior('GO_TO_POINT', coordinates=[3.4, -1.3, 1.3])
    api.executeBehavior('GO_TO_POINT', coordinates=[0, -1.3, 1.3])
    api.executeBehavior('GO_TO_POINT', coordinates=[0, 0, 2])
    
    api.executeBehavior('LAND_ON_STATIC_PLATFORM')
    api.inhibitBehavior('SELF_LOCALIZE_BY_VISUAL_MARKER')

    api.executeBehavior('LAND')
