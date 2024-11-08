def vacuum_world():
    goal_state = {'A': 0, 'B': 0}
    cost = 0

    location_input = input("Enter location of vacuum (A/B): ")
    status_input = int(input(f"Enter status of {location_input} (0 for clean, 1 for dirty): "))
    status_input_compliment = int(input(f"Enter status of the other room (0 for clean, 1 for dirty): "))


    print("Initial location condition:", goal_state)

    if location_input == 'A':
        print("Vacuum is placed in location A")
        if status_input == 1:
            print("Location A is dirty")
            goal_state['A'] = 0
            cost += 1
            print("Location A has been cleaned. Cost:", cost)
        if status_input_compliment == 1:
            print("Location B is dirty")
            print("Moving right to location B")
            cost += 1
            print("Cost for moving right:", cost)
            goal_state['B'] = 0
            cost += 1
            print("Location B has been cleaned. Cost:", cost)
        else:
            print("Location B is already clean. No action. Cost:", cost)
    else:
        print("Vacuum is placed in location B")
        if status_input == 1:
            print("Location B is dirty")
            goal_state['B'] = 0
            cost += 1
            print("Location B has been cleaned. Cost:", cost)
        if status_input_compliment == 1:
            print("Location A is dirty")
            print("Moving left to location A")
            cost += 1
            print("Cost for moving left:", cost)
            goal_state['A'] = 0
            cost += 1
            print("Location A has been cleaned. Cost:", cost)
        else:
            print("Location A is already clean. No action. Cost:", cost)

    print("Goal state:", goal_state)
    print("Performance measure (total cost):", cost)

vacuum_world()
