captain = "Picard"


def initiate_warp_speed(order):
    if order == "engage":
        print("initiating warp speed")
    else:
        print("you are not the captain of this vessel")


initiate_warp_speed("engage")
