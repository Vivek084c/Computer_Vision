# Define locations with descriptions and exits
locations = {
    "forest": {
        "description": "You are standing in a dense forest. Sunlight struggles to penetrate the thick canopy of leaves.",
        "exits": {"north": "mountains", "south": "village"}
    },
    "mountains": {
        "description": "You stand on a rocky mountain path. A cold wind whistles through the sharp peaks.",
        "exits": {"south": "forest"}
    },
    "village": {
        "description": "You arrive in a quaint village. Smoke curls from chimneys and children play in the square.",
        "exits": {"north": "forest"}
    }
}

# Current location
current_location = "forest"

# Game loop
while True:
    # Print current location description
    print(locations[current_location]["description"])

    # Show available exits
    print("Exits:", ", ".join(locations[current_location]["exits"].keys()))

    # Get user input for next move
    direction = input("Which direction do you want to go? ").lower()

    # Check if chosen exit exists
    if direction in locations[current_location]["exits"]:
        current_location = locations[current_location]["exits"][direction]
    else:
        print("You can't go that way.")

    # Check for win condition (reaching village)
    if current_location == "village":
        print("You've reached the village! You win!")
        break

