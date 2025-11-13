import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("weather.csv")

# Display first few rows
print("\n✅ First few rows of data:")
print(data.head())

# Summary statistics
print("\n📊 Summary Statistics:")
print(data.describe())

# Check for missing values
print("\n🔍 Missing Values:")
print(data.isnull().sum())

# Average pollutant levels by city
avg_city_pollution = data.groupby('city')['pollutant_avg'].mean().sort_values(ascending=False).head(10)
print("\n🏙️ Top 10 Most Polluted Cities (by average pollutant level):")
print(avg_city_pollution)

# Plot top 10 polluted cities
plt.figure(figsize=(10,5))
sns.barplot(x=avg_city_pollution.values, y=avg_city_pollution.index, palette="Reds_r")
plt.title("Top 10 Most Polluted Cities")
plt.xlabel("Average Pollutant Level")
plt.ylabel("City")
plt.tight_layout()
plt.show()

# Pollutant variation by state
avg_state_pollution = data.groupby('state')['pollutant_avg'].mean().sort_values(ascending=False)
plt.figure(figsize=(10,5))
sns.barplot(x=avg_state_pollution.values, y=avg_state_pollution.index, palette="coolwarm")
plt.title("Average Pollution Levels by State")
plt.xlabel("Average Pollutant Level")
plt.ylabel("State")
plt.tight_layout()
plt.show()

# Find latest pollution readings
data['last_update'] = pd.to_datetime(data['last_update'], errors='coerce')
latest_data = data.sort_values('last_update', ascending=False).head(10)
print("\n🕓 Latest 10 Pollution Readings:")
print(latest_data[['city', 'pollutant_id', 'pollutant_avg', 'last_update']])

print("\n✅ Air Quality Analysis Completed Successfully!")
