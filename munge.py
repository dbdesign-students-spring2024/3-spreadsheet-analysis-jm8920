# Place your code to clean up the data file below.

import csv

input_file_path = 'data/raw_data.csv'
output_file_path = 'data/clean_data.csv'

# Open and read the input file
with open(input_file_path, mode='r', newline='') as infile:
    reader = csv.reader(infile)
    rows = [row for row in reader]

# Write to the output file
with open(output_file_path, mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    
    # Add new column titles
    header = rows[0]
    header.extend([
        '# of students not fully vaccinated', 
        '% of students not fully vaccinated', 
        '# of students never vaccinated', 
        '% of students never vaccinated'
    ])
    writer.writerow(header)
    
    for row in rows[1:]:
        # Extract values
        student = int(row[1])  
        stu_onedose = int(row[2]) 
        stu_fully = int(row[4])
        
        # Calculate new values
        not_fully = student - stu_fully
        never_vaccinated = student - stu_onedose
        percent_not_fully = (not_fully / student) if student > 0 else 0
        percent_never = (never_vaccinated / student) if student > 0 else 0
        
        # Format percentages to three decimal places
        percent_not_fully_formatted = f"{percent_not_fully:.3f}"
        percent_never_formatted = f"{percent_never:.3f}"
        
        # Extend the row
        row.extend([
            not_fully, 
            percent_not_fully_formatted, 
            never_vaccinated, 
            percent_never_formatted
        ])

        # Store the clean data
        writer.writerow(row)
