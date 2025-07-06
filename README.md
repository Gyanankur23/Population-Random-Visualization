# Population-Random-Visualization

A synthetic data generation and analysis project built to simulate large-scale population datasets using Python’s Faker module, followed by data cleaning, imputation, and visual storytelling.


# 📁 Project Structure

`
Population-Random-Visualization/
├── population_dataset.csv                # Raw synthetic dataset
├── cleanedpopulationdataset.csv        # Imputed and cleaned version
├── population_analysis.py                # Script for processing and plotting
├── data_outputs/                         # All generated CSVs and image charts
│   ├── head_preview.csv
│   ├── describe_stats.csv
│   ├── imputedpopulationdataset.csv
│   ├── X_input.csv
│   ├── Y_output.csv
│   ├── salary_boxplot.png
│   ├── age_histogram.png
│   ├── genderpiechart.png
│   ├── avgsalaryby_country.png
│   ├── correlation_heatmap.png
│   ├── devicebysubscription.png
│   ├── salary_outliers.csv
│   ├── sortedbyage.csv
│   ├── filteredseniorhigh_salary.csv
│   ├── selected_columns.csv
│   ├── meansalaryby_country.csv
│   └── finalcleaneddataset.csv
└── README.md
`

---

# ✨ Key Features

- 🔹 Synthetic population dataset (20,000 rows, 30 columns) using Faker
- 🔹 Data imputation with SimpleImputer
- 🔹 Statistical summaries and exportable outputs
- 🔹 Stunning data visualizations saved as PNG
- 🔹 Feature-label separation for modeling workflows
- 🔹 Outlier detection, filtering, and grouping logic

---

# 📊 Visual Outputs

## 🧓 Age Distribution Histogram
Visualizing the frequency distribution of age across the population.

!Age Histogram

---

## 👩‍🦰 Gender Proportion Pie Chart
Represents the gender ratio in the dataset.

!Gender Pie Chart

---

## 💰 Top 10 Countries by Average Salary
Highlights economic disparities based on geographic data.

!Average Salary by Country

---

## 🧮 Correlation Matrix Heatmap
Explores relationships between numeric features in the dataset.

!Correlation Heatmap

---

## 💻 Device Usage by Subscription Tier
Shows how various subscription groups access the service by device.

!Device by Subscription

---

## 📈 Salary Distribution Boxplot
Detects salary outliers and spread.

!Salary Boxplot

---

## 📂 CSV Snapshots

🧾 head_preview.csv
Initial 5 rows of the dataset for quick overview.

`csv
Age,Gender,Country,Annual Salary (USD),Subscription Type,Device Used
28,female,India,42000,Basic,Laptop
35,male,USA,81000,Premium,Mobile
...
`

---

## 📊 describe_stats.csv
Statistical summary of numeric columns.

`csv
              Age  Annual Salary (USD)
count  20000.00000        20000.000000
mean      36.47893        73245.823000
std       12.90834        29145.981200
...
`

---

## ⚗️ imputedpopulationdataset.csv
Cleaned version after mean imputation of missing values.

---

## 📦 Xinput.csv and Youtput.csv
Model-ready inputs and labels extracted from cleaned dataset.

---

## 📎 salary_outliers.csv
Subset of population earning above $180,000 annually.

---

## 🔍 filteredseniorhigh_salary.csv
Users above age 45 with annual salary above $100,000.

---

## 📊 meansalaryby_country.csv
Average salary grouped by country.

`csv
Country,Annual Salary (USD)
USA,84221.25
Germany,78910.50
India,41200.00
...
`

---

## 📃 selected_columns.csv
Only Age, Salary, and Device columns.

`csv
Age,Annual Salary (USD),Device Used
28,42000,Laptop
35,81000,Mobile
...
`

---

# ⚙️ Setup Instructions

Make sure you have Python 3.8+ installed. Install dependencies:

`bash
pip install pandas numpy matplotlib seaborn scikit-learn faker
`

# Run the script:

`bash
python population_analysis.py
`

---

# 📄 License

Released under the MIT License. Free to use, modify, and redistribute with proper credit.

---

# 👤 Author

Created and maintained by @Gyanankur23  
📧 Email: gyanankurcricket20@gmail.com

Love this project? Star it 🌟 — or fork it and build something even cooler!
`
