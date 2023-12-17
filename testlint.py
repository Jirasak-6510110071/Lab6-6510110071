"""
testlint.py
"""

CAPTAIN = "Picard"


def initiate_warp_speed(order):
    """
    Run function
    """
    if order == "engage":
        print("Initiating warp speed")
    else:
        print("You are not the captain of this vessel")


initiate_warp_speed("engage")
