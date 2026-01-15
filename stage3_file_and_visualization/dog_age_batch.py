class Dog:
    def __init__(self, dog_Age):
        self.dog_Age = dog_Age
        self.human_Age = None

    def human_age_calc(self):
        if 0 <= self.dog_Age <= 1:
            self.human_Age = self.dog_Age * 15
        elif 1 < self.dog_Age <= 5:
            self.human_Age = self.dog_Age * 11 + 2
        elif 5 < self.dog_Age <= 15:
            self.human_Age = self.dog_Age * 8 - 3
        else:
            raise ValueError("The calculator only supports ages 0–15.")
        return self.human_Age

    def dog_class(self):
        if self.human_Age is None:
            raise ValueError("Run human_age_calc() first!")

        if 0 <= self.human_Age < 20:
            self.ageGP = "Young"
        elif 20 <= self.human_Age <= 39:
            self.ageGP = "Adult"
        else:
            self.ageGP = "Senior"

    def resultclass(self):
        return {"dog_Age": self.dog_Age, "human_Age": self.human_Age, "ageGP": self.ageGP}


# Read dog age from file
results = []
with open("dog_ages.txt", "r") as ages:
    for line in ages:
        try:
            dog = Dog(float(line.strip()))
            dog.human_age_calc()
            dog.dog_class()
            results.append(dog.resultclass())
        except ValueError:
            print(f"Skipping invalid entry: {line}")

# View results
for r in results:
    print(r)

# ----- BAR CHART -----
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
# Extract data
dog_ages = [r["dog_Age"] for r in results]
human_ages = [r["human_Age"] for r in results]
age_groups = [r["ageGP"] for r in results]

# Color mapping
color_map = {"Young": "green", "Adult": "orange", "Senior": "red"}
bar_colors = [color_map[group] for group in age_groups]

# Create bar chart
plt.figure()
bars = plt.bar(dog_ages, human_ages, color=bar_colors)

# Label each bar with age group
for bar, group in zip(bars, age_groups):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), group, ha='center', va='bottom')

# Titles and labels
plt.title("Dog Age vs Human Age")
plt.xlabel("Dog Age (years)")
plt.ylabel("Equivalent Human Age (years)")

# Legend
legend_elements = [Patch(facecolor="green", label="Young"), Patch(facecolor="orange", label="Adult"), Patch(facecolor="red", label="Senior")]
plt.legend(handles=legend_elements)

# Show chart
plt.show()
