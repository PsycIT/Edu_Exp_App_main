import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Create a DataFrame from the provided data
df = pd.read_csv('output/population_30p.csv', delimiter=',')

# Calculate the average 'Immersion score'
average_score = df['Immersion score'].mean()

# Calculate the average 'Immersion score'
average_score = df['Immersion score'].mean()

# Set seaborn style
sns.set(style="whitegrid")

# Plotting with seaborn
plt.figure(figsize=(12, 8))

# Assign colors based on the comparison with the average score
colors = ['blue' if score < average_score else 'red' for score in df['Immersion score']]
sns.histplot(data=df, x='Immersion score', bins=len(df['Immersion score'].unique()), palette=colors, kde=True)

# Add a vertical line at the average 'Immersion score'
plt.axvline(x=average_score, color='black', linestyle='--', linewidth=2, label=f'Average Score: {average_score:.2f}')

# Add labels and title
plt.xlabel('Immersion score')
plt.ylabel('Frequency')
plt.title('Frequency Table of Immersion Scores')
plt.legend()

plt.show()