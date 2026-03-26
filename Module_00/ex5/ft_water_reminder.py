def ft_water_reminder():
    """Watering reminder"""
    n_days = int(input("Days since last watering: "))
    if n_days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
