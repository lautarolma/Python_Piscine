def ft_count_harvest_recursive():
    """Harvest reminder with days count-down"""
    n_days = int(input("Days until harvest: "))

    def count_days(actual_day, limit):
        """Recursive aux function for the harvest reminder"""
        if actual_day > limit:
            print("Harvest time!")
            return
        print(f"Day {actual_day}")
        count_days(actual_day + 1, limit)

    count_days(1, n_days)
