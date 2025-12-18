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
                print(" Highest:", high)

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


