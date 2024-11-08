import random

def calculate_tour_length(tour, distance_matrix):
    length = 0
    # Calculate the total distance of the tour
    for i in range(len(tour)):
        length += distance_matrix[tour[i]][tour[(i + 1) % len(tour)]]
    return length

def generate_random_order(tour):
    swapped = tour[:]
    
    # Swap two cities to create a neighboring tour
    i, j = random.sample(range(len(tour)), 2)
    swapped[i], swapped[j] = swapped[j], swapped[i]
    return swapped

def hill_climbing_tsp(distance_matrix, iterations=1000):
    # Create an initial random tour
    num_cities = len(distance_matrix)
    current_tour = list(range(num_cities))
    print(current_tour)
    random.shuffle(current_tour)
    
    # Calculate the length of the initial tour
    current_length = calculate_tour_length(current_tour, distance_matrix)
    
    # Hill Climbing iterations
    for _ in range(iterations):
        swapped = generate_random_order(current_tour)
        new_length = calculate_tour_length(swapped, distance_matrix)
        
        # If the neighbor tour is shorter, move to this neighbor
        if new_length < current_length:
            current_tour = swapped
            current_length = new_length

    return current_tour, current_length

# Example usage
if __name__ == "__main__":
    # Example symmetric distance matrix
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    best_tour, best_length = hill_climbing_tsp(distance_matrix)
    print("Best tour:", best_tour)
    print("Total distance:", best_length)
