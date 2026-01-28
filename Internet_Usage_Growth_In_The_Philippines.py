print("------------------------------------------------------------------")
print("All Rights Reserved 2026 | Group 4")
print("Date of Completion:January 29, 2026")
print("Assignment 01:Research-Based Data Visualization Using Python")
print("------------------------------------------------------------------\n")
import pandas as pd
import matplotlib.pyplot as plt

data = {"Year": [2015,2016,2017,2018,2019,2020,2021,2022,2023],
        "Internet Usage (%)": [37,39,42,44,43,54,67,75,84]}

df = pd.DataFrame(data)


#To show the internet usage growth in the philippines over time using line chart
plt.figure("Line Chart")
plt.plot(df["Year"], df["Internet Usage (%)"], marker='o')
plt.title("Internet Usage Growth in the Philippines")
plt.xlabel("Year")
plt.ylabel("Internet Usage (%)")
plt.grid(True)
plt.show()

#This line of code shows how internet usage changes over time using bar chart.
plt.figure("Bar Chart")
plt.bar(df["Year"], df["Internet Usage (%)"])
plt.title("Internet Usage Growth in the Philippines)")
plt.xlabel("Year")
plt.ylabel("Internet Usage (%)")
plt.xticks(df["Year"], rotation=45)
plt.tight_layout()
plt.show()

print("\n------------------------------------------------------------------")