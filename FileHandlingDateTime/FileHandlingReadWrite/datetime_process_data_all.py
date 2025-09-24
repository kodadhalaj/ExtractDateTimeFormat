"""
Module Description:
This program reads large list of datetime values from an input file, filters out duplicates and
invalid entries based on the ISO 8601 datetime format (YYYY-MM-DDThh:mm:ssTZD),
and classify them into valid, duplicates, and invalid and writes results into
    three separate files:
        - `valid_file`: unique valid datetime strings
        - `duplicates_file`: repeated valid values beyond the first occurrence
        - `invalid_file`: all values that do not match ISO 8601 format

The filtering is performed using a regular expression (RegEx) Python module to verify the datetime format,
to filter the invalid datetime format and to ignore the duplicate valid entries and only one instance
of each valid datetime is saved to output file

"""
import re
from collections import Counter

# Regex for ISO 8601 format: YYYY-MM-DDThh:mm:ssTZD
datetime_pattern = re.compile(
    r"^\d{4}-\d{2}-\d{2}T"    # YYYY-MM-DDT
    r"\d{2}:\d{2}:\d{2}"      # hh:mm:ss
    r"(Z|[+-]\d{2}:\d{2})$"   # Z or ±hh:mm
)

#Check if the datetime string matches ISO 8601 format.
def is_valid_datetime(value: str) -> bool:
    return bool(datetime_pattern.match(value))

"""
    Reads a CSV file of datetime strings, validates them against ISO 8601, and writes:
    - unique valid datetimes to `valid_file`
    - duplicates to `duplicates_file`
    - invalid values to `invalid_file`
    
Args:
        input_file (str): Path to the CSV/text file containing datetime values.
        valid_file (str): Output path for unique valid datetimes.
        duplicates_file (str): Output path for duplicate valid datetimes.
        invalid_file (str): Output path for invalid datetime strings.
"""

def filter_datetimes(input_file: str, valid_file: str, duplicates_file: str, invalid_file: str):

    # Read all lines (strip whitespace and ignore empty lines)
    with open(input_file, "r", encoding="utf-8") as infile:
        lines = [] # Create an empty list to hold lines from the file

        # Loop through each line in the file
        # Remove any leading/trailing whitespace or newline characters
        # Only keep non-empty lines (skip blanks)
        for line in infile:
            stripped_line = line.strip()
            if stripped_line:
                lines.append(stripped_line)

    #Uses `collections.Counter` to efficiently count occurrences of each line.
    counts = Counter(lines)  # Count frequency of each datetime

    validlist = []
    duplicateslist = []
    invalidlist = []

    for datastr, count in counts.items():
        if is_valid_datetime(datastr):
            if count == 1:
                validlist.append(datastr)
            else:
                # first occurrence goes to valid, rest are duplicates
                validlist.append(datastr)
                duplicateslist.extend([datastr] * (count - 1))
        else:
            # invalid values (all occurrences, even if duplicated)
            invalidlist.extend([datastr] * count)

    # Write outputs
    with open(valid_file, "w", encoding="utf-8") as vf:
        for data in validlist:
            vf.write(data + "\n")

    with open(duplicates_file, "w", encoding="utf-8") as df:
        for data in duplicateslist:
            df.write(data + "\n")

    with open(invalid_file, "w", encoding="utf-8") as inf:
        for data in invalidlist:
            inf.write(data + "\n")

    # Print summary
    print(f"Total records processed: {len(lines)}")
    print(f"Unique valid values written: {len(validlist)} → {valid_file}")
    print(f"Duplicates written: {len(duplicateslist)} → {duplicates_file}")
    print(f"Invalid values written: {len(invalidlist)} → {invalid_file}")


if __name__ == "__main__":
    filter_datetimes(
        "datetime_inputfile.csv",
        "valid_dates.csv",
        "duplicates.csv",
        "invalid_dates.csv"
    )
