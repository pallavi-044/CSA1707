def vacuum_cleaner(state, start):
    location = start
    print("Initial state:", state, "Starting at:", location)

    while "Dirty" in state.values():
        if state[location] == "Dirty":
            print(f"Location {location} is Dirty → Clean it")
            state[location] = "Clean"
        else:
            print(f"Location {location} is already Clean")

        # Move to the other room
        location = "B" if location == "A" else "A"
        print("Move to", location)

    print("Final state:", state)
    print("All rooms are clean!")

# --- Run ---
rooms = {"A": "Dirty", "B": "Dirty"}  # Initial condition
start = "A"  # Starting room
vacuum_cleaner(rooms, start)
