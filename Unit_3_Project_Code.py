import matplotlib.pyplot as plt
# Imports matplotlib which allows me to create graphs in the program
def average(numbers):
    return sum(numbers) / len(numbers)
# This user created function calculates average by adding all numbers and dividing by how many there are

def highest_score(numbers):
    return max(numbers)
# This function gives the highest value using pythons in built max() function

# Below is a OOP
class ScoreTracker:
    def __init__(self):
        # This constructor runs when the ScoreTracker object is created

        # This is an empty dictionary where the key will be the subject name and value is list of scores for that subject
        self.data = {}

    def add_score(self, subject, score):
        # This method adds a score to the dictionary

        # Changes subject to title case
        subject = subject.title()

        # Checks if subject is not in the dictionary, and if so, it makes a new empty list for it by adding it as a new key.
        if subject not in self.data:
            self.data[subject] = []

        # Adds the score to the subject key
        self.data[subject].append(score)

    def show_summary(self):
        # This method prints summary

        # If the dictionary is empty, nothing to show.
        if not self.data:
            print("No scores entered yet.")
            return

        print("\n--- Summary ---")

        # Loop through each item in teh dictionary
        for item in self.data.items():
            subject = item[0]  # Subject name (key)
            scores = item[1]   # List of scores (value)

            # Calculate average and highest score using functions
            avg = average(scores)
            high = highest_score(scores)

            # Print the results
            print(subject)
            print("Scores:", scores)
            print("Average:", round(avg,2))
            print("Highest:", high)

    def plot(self):
        # This method creates a bar graph with average scores

       # Create a list of subject names
        subjects = list(self.data.keys())

        # Create a list to store average scores
        averages = []

        # Loops through every subject and calculates average
        for subject in subjects:
            averages.append(average(self.data[subject]))

        # Creates bar graph
        plt.bar(subjects, averages)
        plt.xlabel("Subject")
        plt.ylabel("Average score")
        plt.title("Average score over all subjects")
        plt.show()

# Creates an object from ScoreTracker class
tracker = ScoreTracker()

print("Welcome to the Quiz Score Tracker")

# Repeat the menu until option 4 is selected (user wants to exit)
while True:
    print("\nMenu")
    print("1. Add a score")
    print("2. View summary")
    print("3. Plot graph")
    print("4. Exit")

    # User's menu choice
    choice = input("Enter your choice: ")

    # Option 1: Add a score
    if choice == "1":
        user_subject = input("Enter subject name: ")

        # Try to conver the input into a number
        try:
            user_score = float(input("Enter score (0-100): "))

            # Check if the score is within the range
            if 0 <= user_score <= 100:
                tracker.add_score(user_subject, user_score)
                print("Score added successfully.")
            else:
                print("Score must be between 0 and 100.")

        # Takes care of invalid numeric input
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Option 2: Show summary, calls on corresponding method
    elif choice == "2":
        tracker.show_summary()

    # Option 3: Plot graph, calls on corresponding method
    elif choice == "3":
        if tracker.data:
            tracker.plot()
        else:
            print("No data available to plot.")
    # Option 4: Exit program
    elif choice == "4":
        print("Thank you for using the program.")
        break
    # Takes care of invalid menu choice
    else:
        print("Invalid option. Please choose 1-4")