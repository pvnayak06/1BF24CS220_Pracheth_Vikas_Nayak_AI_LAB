def get_valid_status(prompt):
    while True:
        status = input(prompt).strip().capitalize()
        if status in ("Clean", "Dirty"):
            return status
        print("Invalid input. Please enter 'Clean' or 'Dirty'.")

def get_valid_location(prompt):
    while True:
        loc = input(prompt).strip().upper()
        if loc in ("A", "B"):
            return loc
        print("Invalid input. Please enter 'A' or 'B'.")

def vacuum_cleaner_agent():
    # Take user input for the environment
    status_a = get_valid_status("Enter status of Room A (Clean/Dirty): ")
    status_b = get_valid_status("Enter status of Room B (Clean/Dirty): ")
    start_location = get_valid_location("Enter starting location (A/B): ")

    environment = {"A": status_a, "B": status_b}
    location = start_location
    total_cost = 0
    steps = 0
    max_steps = 10  # safety limit

    print("\nInitial environment:", environment)
    print()

    while steps < max_steps:
        status = environment[location]
        print(f"Step {steps}: Agent at {location}, status = {status}")

        if status == "Dirty":
            print(f"  -> Cleaning {location}")
            environment[location] = "Clean"
            total_cost += 1
        else:
            print(f"  -> {location} is already clean")

        if all(s == "Clean" for s in environment.values()):
            print("\nAll locations are clean. Task complete.")
            break

        # Move to the other location
        location = "B" if location == "A" else "A"
        total_cost += 1  # cost for moving
        steps += 1

    print(f"\nFinal environment state: {environment}")
    print(f"Total cost (cleaning + moves): {total_cost}")


if __name__ == "__main__":
    vacuum_cleaner_agent()