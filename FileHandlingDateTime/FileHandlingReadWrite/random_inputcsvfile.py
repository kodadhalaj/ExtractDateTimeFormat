"""
Generate a random valid ISO 8601 datetime string
Expected datetime format: Format produced: YYYY-MM-DDThh:mm:ssTZD

    Implementation Details:
        - Chooses a random datetime between Jan 1, 2000 and Dec 31, 2030.
        - Adds a random number of seconds to the start date to create variety.
        - Appends a random timezone:
        - Either "Z" for UTC Or a random offset between ±00:00 and ±14:45
        - Generate some of the duplicate datetime values
        - Generate some of the invalid datetime values (example: YYYY-MM-DD , YYYY/MM/DDThh:mm:ssTZD

"""
import csv
import random
from datetime import datetime, timedelta

def random_valid_datetime() -> str:
    """Generate a random valid ISO 8601 datetime string."""
    start = datetime(2000, 1, 1, 0, 0, 0)
    end = datetime(2030, 12, 31, 23, 59, 59)

    delta = end - start
    random_seconds = random.randint(0, int(delta.total_seconds()))
    dt = start + timedelta(seconds=random_seconds)

    # Random timezone offset (Z or ±hh:mm)
    if random.random() < 0.5:
        tz = "Z"
    else:
        sign = random.choice(["+", "-"])
        hh = str(random.randint(0, 14)).zfill(2)
        mm = str(random.choice([0, 15, 30, 45])).zfill(2)
        tz = f"{sign}{hh}:{mm}"

    return dt.strftime("%Y-%m-%dT%H:%M:%S") + tz


#Generate an intentionally invalid datetime string.
#Purpose:
        #Creates malformed or incorrectly formatted values
        #to simulate "bad data" in the dataset.

def random_invalid_datetime() -> str:

    samples = [
        "2024-13-40T25:61:61Z",    # invalid month, day, time
        "2024/01/01 12:00:00",     # wrong separators
        "abcd-ef-ghT12:34:56Z",    # non-numeric
        "2024-09-22",              # missing time
        "20240922T123456Z",        # compact form, not allowed
        "2024-09-22T12:34",        # missing seconds + TZ
    ]
    return random.choice(samples)

#Main driver function to generate a sample CSV input file
#containing valid, invalid, and duplicate datetime values.

#Shuffle the list to mix valid, invalid, and duplicates.
#Write the values into a CSV file with a "datetime" header.

#Output:
        #A file named "datetime_inputfile.csv" will be created
        #in the current directory containing ~100 datetime records.

def main():
    output_file = "datetime_inputfile.csv"
    values = []

    # Generate ~70 valid values
    for _ in range(70):
        values.append(random_valid_datetime())

    # Generate ~20 invalid values
    for _ in range(20):
        values.append(random_invalid_datetime())

    # Add ~10 duplicates
    for _ in range(10):
        values.append(random.choice(values))

    # Shuffle them
    random.shuffle(values)

    # Write to CSV
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["datetime"])  # header
        for v in values:
            writer.writerow([v])

    print(f"Generated {len(values)} date-time values in {output_file}")

if __name__ == "__main__":
    main()
