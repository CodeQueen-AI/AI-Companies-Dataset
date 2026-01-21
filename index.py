# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# --------------------------------------------- Data Analysis----------------------------------------------
# Load Dataset
df = pd.read_csv("AI_Companies.csv")

# Preview
print("First 5 Rows:")
print(df.head())

# Info
print("Dataset Information:")
df.info()

# Stats
print("Statistical Summary:")
print(df.describe(include="all"))

# Missing Values
print("Missing Values:")
print(df.isnull().sum())

# Data Cleaning
df.drop(columns=["Unnamed: 7"], inplace=True)
df.fillna("Unknown", inplace=True)

# ------------------------------------------Data Visualization----------------------------------------------

# # Plot 1: Companies by Employee Size
# plt.figure()
# sns.countplot(y="Number of Employees", data=df, color="purple" )
# plt.title("AI Companies by Number of Employees")
# plt.xlabel("Count")
# plt.ylabel("Employee Range")
# plt.show()

# Plot 2: Companies by Location (Top 10)
# plt.figure(figsize=(10,6)) 
# sns.countplot(y="Location",data=df,order=df["Location"].value_counts().head(10).index,color="orange")
# plt.title("Top 10 Locations with AI Companies", fontsize=14, fontweight='bold')
# plt.xlabel("Count")
# plt.ylabel("Location")
# plt.tight_layout() 
# plt.show()


# # Plot 3: AI Service Focus Distribution
# plt.figure()
# sns.countplot(y="Percent AI Service Focus", data=df)
# plt.title("AI Service Focus Distribution")
# plt.xlabel("Count")
# plt.ylabel("AI Service Focus (%)")
# plt.show()

# # Plot 4: Average Hourly Rate Distribution
# plt.figure()
# sns.histplot(df["Average Hourly Rate"])
# plt.title("Average Hourly Rate Distribution")
# plt.xlabel("Hourly Rate")
# plt.ylabel("Frequency")
# plt.show()

# # Plot 5: Project Size vs Employees
# plt.figure()
# sns.countplot(
#     x="Minimum Project Size",
#     hue="Number of Employees",
#     data=df
# )
# plt.title("Project Size vs Employee Count")
# plt.xlabel("Minimum Project Size")
# plt.ylabel("Count")
# plt.show()

# # ===============================
# # -------- NUMPY ANALYSIS --------
# # ===============================
# employee_counts = df["Number of Employees"].value_counts().values

# print("\n--- Employee Distribution Stats ---")
# print("Max Companies in a Category:", np.max(employee_counts))
# print("Min Companies in a Category:", np.min(employee_counts))
# print("Average Companies:", np.mean(employee_counts))

# # ===============================
# # Final Insights
# # ===============================
# print("\n--- Key Insights from EDA ---")
# print("• Most AI companies are small to mid-sized")
# print("• AI companies are concentrated in specific locations")
# print("• Many firms focus partially on AI services")
# print("• Pricing and project size vary widely")
# print("• AI service industry is diverse and growing")
