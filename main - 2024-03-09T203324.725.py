import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load bat species data
bat_data_url = "https://example.com/bat_species_data.csv"  # Replace with actual data URL
bat_species_data = pd.read_csv(bat_data_url)

# Basic exploration of the data
print("First few rows of bat species data:")
print(bat_species_data.head())

# Plotting species distribution
plt.figure(figsize=(10, 6))
sns.scatterplot(data=bat_species_data, x='Longitude', y='Latitude', hue='Habitat', palette='viridis', s=100)
plt.title('Distribution of Bat Species')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend(title='Habitat')
plt.grid(True)
plt.show()

# Analyzing species diversity
habitat_counts = bat_species_data['Habitat'].value_counts()
print("\nSpecies count by habitat:")
print(habitat_counts)

# Plotting habitat distribution
plt.figure(figsize=(8, 6))
habitat_counts.plot(kind='bar', color='skyblue')
plt.title('Bat Species Distribution by Habitat')
plt.xlabel('Habitat')
plt.ylabel('Species Count')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
