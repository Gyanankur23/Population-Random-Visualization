import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
import os

# Create an output directory
output_dir = 'data_outputs'
os.makedirs(output_dir, exist_ok=True)

# 1️⃣ Load the main CSV
df = pd.read_csv('population_dataset.csv')
df.head().to_csv(f'{output_dir}/head_preview.csv', index=False)
df.describe().to_csv(f'{output_dir}/describe_stats.csv')

# 2️⃣ Handle missing values
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
df[numeric_cols] = imputer.fit_transform(df[numeric_cols])
df.to_csv(f'{output_dir}/imputed_population_dataset.csv', index=False)

# 3️⃣ Save input & output arrays
X = df.iloc[:, :-1].values
Y = df.iloc[:, 3].values
pd.DataFrame(X).to_csv(f'{output_dir}/X_input.csv', index=False)
pd.DataFrame(Y, columns=['Y_output']).to_csv(f'{output_dir}/Y_output.csv', index=False)

# 4️⃣ Visualize and save outlier chart
plt.figure(figsize=(10, 4))
sns.boxplot(x=df['Annual Salary (USD)'])
plt.title('Salary Distribution with Outliers')
plt.tight_layout()
plt.savefig(f'{output_dir}/salary_boxplot.png')
plt.close()

# 1️⃣ Histogram: Age Distribution
# Shows how your dataset's population is spread across different age groups
plt.figure(figsize=(8,5))
plt.hist(df['Age'], bins=20, color='teal', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('data_outputs/age_histogram.png')
plt.close()

# 2️⃣ Pie Chart: Gender Proportion
# Visualizes the percentage of each gender in the dataset
plt.figure(figsize=(6,6))
df['Gender'].value_counts().plot.pie(
    autopct='%1.1f%%',
    startangle=140,
    colors=['gold', 'skyblue', 'lightcoral']
)
plt.ylabel('')
plt.title('Gender Distribution')
plt.tight_layout()
plt.savefig('data_outputs/gender_pie_chart.png')
plt.close()

# 3️⃣ Bar Chart: Average Salary by Country (Top 10)
# Helps compare average annual salary across countries
salary_country = df.groupby('Country')['Annual Salary (USD)'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,5))
salary_country.plot(kind='bar', color='darkgreen')
plt.title('Top 10 Countries by Average Salary')
plt.xlabel('Country')
plt.ylabel('Avg Salary (USD)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('data_outputs/avg_salary_by_country.png')
plt.close()

# 4️⃣ Heatmap: Correlation Matrix of Numeric Features
# Reveals statistical relationships among continuous variables
plt.figure(figsize=(12,8))
sns.heatmap(df.select_dtypes(include=[np.number]).corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.savefig('data_outputs/correlation_heatmap.png')
plt.close()

# 5️⃣ Stacked Bar Chart: Device Usage by Subscription Tier
# Compares how different user tiers access the platform by device type
device_subs = pd.crosstab(df['Subscription Type'], df['Device Used'])
device_subs.plot(
    kind='bar',
    stacked=True,
    figsize=(10,6),
    colormap='tab20'
)
plt.title('Device Usage by Subscription Type')
plt.xlabel('Subscription Type')
plt.ylabel('User Count')
plt.legend(title='Device Used')
plt.tight_layout()
plt.savefig('data_outputs/device_by_subscription.png')
plt.close()

# 5️⃣ Save outlier index information
outliers = np.where(df['Annual Salary (USD)'] > 180000)
outlier_df = df.iloc[outliers]
outlier_df.to_csv(f'{output_dir}/salary_outliers.csv', index=False)

# 6️⃣ Sorting
sorted_df = df.sort_values(by='Age')
sorted_df.to_csv(f'{output_dir}/sorted_by_age.csv', index=False)

# 7️⃣ Filtering rows
filtered_df = df.query('Age > 45 and `Annual Salary (USD)` > 100000')
filtered_df.to_csv(f'{output_dir}/filtered_senior_high_salary.csv', index=False)

# 8️⃣ Filtering columns
selected_columns = df[['Age', 'Annual Salary (USD)', 'Device Used']]
selected_columns.to_csv(f'{output_dir}/selected_columns.csv', index=False)

# 9️⃣ Grouping data
grouped_salary = df.groupby('Country')['Annual Salary (USD)'].mean()
grouped_salary.to_csv(f'{output_dir}/mean_salary_by_country.csv')

# 🔟 Save final clean dataset
df.to_csv(f'{output_dir}/final_cleaned_dataset.csv', index=False)

print("✅ All outputs saved to the 'data_outputs' directory.")