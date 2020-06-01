def reward_function(params):

    # Read input parameters
    on_track = params['all_wheels_on_track']
    closest_waypoints = params['closest_waypoints']
    distance_from_center = params['distance_from_center']
    is_left_of_center = params['is_left_of_center']
    track_width = params['track_width']
    steering = abs(params['steering_angle']) # Only need the absolute steering angle

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the agent is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 2
    elif distance_from_center <= marker_2:
        reward = 0
    elif distance_from_center <= marker_3 and distance_from_center >= marker_2:
        reward = 0
    else:
        reward = 0  # likely crashed/ close to off track
        
    if on_track:
        reward += 3
        
    # Give higher reward if the agent stays left
    if is_left_of_center:
        reward += 1
        
    # Read input variable
    steps = params['steps']
    progress = params['progress']
    
    # Total num of steps we want the car to finish the lap, it will vary depends on the track length
    TOTAL_NUM_STEPS = 100

    # Give additional reward if the car pass every 100 steps faster than expected 
    if (steps % 100) == 0 and progress > (steps / TOTAL_NUM_STEPS) * 100 :
        reward += 10.0

    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 10

    # Penalize reward if the agent is steering too much
    if steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    return float(reward)