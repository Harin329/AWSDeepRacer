def reward_function(params):
    
    # Read input parameters
    offtrack = params["is_offtrack"]
    steps = params["steps"]
    progress = params["progress"]
    speed = params["speed"]

    if (not offtrack) and steps > 0:
        reward = ((progress / steps) * 100) + (speed**2)
    else:
        reward = 1e-3
        
    return float(reward)