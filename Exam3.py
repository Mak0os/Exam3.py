# Program Name: Exam3.py
# Course: IT1114/Section XXX
# Student Name: Daniel Urdaneta
# Assignment Number: Lab#
# Due Date: 12/4/2024
# Purpose: This program reads diving event data from an input file
# List specific resources used to complete the assignment: Python documentation, course notes

# Function to calculate the final dive score
def calculate_dive_score(dd, scores):
    # Sort the scores to remove the highest and lowest
    scores.sort()
    scores = scores[1:-1]  # Remove the lowest and highest scores
    average_score = sum(scores) / len(scores)  # Calculate the average of the remaining scores
    final_score = average_score * dd  # Multiply by the degree of difficulty
    return round(final_score, 1)  # Return the score rounded to one decimal place

def main():
    try:
        # Open the input file
        with open("input.txt", "r") as file:
            lines = file.readlines()

        # Print headers for output
        print("Name\tDD\tScore")

        # Process each line in the file
        for line in lines:
            parts = line.strip().split("\t")  # Split the line by tab
            name = parts[0]  # Diver's name
            dd = float(parts[1])  # Degree of difficulty
            scores = list(map(float, parts[2:]))  # Convert score strings to floats

            # Calculate the dive score
            final_score = calculate_dive_score(dd, scores)

            # Print the result
            print(f"{name}\t{dd}\t{final_score}")

    except FileNotFoundError:
        print("Error: The file 'input.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point of the program
if __name__ == "__main__":
    main()
