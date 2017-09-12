import executive_engine_api as api

def runMission():
    api.executeBehavior('TAKE_OFF')
    api.activateBehavior('PAY_ATTENTION_TO_VISUAL_MARKERS')
    api.executeBehavior('MOVE_TO_VISUAL_MARKER', marker_id=0)
    api.inhibitBehavior('PAY_ATTENTION_TO_VISUAL_MARKERS')
    api.executeBehavior('LAND_ON_STATIC_PLATFORM')