CAPTAIN = "Picard"


def initiate_warp_speed(order):
    if order == "engage":
        print("Initiating warp speed")
    else:
        print("You are not the captain of this vessel")


initiate_warp_speed("engage")
