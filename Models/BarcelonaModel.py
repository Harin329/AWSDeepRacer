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
        reward = 1
    elif distance_from_center <= marker_2:
        reward = 0
    elif distance_from_center <= marker_3 and distance_from_center >= marker_2:
        reward = 2
    else:
        reward = 0  # likely crashed/ close to off track
        
    if on_track:
        reward += 5
        
    # Give higher reward if the agent stays left
    if is_left_of_center:
        reward += 1
        
    line = [
    [0, -2],
    [-5, -2.5],
    [-8.6, 2.65],
    [-6, 4.9],
    [-3, 4.9],
    [-2.5, 2.25],
    [-4.7, 1.75],
    [-3.5, -0.5],
    [-2.5, -0.75],
    [1, 4],
    [3, 3],
    [5, 0],
    [6.5, 2],
    [5.15, 3.75],
    [7.75, 4.25],
    [9.5, -0.8],
    [7, -2],
    [0, -2]
    ]
    
    # Read input parameters
    x = params['x']
    y = params['y']
    position = [x, y]
    progress = params['progress']
    offTrack = params['is_offtrack']
    
    if position in line:
        reward += 1
        
    import math

    # Read input variables
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']

    # Calculate the direction of the center line based on the closest waypoints
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0]) 
    # Convert to degree
    track_direction = math.degrees(track_direction)

    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    # Penalize the reward if the difference is too large
    DIRECTION_THRESHOLD = 10.0
    if direction_diff > DIRECTION_THRESHOLD:
        reward *= 0.5
        
    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 15

    # Penalize reward if the agent is steering too much
    if steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8
    

    return float(reward)