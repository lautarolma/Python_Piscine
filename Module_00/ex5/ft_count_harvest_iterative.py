def ft_count_harvest_iterative():
"""Harvest reminder with days count-down"""

    n_days = int(input("Days until harvest: "))
    for i in range(1, n_days + 1): 
        print(f"Day {i}")
    print("Harvest time!")
