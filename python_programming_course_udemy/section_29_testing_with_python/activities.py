# def eat( food, is_healthy ):
#     pass
    
# def nap( num_hours ):
#     pass
# this has been tested and it is working
# ==============================================

def eat( food, is_healthy ):
    ending = "because YOLO!"
    if is_healthy:
        ending = "because my body is a temple" 
    return f"I'm eating {food}, {ending}"
    
def nap( num_hours ):
    if num_hours == 1:
        return "I'm feeling refreshed after 1 hour of nap"
    return "Ugh I overslept. I didn't mean to nap for 3 hours"