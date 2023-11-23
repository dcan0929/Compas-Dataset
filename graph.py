import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import os
from flask import Flask, render_template

app = Flask(__name__)

# Load the CSV data
url = 'resources/cox-violent-parsed_filt_usable.csv'
df = pd.read_csv(url)

# Directory to save images
img_dir = 'static/images'

# Check if the directory exists, create it if not
if not os.path.exists(img_dir):
    os.makedirs(img_dir)

# Function to analyze data and save plots as images
def analyze_and_save_plots():
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

    # Adjust layout
    plt.tight_layout()

    # Save the plot as an image
    img_path = os.path.join('static/images', 'analysis_plot.png')
    plt.savefig(img_path)
    plt.close()

    return img_path

# Route to display the plot on the web page
@app.route('/')
def show_plot():
    # Analyze data and save plots as images
    img_path = analyze_and_save_plots()

    # Render the template with the image path
    return render_template('index.html', img_path=img_path)

if __name__ == '__main__':
    app.run(debug=True)
