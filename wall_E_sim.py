import random

# Dictionary representing zones in the city
city_zones = {
    "Zone 1": [],
    "Zone 2": [],
    "Zone 3": [],
    "Zone 4": [],
    "Zone 5": [],
    "Zone 6": [],
    "Zone 7": [],
    "Zone 8": [],
    "Zone 9": ["boss"]
}

# List of possible items
possible_items = ["scrap metal", "power cell", "plastic", "wire", "short circuit", "battery pack", "rubber", "gear", "rusty key?", "keygen", "strange keycard"]

# Locked zones and their required keys
locked_zones = {
    "Zone 6": "rusty key?",
    "Zone 8": "keygen",
    "Zone 9": "strange keycard"
}

# Robot's inventory to store collected power cells and keys
robot_inventory = []

# Initial battery level and boss health
battery_level = 10
boss_health = 15

# Function to set difficulty level
def set_difficulty():
    global battery_level, boss_health
    while True:
        difficulty = input("Choose difficulty (easy/normal/hard): ").strip().lower()
        if difficulty == "easy":
            battery_level = 20  # Increased battery level for easy mode
            boss_health = 10    # Reduced boss health for easy mode
            print("Easy mode selected. Your battery is 20, and the boss has 10 health.")
            break
        elif difficulty == "normal":
            battery_level = 10  # Default battery level for normal mode
            boss_health = 15    # Default boss health for normal mode
            print("Normal mode selected. Your battery is 10, and the boss has 15 health.")
            break
        elif difficulty == "hard":
            battery_level = 10  # Normal battery level for hard mode
            boss_health = 20    # Normal boss health for hard mode
            print("Hard mode selected. Your battery is 10, and the boss has 20 health.")
            break
        else:
            print("Invalid choice. Please choose 'easy', 'normal' or 'hard'.")

# Function to randomly generate items in zones
def generate_zone_items(zone):
    if zone != "Zone 9":
        # Randomly select 3 items from the possible items list
        items = random.sample(possible_items, 3)
        city_zones[zone] = items
    else:
        city_zones[zone] = ["boss"]

# Function to move to a different zone and search for items
def move_to_zone(zone):
    global battery_level
    if battery_level <= 0:
        print("Battery is dead. Game over.")
        return
    
    # Check if the zone is locked
    if zone in locked_zones and locked_zones[zone] not in robot_inventory:
        print(f"{zone} is locked. You need {locked_zones[zone]} to access it.")
        return
    
    if zone in city_zones:
        print(f"Moving to {zone}...")
        battery_level -= 1
        print(f"Battery level: {battery_level}")
        if not city_zones[zone]:
            generate_zone_items(zone)
        if zone == "Zone 9":
            boss_battle()
        else:
            search_for_items(zone)
    else:
        print("Invalid zone. Try again.")

# Function to search for items in the current zone
def search_for_items(zone):
    items = city_zones[zone]
    print(f"Items found in {zone}: {items}")
    for item in items:
        handle_item(item)

# Function to handle different items found in the zone
def handle_item(item):
    global battery_level
    if item == "power cell":
        robot_inventory.append(item)
        print(f"Collected a {item}!")
    elif item == "short circuit":
        battery_level -= 2
        print(f"Encountered a {item}! Battery level decreased by 2.")
    elif item == "battery pack":
        battery_level += 3
        print(f"Found a {item}! Battery level increased by 3.")
    elif item == "keygen":
        robot_inventory.append(item)
        print(f"Collected a {item}!")
    elif item == "rusty key?":
        robot_inventory.append(item)
        print(f"Collected a {item}!")
    elif item == "strange keycard":
        robot_inventory.append(item)
        print(f"Collected a {item}!")
    print(f"Current battery level: {battery_level}")

# Function to display the current inventory of collected power cells and keys
def display_inventory():
    print(f"Inventory: {robot_inventory}")
    print(f"Total power cells collected: {robot_inventory.count('power cell')}")

# Function to handle the boss battle
def boss_battle():
    global battery_level, boss_health
    print("[SYSTEM ALERT] You have encountered the boss! Prepare for battle!")
    while battery_level > 0 and boss_health > 0:
        player_attack = random.randint(1, 4)
        boss_attack = random.randint(1, 3)
        print(f"[SYSTEM] You attack the boss and deal {player_attack} damage!")
        boss_health -= player_attack
        if boss_health <= 0:
            print("[SYSTEM] You have defeated the boss! The boss dropped a power cell.")
            robot_inventory.append("power core")
            return
        print(f"[ALERT] Boss attacks and deals {boss_attack} damage!")
        battery_level -= boss_attack
        if battery_level <= 0:
            print("[ALERT] The boss has defeated you. Shutting Down... Game Over.")
            return
        print(f"[SYSTEM] Your battery level: {battery_level}, Boss health: {boss_health}")

# Set difficulty level before the game starts
set_difficulty()

# Main game loop
while battery_level > 0 and robot_inventory.count('power cell') < 8:
    print("\nCurrent zones: Zone 1, Zone 2, Zone 3, Zone 4, Zone 5, Zone 6, Zone 7, Zone 8, Zone 9")
    user_input = input("[SYSTEM] Enter the zone to move to or 'inventory' to check inventory: ").strip()
    
    if user_input.lower() == 'inventory':
        display_inventory()
    elif user_input in city_zones:
        move_to_zone(user_input)
    else:
        print("Invalid input. Try again.")

# End of game messages
if battery_level <= 0:
    print("[ALERT] Battery depleted. Shutting down... Game Over.")
elif robot_inventory.count('power cell') >= 5:
    print("[SYSTEM] All power cells collected. You Win!")
elif robot_inventory.count('power core') >= 1:
    print("[SYSTEM] Power core has been acquired. Quota fulfilled. You Win! [SECRET ENDING]")
