def ft_plant_age():
"""Displays if the plant its ready to harvest by checking the imput age"""

    plant_age = int(input("Enter plant age in days: "))
    if plant_age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
