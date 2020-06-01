def reward_function(params):

    # Read input variable
    steps = params['steps']
    progress = params['progress']
    speed = params['speed']
    
    # Initialize the reward with typical value 
    reward = 0.0
    
    if progress == 100:
        reward += 150
    
    # Read input variable
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    isLeft = params['is_left_of_center']

    # Penalize if the car is too far away from the center
    marker = 0.5 * track_width

    if distance_from_center <= marker and isLeft:
        reward += 1
        
    reward *= speed

    return reward