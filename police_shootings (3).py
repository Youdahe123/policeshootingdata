def create_database(filename):
    data_file = open(filename, 'r')  # Open file
    data_lines = data_file.readlines()  # Read lines

    database = {}  # Initialize database
    for row in range(1, len(data_lines)):  # Loop through rows
        line = data_lines[row]
        entries = line.split(',')  # Split line by comma
        db_entry = {"name": entries[11], "date": entries[1], "armed_with": entries[4], "age": entries[12],  # Create entry
                    "gender": entries[13], "race": entries[14], "state": entries[7]}
        entry_id = int(entries[0])  # Convert ID to integer
        database[entry_id] = db_entry  # Add to database

    return database  # Return database


def main():
    db = create_database('fatal-police-shootings-data.csv')  # Create database

    unarmed_selection = 0  # Counter for unarmed
    unarmed_race_counts = {}  # Dictionary for unarmed race counts
    for entry_id, db_entry in db.items():  # Loop through database entries
        if db_entry["armed_with"] == "unarmed":  # Check if unarmed
            race = db_entry["race"]  # Get race
            if race in unarmed_race_counts:  # If race exists in dictionary
                unarmed_race_counts[race] += 1  # Increment count
            else:
                unarmed_race_counts[race] = 1  # Initialize count
            unarmed_race_counts[race] = unarmed_race_counts.get(race, 0) + 1  # Ensure key exists
            unarmed_selection += 1  # Increment unarmed selection counter

    total_shootings = len(db)  # Total fatal shootings
    unarmed_total = len(unarmed_race_counts)  # Total unarmed shootings

    race_counts = {}  # Initialize race count dictionary
    for entry_id, db_entry in db.items():  # Loop through database entries
        race = db_entry["race"]  # Get race
        race_counts[race] = race_counts.get(race, 0) + 1  # Count race occurrences

        if entry_id == 1694:  # Check for ID 1694
            print(f"Name with ID 1694: {db_entry['name']}")  # Print name for ID 1694

        if db_entry["state"] == "MN":  # Check if from Minnesota
            print(f" from Minnesota: {db_entry['name']}")  # Print name from MN

    print("\nFraction of fatal police shootings by race:")  # Print race fractions
    for race, count in race_counts.items():  # Loop through race counts
        fraction = count / total_shootings  # Calculate fraction
        print(f"{race}: {fraction:.4f}")  # Print fraction

    print("\nFraction of fatal police shootings by unarmed race:")  # Print unarmed race fractions
    for race, count2 in unarmed_race_counts.items():  # Loop through unarmed race counts
        fraction1 = count2 / unarmed_total  # Calculate fraction
        print(f"{race}:{fraction1:.4f}")  # Print fraction


if __name__ == "__main__":  # Run main if this is the main script
    main()
