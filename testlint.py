"""
This module provides functions related to warp speed initiation.
"""

CAPTAIN = "Picard"


def initiate_warp_speed(order):
    """
    Initiate warp speed based on the given order.

    Parameters:
    - order (str): The order given to initiate warp speed.

    Returns:
    None
    """
    if order == "engage":
        print("Initiating warp speed")
    else:
        print("You are not the captain of this vessel")


initiate_warp_speed("engage")

