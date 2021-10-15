# ESC180 Project 1
# gamify.py
# Oct 14, 2021

# Done in collaboration by:
# Ma, Carl Ka To (macarl1) and
# Xu, Shen Xiao Zhu (xushenxi)

# NOTE: TEST RUN, SUBMISSION NOT FINAL

def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''
    
    global cur_hedons, cur_health, cur_time
    global last_activity, last_activity_duration, last_finished
    global bored_with_stars
    global time_stars
    time_stars = []

    global tired, star_offer_time
    tired = False

    star_offer_time = -1000
    
    cur_hedons = 0
    cur_health = 0
    
    cur_star = None
    total_num_stars = 0
    cur_star_activity = None
    
    bored_with_stars = False
    
    last_activity = None
    last_activity_duration = 0
    
    cur_time = 0
    
    last_finished = -1000
    

            

def star_can_be_taken(activity):
    global bored_with_stars, cur_time, cur_star_activity
    new_time_stars = []
    for i in time_stars:
        if not (max(time_stars) - i > 120):
            new_time_stars.append(i)

    if len(new_time_stars) > 2:
        bored_with_stars = True
    
    if star_offer_time == cur_time and not bored_with_stars and activity == cur_star_activity:
        return True
    else:
        return False

    
def perform_activity(activity, duration):
    global cur_hedons, cur_health, cur_time
    global last_activity, last_activity_duration, last_finished
    global bored_with_stars

    #print("Performing: " + activity)
    cur_hedons += estimate_hedons_delta(activity, duration)
    #print("Hedrons after " + activity + ": " + str(cur_hedons))
    cur_health += estimate_health_delta(activity, duration)
    #print("Health after " + activity + ": " + str(cur_health))
    if activity == last_activity:
        last_activity_duration += duration
    else:
        last_activity = activity
        last_activity_duration = duration
    
    cur_time += duration

    if activity != "resting":
        last_finished = cur_time
    

def get_cur_hedons():
    return cur_hedons
    
def get_cur_health():
    return cur_health
    
def offer_star(activity):
    global star_offer_time, cur_time, cur_star_activity
    star_offer_time = cur_time
    cur_star_activity = activity
    time_stars.append(cur_time)


        
def most_fun_activity_minute():
    #print("Calculating most_fun_activity_minute")
    return max((estimate_hedons_delta(i,1), i) for i in ["running", "textbooks", "resting"])[1]
    
################################################################################
#These functions are not required, but we recommend that you use them anyway
#as helper functions

def get_effective_minutes_left_hedons(activity):
    '''Return the number of minutes during which the user will get the full
    amount of hedons for activity activity'''
    pass
    
def get_effective_minutes_left_health(activity):
    pass

def estimate_hedons_delta(activity, duration):
    '''Return the amount of hedons the user would get for performing activity
    activity for duration minutes'''
    global tired
    if last_finished + 120 >= cur_time:
        tired = True
    else:
        tired = False

    hedons_delta = 0    

    if tired == True:
        #print("Tired")
        if activity == "running" or activity == "textbooks":
            hedons_delta += -2 * duration
            
        if activity == "resting":
            hedons_delta += 0
    else:
        #print("Not tired")
        if activity == "running":
            if duration <= 10:
                hedons_delta += 2 * duration
            else:
                hedons_delta += 2 * 10 - 2 * (duration - 10)
        if activity == "textbooks":
            if duration <= 20:
                hedons_delta += 1 * duration
            else:
                hedons_delta += 1 * 20 - 1 * (duration - 20)
        if activity == "resting":
            hedons_delta += 0

    if star_can_be_taken(activity):
        #print("using star")
        if duration <= 10:
            hedons_delta += 3 * duration
        else:
            hedons_delta += 30

    return hedons_delta
            

def estimate_health_delta(activity, duration):
    if activity == "running":

        if last_activity == "running":
            temp = last_activity_duration
        else:
            temp = 0
        
        if temp + duration <= 180:
            return 3 * duration
        elif temp <= 180:
            return 3 * (180 - temp) + 1 * (temp + duration - 180)
        else:
            return 1 * duration

    if activity == "textbooks":
        return 2 * duration
    if activity == "resting":
        return 0

    
################################################################################
        
if __name__ == '__main__':
    initialize()
    perform_activity("running", 30)    
    print(get_cur_hedons())            # -20 = 10 * 2 + 20 * (-2)             # Test 1
    print(get_cur_health())            # 90 = 30 * 3                          # Test 2           		
    print(most_fun_activity_minute())  # resting                              # Test 3
    perform_activity("resting", 30)    
    offer_star("running")              
    print(most_fun_activity_minute())  # running                              # Test 4
    perform_activity("textbooks", 30)  
    print(get_cur_health())            # 150 = 90 + 30*2                      # Test 5
    print(get_cur_hedons())            # -80 = -20 + 30 * (-2)                # Test 6
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            # 210 = 150 + 20 * 3                   # Test 7
    print(get_cur_hedons())            # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
    perform_activity("running", 170)
    print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10
