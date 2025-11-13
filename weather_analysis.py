import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("weather.csv")

# Convert Date column to datetime format
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

# Display first few rows
print("\n✅ First few rows of data:")
print(data.head())

# Summary statistics
print("\n📊 Summary Statistics:")
print(data.describe())

# Check for missing values
print("\n🔍 Missing Values:")
print(data.isnull().sum())

# Key Metrics
avg_temp = data['Temperature'].mean()
max_temp = data['Temperature'].max()
min_temp = data['Temperature'].min()
rainy_days = data[data['Rainfall'] > 0].shape[0]

print(f"\n🌡 Average Temperature: {avg_temp:.1f}°C")
print(f"🔥 Maximum Temperature: {max_temp}°C")
print(f"❄️ Minimum Temperature: {min_temp}°C")
print(f"🌧 Total Rainy Days: {rainy_days}")

# Temperature Trend Plot
plt.figure(figsize=(10,5))
sns.lineplot(x='Date', y='Temperature', data=data, marker='o', color='orange')
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Humidity and Rainfall Plot
fig, ax1 = plt.subplots(figsize=(10,5))
ax1.set_xlabel("Date")
ax1.set_ylabel("Humidity (%)", color='blue')
ax1.plot(data['Date'], data['Humidity'], color='blue', marker='o', label='Humidity')

ax2 = ax1.twinx()
ax2.set_ylabel("Rainfall (mm)", color='green')
ax2.bar(data['Date'], data['Rainfall'], color='green', alpha=0.4, label='Rainfall')

plt.title("Humidity and Rainfall Over Time")
plt.tight_layout()
plt.show()

print("\n✅ Weather analysis completed successfully!")
