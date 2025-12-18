import matplotlib.pyplot as plt

def average(numbers):
    return sum(numbers) / len(numbers)

def highest_score(numbers):
    return max(numbers)


class ScoreTracker:
    def __init__(self):
        self.data = {}

    def add_score(self, subject, score):
        subject = subject.title()

        if subject not in self.data:
            self.data[subject] = []

        self.data[subject].append(score)

    def show_summary(self):
        if not self.data:
            print("No scores entered yet.")
            return

        print("\n--- Summary ---")
        for item in self.data.items():
            subject = item[0]
            scores = item[1]

            avg = average(scores)
            high = highest_score(scores)

            print(subject)
            print("Scores:", scores)
            print("Average:", round(avg,2))
            print("Highest:", high)

    def plot(self):
        subjects = list(self.data.keys())
        averages = []

        for subject in subjects:
            averages.append(average(self.data[subject]))

        plt.bar(subjects, averages)
        plt.xlabel("Subject")
        plt.ylabel("Average score")
        plt.title("Average score over all subjects")
        plt.show()


tracker = ScoreTracker()

print("Welcome to teh Quiz Score Tracker")

while True:
    print("\nMenu")
    print("1. Add a score")
    print("2. View summary")
    print("3. Plot graph")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        subject = input("Enter subject name: ")

        try:
            score = float(input("Enter score (0-100): "))

            if 0 <= score <= 100:
                tracker.add_score(subject, score)
                print("Score added successfully.")
            else:
                print("Score must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == "2":
        tracker.show_summary()

    elif choice == "3":
        if tracker.data:
            tracker.plot()
        else:
            print("No data available to plot.")

    elif choice == "4":
        print("Thank you for using the program.")
        break

    else:
        print("Invalid option. Please choose 1-4")