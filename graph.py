import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV data
# Replace 'your_file_path_here.csv' with the actual path of your CSV file
url = 'your_file_path_here.csv'
df = pd.read_csv(url)

# Display basic information about the dataset
print(df.info())

# Visualize the data
fig, axes = plt.subplots(3, 2, figsize=(15, 18))

# Scatter plot: Age vs Decile Score colored by Race
sns.scatterplot(data=df, x='age', y='decile_score', hue='race', ax=axes[0, 0])
axes[0, 0].set_title('Scatter Plot: Age vs Decile Score (Colored by Race)')

# Boxplot: Decile Score grouped by Race
sns.boxplot(data=df, x='race', y='decile_score', ax=axes[0, 1])
axes[0, 1].set_title('Boxplot: Decile Score by Race')

# Countplot: Age Category
sns.countplot(data=df, x='age_cat', ax=axes[1, 0])
axes[1, 0].set_title('Countplot: Age Category')

# Countplot: Race
sns.countplot(data=df, x='race', ax=axes[1, 1])
axes[1, 1].set_title('Countplot: Race')

# Countplot: Recidivism
sns.countplot(data=df, x='is_recid', ax=axes[2, 0])
axes[2, 0].set_title('Countplot: Recidivism')

# Countplot: Violent Recidivism
sns.countplot(data=df, x='is_violent_recid', ax=axes[2, 1])
axes[2, 1].set_title('Countplot: Violent Recidivism')

# Adjust layout and display the plots
plt.tight_layout()
plt.show()

