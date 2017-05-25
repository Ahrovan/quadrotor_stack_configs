import executive_engine_api as api
import rospy
from std_msgs.msg import String

homeX = 2
homeY = 2
homeZ = 0
exit = False
finish = False
state = 0

###############################################################################
######## Function for interpreting messages received from the operator ########
###############################################################################
def msgCallback(msg):
    global homeX, homeY, homeZ, exit, state
    message = ""
    if msg != "unused":
        message = msg.data
    if message == "to":
        api.executeBehavior('TAKE_OFF')
        memorizePoint()
        print("Home position set at (%s, %s, %s)" % (homeX, homeY, homeZ))
    elif message == "l":
        api.executeBehavior('LAND')
        print "Landing"
    elif message == "s":
        api.executeBehavior('START_HOVERING')
        print "Hovering"
    elif message == "mu":
        moveUp(message)
        print "Moving Up"
    elif message == "md":
        moveDown(message)
        print "Moving Down"
    elif message == "mr":
        moveRight(message)
        print "Moving Right"
    elif message == "ml":
        moveLeft(message)
        print "Moving Left"
    elif message == "zi":
        api.executeBehavior('GO_TO_POINT', relative_coordinates = [ 0, 1, 0])
        print "Zooming In"
    elif message == "zo":
        api.executeBehavior('GO_TO_POINT', relative_coordinates = [ 0, -1, 0])
        print "Zooming Out"
    #elif message == "cp":
    #    api.executeBehavior('NOTIFY_OPERATOR')
    #elif message == "ton":
    #    api.executeBehavior('NOTIFY_OPERATOR')
    #elif message == "toff":
    #    api.executeBehavior('NOTIFY_OPERATOR')
    #elif message == "sp":
    #    api.executeBehavior('NOTIFY_OPERATOR')
    elif message == "cm":
        state -= 1
        print "Resuming Mission"
        msgCallback("unused")
    elif message == "sm" or message == "zz" or state == 0 or state == 1:
        if message == "sm":
            print "Starting Mission"
            print "Inspection type: Zig Zag"
        elif message == "zz":
            print "Changed Inspection Strategy to: Zig Zag"
        message = ""
        while not api.trueBelief('visible(aruco_5)') and message == "":
            if state == 0:
                state = 1
                print "Moving right"
                moveRight(message)
                if exit == False:
                    message = ""
                    print "going up"
                    api.executeBehavior('GO_TO_POINT', relative_coordinates = [ 0, 0, 1])
                    try:
                        # Wait for message (Subscribing to topic 'order')
                        message = rospy.client.wait_for_message('order', String, timeout = 1)
                        if message != "":
                            exit = True
                            msgCallback(message)
                    except rospy.ROSException, e: #Timeout exception handling
                        pass
            if exit == False:
                if state == 1:
                    state = 2
                    print "moving left"
                    moveLeft(message)
                if exit == False:
                    message = ""
                    print "going up"
                    api.executeBehavior('GO_TO_POINT', relative_coordinates = [ 0, 0, 1])
                    try:
                        message = rospy.client.wait_for_message('order', String, timeout = 1)
                        if message != "":
                            exit = True
                            msgCallback(message)
                    except rospy.ROSException, e:
                        pass
            try:
                message = rospy.client.wait_for_message('order', String, timeout = 1)
                msgCallback(message)
            except rospy.ROSException, e:
                pass
            if exit == True: #Condition for exiting the main process execution  
                break
    elif message == "ud" or state == 2 or state == 3:
        if message == "ud":
            print "Changed Inspection Strategy to: Up and Down"
        message = ""
        while not api.trueBelief('visible(aruco_5)') or message == "":
            if state == 2:
                state = 3
                moveUp(message)
            if exit == False:
                message = ""
                api.executeBehavior('GO_TO_POINT', relative_coordinates = [ 1, 0, 0])
                try:
                    message = rospy.client.wait_for_message('order', String, timeout = 1)
                    if message != "":
                        exit = True
                        msgCallback(message)
                except rospy.ROSException, e:
                    pass
            if exit == False:
                if state == 3:
                    state = 4
                    moveLeft(message)
            if exit == False:
                message = ""
                api.executeBehavior('GO_TO_POINT', relative_coordinates = [ 1, 0, 0])
                try:
                    message = rospy.client.wait_for_message('order', String, timeout = 1)
                    if message != "":
                        exit = True
                        msgCallback(message)
                except rospy.ROSException, e:
                    pass
            try:
                message = rospy.client.wait_for_message('order', String, timeout = 1)
                msgCallback(message)
            except rospy.ROSException, e:
                pass
            if exit == True: 
                break
    elif message == "fm":
        global finish
        goHome()
        api.executeBehavior('LAND')
        finish = True
    elif message == "gh":
        print "Going to point labeled as \"Home\""
        goHome()
    else:
        pass

#######################################################################
############################ Main function ############################
#######################################################################
def runMission():
    global exit, state
    print("Starting mission")
    msg = ""
    while msg == "" and finish == False:
        msg = rospy.client.wait_for_message('order', String, timeout = 20)
        #msgCallback(msg)
        msg = ""
        exit = False

    print("Mission ended")

#######################################################################
######################## Moving Right function ########################
#######################################################################
def moveRight(msg):
    global exit
    api.executeBehavior('MOVE', direction="RIGHT", speed = 1)
    while not api.trueBelief('visible(aruco_1)') and msg == "":
        try:
            msg = rospy.client.wait_for_message('order', String, timeout = 1)
            if msg != "":
                exit = True
                msgCallback(msg)
        except rospy.ROSException, e:
            pass

    api.executeBehavior('START_HOVERING')

########################################################################
######################### Moving Left function #########################
########################################################################
def moveLeft(msg):
    global exit
    api.executeBehavior('MOVE', direction="LEFT", speed = 1)
    while not api.trueBelief('visible(aruco_2)') or msg == "":
        try:
            msg = rospy.client.wait_for_message('order', String, timeout = 1)
            if msg != "":
                exit = True
                msgCallback(msg)
        except rospy.ROSException, e:
            pass

    api.executeBehavior('START_HOVERING')
        
######################################################################
######################### Moving Up function #########################
######################################################################
def moveUp(msg):
    global exit
    api.executeBehavior('MOVE', direction="UPWARD", speed = 1)
    while not api.trueBelief('visible(aruco_3)') and msg == "":
        try:
            msg = rospy.client.wait_for_message('order', String, timeout = 1)
            if msg != "":
                exit = True
                msgCallback(msg)
        except rospy.ROSException, e:
            pass

    api.executeBehavior('START_HOVERING')

######################################################################
######################## Moving Down function ########################
######################################################################
def moveDown(msg): 
    global exit
    api.executeBehavior('MOVE', direction="DOWNWARD", speed = 1)
    while not api.trueBelief('visible(aruco_4)') and msg == "":
        try:
            msg = rospy.client.wait_for_message('order', String, timeout = 1)
            if msg != "":
                exit = True
                msgCallback(msg)
        except rospy.ROSException, e:
            pass

    api.executeBehavior('START_HOVERING')

#######################################################################
######################### Going Home function #########################
#######################################################################
def goHome(msg):
    global homeX, homeY, homeZ
    api.executeBehavior('GO_TO_POINT', point = [ homeX, homeY, homeZ])

#########################################################################
######################## Memorize Point function ########################
#########################################################################
def memorizePoint():
    global homeX, homeY, homeZ
    success, unification = api.consultBelief('position(self, (?X, ?Y, ?Z))')
    if success:
        homeX, homeY, homeZ = unification['X'], unification['Y'], unification['Z']


