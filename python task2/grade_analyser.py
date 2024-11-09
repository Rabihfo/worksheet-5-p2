import csv

# Classification function based on grade
def classify(average_grade):
    if average_grade >= 70:
        return "1"
    elif average_grade >= 60:
        return "2:1"
    elif average_grade >= 50:
        return "2:2"
    elif average_grade >= 40:
        return "3"
    else:
        return "F"

# Main function to process student data
def process_student_file():
    # Ask for the filename
    input_filename = input("Enter the student data filename (including .csv extension): ")
    output_filename = input_filename + "_out.csv"

    # Open the input file and prepare the output file
    with open(input_filename, 'r') as infile, open(output_filename, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Process each row in the input file
        for row in reader:
            student_id = row[0]  # The first column is the student ID
            grades = [int(grade) for grade in row[1:] if grade]  # Convert non-empty grades to integers

            # Calculate the average grade
            if grades:
                average_grade = sum(grades) / len(grades)
                classification = classify(average_grade)
                
                # Write to output in the specified format
                writer.writerow([student_id, f"{average_grade:.2f}", classification])

    print(f"Output file generated: {output_filename}")

# Run the function
process_student_file()
