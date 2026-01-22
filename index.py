# Import Library
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="darkgrid")
plt.style.use('dark_background')

# Load Dataset
df = pd.read_csv("AI_Companies.csv")

# Preview & Info
print("First 5 Rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe(include="all"))

print("\nMissing Values:")
print(df.isnull().sum())

# Data Cleaning
df.drop(columns=["Unnamed: 7"], inplace=True)
df.fillna("Unknown", inplace=True)

# Save All Plots 
output_folder = "Plot Images"
os.makedirs(output_folder, exist_ok=True)

def save_plot(fig, filename):
    fig.tight_layout()
    fig.savefig(os.path.join(output_folder, filename))

# Plot 1: Companies by Employee Size
fig = plt.figure()
sns.countplot(y="Number of Employees", data=df, color="purple")
plt.title("AI Companies by Number of Employees")
plt.xlabel("Count")
plt.ylabel("Employee Range")
save_plot(fig, "Plot1.png")
plt.show()

# Plot 2: Companies by Location (Top 10)
fig = plt.figure(figsize=(10,6))
sns.countplot(
    y="Location",
    data=df,
    order=df["Location"].value_counts().head(10).index,
    color="orange"
)
plt.title("Top 10 Locations with AI Companies", fontsize=14, fontweight='bold')
plt.xlabel("Count")
plt.ylabel("Location")
save_plot(fig, "Plot2.png")
plt.show()

# Plot 3: AI Service Focus Distribution
fig = plt.figure(figsize=(10,6))
sns.countplot(y="Percent AI Service Focus", data=df, color="green")
plt.title("AI Service Focus Distribution", fontsize=14, fontweight='bold')
plt.xlabel("Count")
plt.ylabel("AI Service Focus (%)")
save_plot(fig, "Plot3.png")
plt.show()

# Plot 4: Average Hourly Rate Distribution
fig = plt.figure()
sns.histplot(df["Average Hourly Rate"], color='blue')
plt.title("Average Hourly Rate Distribution")
plt.xlabel("Hourly Rate")
plt.ylabel("Frequency")
save_plot(fig, "Plot4.png")
plt.show()

# Plot 5: Project Size vs Employees
fig = plt.figure()
sns.countplot(x="Minimum Project Size", hue="Number of Employees", data=df)
plt.title("Project Size vs Employee Count")
plt.xlabel("Minimum Project Size")
plt.ylabel("Count")
save_plot(fig, "Plot5.png")
plt.show()

# ------------------------------------------- Numpy Analysis ------------------------------------------------
employee_counts = df["Number of Employees"].value_counts().values
print("\n--- Employee Distribution Stats ---")
print("Max Companies in a Category:", np.max(employee_counts))
print("Min Companies in a Category:", np.min(employee_counts))
print("Average Companies:", np.mean(employee_counts))

# ----------------------------------------- Key Insights from EDA ----------------------------------------------
print("\n--- Key Insights from EDA ---")
print("• Most AI companies are small to mid-sized")
print("• AI companies are concentrated in specific locations")
print("• Many firms focus partially on AI services")
print("• Pricing and project size vary widely")
print("• AI service industry is diverse and growing")
