"""
Module Description:
This program reads large list of datetime values from an input file, filters out duplicates and
invalid entries based on the ISO 8601 datetime format (YYYY-MM-DDThh:mm:ssTZD), and writes only the
unique valid datetime values to an output file.

The filtering is performed using a regular expression (RegEx) Python module to verify the datetime format,
to filter the invalid datetime format and to ignore the duplicate valid entries and only one instance
of each valid datetime is saved to output file
"""

#Python’s regular expressions module
import re

#: Compiled regex pattern for validating ISO 8601 datetime strings.
#: The format enforced is: YYYY-MM-DDThh:mm:ssTZD
datetime_pattern = re.compile(
    r"^\d{4}-\d{2}-\d{2}T"    # YYYY-MM-DDT
    r"\d{2}:\d{2}:\d{2}"      # hh:mm:ss
    r"(Z|[+-]\d{2}:\d{2})$"   # Z or ±hh:mm
)

# Check if given value is ISO-8601format ( YYYY-MM-DDThh:mm:ssTZD Where TZD = Z or ±hh:mm )
def is_valid_datetime(value: str) -> bool:
    return bool(datetime_pattern.match(value))

"""
Args:
        input_file (str): Path to the input file containing datetime strings.
        output_file (str): Path to the output file where valid, unique datetimes will be saved.
"""
def filter_datetimes(input_file: str, output_file: str):
    uniquedata_set = set()   # to track unique values
    validdata_list = []     # to store list of valid values

    # Read input file
    with open(input_file, "r", encoding="utf-8") as infile:
        lines = infile.readlines()   # read all lines once
        linecount = len(lines)-1     # count total lines to display in output

        for line in lines:           # iterate over the same lines
            datetime_str = line.strip()
            if datetime_str and is_valid_datetime(datetime_str) and datetime_str not in uniquedata_set:
                uniquedata_set.add(datetime_str)
                validdata_list.append(datetime_str)

    # Write valid, unique values to output file
    with open(output_file, "w", encoding="utf-8") as outfile:
        for datetime_str in validdata_list:
            outfile.write(datetime_str + "\n")

    print(f"Total number of datetime records: {linecount}")
    print(f"Filtering complete. {len(validdata_list)} valid unique values written to {output_file}")

if __name__ == "__main__":
    filter_datetimes("datetime_inputfile.csv", "datetime_validoutput.csv")

