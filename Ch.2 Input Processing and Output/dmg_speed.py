# Create a program that takes damage and speed (attacks per second) and returns the amount of damage after a given time.

# inputs
# Damage
# ATK Speed

# Process
# What is the amount of damage
# What is the Attack speed
# Multiply ATK Speed * Damage

# Output
# amount of damage after a given time

damage_per_attack = float(input("Enter damage per attack: "))
attacks_per_second = float(input("Enter attacks per second: "))
time_seconds = float(input("Enter time in seconds: "))
total_damage = damage_per_attack * attacks_per_second * time_seconds

print(f"Total damage after {time_seconds:.2f} seconds: {total_damage:.2f}")
