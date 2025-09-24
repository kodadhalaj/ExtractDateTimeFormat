# Program Name: Extract and Filter DateTime Formats

This repository contains **Python scripts** for reading date-time values from files, validating their format, and writing unique, valid entries to new files.  

The primary focus is on extracting and processing date-times that adhere strictly to the **ISO 8601 format** (`YYYY-MM-DDThh:mm:ssTZD`).  
Invalid and duplicate entries are filtered out to facilitate cleaner downstream data analysis.
**Note:** This program does notperform semantic validation of the data-time value. In other words, the date-time value "9999-02-31T12:34:56+12:34" 
can be considered valid by your program even though February 31, 9999 is not a legitimate date

---

## Features 
- ✅ Read date-time values from input files (plain text or CSV).  
- ✅ Validate each value against the **ISO 8601** standard, including time zone designators.  
- ✅ Filter and save unique, valid values to a new output file.  
- ✅ (Optional) Identify and export lists of **duplicate** and **invalid** values for auditing.  

---

## How to Use the Program

1. Clone the repository:
   ```bash
   git clone https://github.com/kodadhalaj/ExtractDateTimeFormat.git
  
2. Navigate to the repository:
   ```bash
   cd ExtractDateTimeFormat/FileHandlingDateTime/FileHandlingReadWrite

3.	Prepare your input file with date-time values
    - Run **random_inputcsvfile.py** script to generate a sample input file **(datetime_inputfile.csv)**
  
4.	Extract and filter unique valid values:
    - Run **datetime_process_validdata.py** to generate an output file **(datetime_validoutput.csv)** containing only unique, valid date and time values.
6.	(Optional) Extract all categories:
    - Run **datetime_process_data_all.py** to generate three separate output files:
     - i.	unique valid date and time values **(valid_dates.csv)**
     - ii.	duplicate date and time values **(duplicates.csv)**
     - iii.	invalid date and time values **invalid_dates.csv)**


✅ Valid DateTime Values
- 2023-05-17T10:15:30Z
- 9999-02-31T07:45:15+05:30
- 2001-06-26T01:32:11-04:45

❌ Invalid DateTime Values
- 01-01-2024 12:00:00
- 2024/01/01 12:00:00
- 2024-01-01
- INVALID DATE TIME
