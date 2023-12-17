CAPTAIN = "Picard"


def initiateWarpSpeed(order):
    if order == "engage":
        print("initiating warp speed")
    else:
        print("you are not the captain of this vessel")


initiateWarpSpeed("engage")
