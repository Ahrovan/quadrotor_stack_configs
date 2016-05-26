Mission: Search in a square

Brief: The Drone flies in a square trajectory and if it finds a visual marker it goes Home and Lands.
Details: The Drone flies following the trajectory:
    (4.0, 4.0, 0.7) -> (6.0, 4.0, 1.0) -> (6.0, 6.0, 1.0) -> (4.0, 6.0, 1.0) -> (4.0, 4.0, 1.0)

Initial Point: (4.0, 4.0, 0.0)
Initial Point after take-off: (4.0, 4.0, 0.7)
Initial Yaw: 0º

Obstacles:
    1. center=(5.0, 3.8), heigth=1.3, length=0.2, width=0.2  <-- Check if height is correct

Recognized Visual Markers:
    1. Type=Aruco Marker, id=0, Effect=Triggers Event 1

Events:
    1. Name='Return Gome', Trigger=Visual Marker 1
    2. Name='Low Battery', Trigger=Battery percentaje below 25%


IMPORTANT:
The file ekf_state_estimator_config.xml in examples/missions/search_in_a_square/ is not being read
This is due a mistake in the code of the droneEKFStateEstimatorROSModule. Until this mistake is corrected,
the ekf_state_estimator_config.xml file will have to be copied to the drone1/ directory.