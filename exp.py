import threading
import time
import random
import sys

# A flag to determine if the race has been won
race_won = False
winner = None

def car_race(color, distance, speed):
    global race_won, winner
    distance_traveled = 0
    while distance_traveled < distance:
        # Simulate car movement
        distance_traveled += speed
        # Obstacle encounter
        if random.randint(1, 10) > 8:  # 20% chance to hit an obstacle
            print(f"{color} car hit an obstacle!")
            time.sleep(random.uniform(1, 2))  # Delay due to the obstacle

        # Update the console with the car's progress using ASCII art
        sys.stdout.write(f"\r{color} car: {'=' * (distance_traveled // 10)}{'>'} ({distance_traveled}km)")
        sys.stdout.flush()
        
        # Random delay to simulate varying speeds
        time.sleep(random.uniform(0.5, 1.5))
        
        if distance_traveled >= distance:
            if not race_won:
                race_won = True
                winner = color
                print(f"\n{color} car wins the race!")
            break

def main():
    # User input for distances and speeds
    distance_blue = int(input("Enter the distance for the Blue car: "))
    speed_blue = int(input("Enter the speed for the Blue car: "))
    distance_red = int(input("Enter the distance for the Red car: "))
    speed_red = int(input("Enter the speed for the Red car: "))

    # Create threads for each car
    blue_thread = threading.Thread(target=car_race, args=("Blue", distance_blue, speed_blue))
    red_thread = threading.Thread(target=car_race, args=("Red", distance_red, speed_red))

    # Start the race
    blue_thread.start()
    red_thread.start()

    # Wait for both cars to finish
    blue_thread.join()
    red_thread.join()

    if winner:
        print(f"The winner of the race is the {winner} car!")

if __name__ == "__main__":
    main()
