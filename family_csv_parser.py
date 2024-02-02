import csv
import sys
import os

def parse_csv(file_path):
    parsed_data = []

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)

        # Skip the first row as it contains column headers
        next(reader, None)

        for row in reader:
            # Remove leading and trailing whitespaces for each column
            cleaned_row = [col.strip() for col in row]

            # Check if the row is empty
            if any(cleaned_row):
                entry = {
                    "First_Name": cleaned_row[0] if len(cleaned_row) > 0 else '',
                    "Middle_Name": cleaned_row[1] if len(cleaned_row) > 1 else '',
                    "Last_Name": cleaned_row[2] if len(cleaned_row) > 2 else '',
                    "Mailing_Address": cleaned_row[3] if len(cleaned_row) > 3 else '',
                    "City": cleaned_row[4] if len(cleaned_row) > 4 else '',
                    "State": cleaned_row[5] if len(cleaned_row) > 5 else '',
                    "Zip": cleaned_row[6] if len(cleaned_row) > 6 else '',
                    "Phone": cleaned_row[7] if len(cleaned_row) > 7 else '',
                    "Birthdate": cleaned_row[8] if len(cleaned_row) > 8 else '',
                    "Email": cleaned_row[9] if len(cleaned_row) > 9 else '',
                    "Deathdate": cleaned_row[10] if len(cleaned_row) > 10 else ''
                }
                parsed_data.append(entry)

    return parsed_data

def write_to_csv(input_file, data):
    # Construct the output file path by modifying the input file name
    output_file = os.path.splitext(input_file)[0] + "_parsed.csv"

    with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            "First_Name", "Middle_Name", "Last_Name",
            "Mailing_Address", "City", "State", "Zip",
            "Phone", "Birthdate", "Email", "Deathdate"
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header
        writer.writeheader()

        # Write data
        for entry in data:
            writer.writerow(entry)

    return output_file

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file_path>")
        sys.exit(1)

    input_file_path = sys.argv[1]

    parsed_data = parse_csv(input_file_path)

    # Display the parsed data
    for entry in parsed_data:
        print("\nEntry:")
        for key, value in entry.items():
            print(f"{key}: {value}")

    # Write the parsed data to a new CSV file in the same directory
    output_file_path = write_to_csv(input_file_path, parsed_data)

    print(f"\nParsed data has been written to {output_file_path}")
