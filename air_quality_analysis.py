import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Airquality.csv")

# Display first few rows
print("Preview of dataset:")
print(df.head(), "\n")

# Basic info
print("Dataset Info:")
print(df.info(), "\n")

# Check for missing values
print("Missing Values:\n", df.isnull().sum(), "\n")

# Drop rows with missing essential data
df.dropna(subset=["pollutant_avg"], inplace=True)

# Convert date column to datetime
df['last_update'] = pd.to_datetime(df['last_update'], errors='coerce')

# Summary statistics
print("Summary Statistics:")
print(df.describe(), "\n")

# --- Analysis Section ---

# Top 10 most polluted cities based on average pollutant value
top_cities = df.groupby("city")["pollutant_avg"].mean().sort_values(ascending=False).head(10)
print("Top 10 Most Polluted Cities:\n", top_cities, "\n")

# Average pollutant levels by country
avg_by_country = df.groupby("country")["pollutant_avg"].mean().sort_values(ascending=False)
print("Average Pollutant Levels by Country:\n", avg_by_country, "\n")

# Average pollutant levels by state
avg_by_state = df.groupby("state")["pollutant_avg"].mean().sort_values(ascending=False)
print("Average Pollutant Levels by State:\n", avg_by_state.head(10), "\n")

# --- Visualization Section ---

plt.figure(figsize=(10, 6))
sns.barplot(x=top_cities.values, y=top_cities.index, palette="Reds_r")
plt.title("Top 10 Most Polluted Cities")
plt.xlabel("Average Pollutant Level")
plt.ylabel("City")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x=avg_by_country.values[:10], y=avg_by_country.index[:10], palette="coolwarm")
plt.title("Average Pollutant Levels by Country")
plt.xlabel("Average Pollutant")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

# Time-based analysis (optional)
df_sorted = df.sort_values("last_update")
plt.figure(figsize=(10, 5))
sns.lineplot(data=df_sorted, x="last_update", y="pollutant_avg", color="green")
plt.title("Pollutant Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Average Pollutant Level")
plt.tight_layout()
plt.show()

print("✅ Analysis Complete! Charts displayed successfully.")
