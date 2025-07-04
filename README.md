# Population-Random-Visualization

A synthetic data generation and analysis project built to simulate large-scale population datasets for preprocessing, visualization, and machine learning workflows.

---

## 📁 Project Structure


Population-Random-Visualization/ ├── population_dataset.csv                # Raw synthetic dataset (20,000 rows, 30 columns) ├── cleaned_population_dataset.csv        # Imputed and cleaned version of the dataset ├── population_analysis.py                # Main script for data loading, preprocessing, visualizations ├── data_outputs/                         # Folder for all generated CSVs and image charts │   ├── age_histogram.png │   ├── gender_pie_chart.png │   ├── avg_salary_by_country.png │   ├── correlation_heatmap.png │   ├── device_by_subscription.png │   ├── head_preview.csv │   ├── describe_stats.csv │   ├── salary_outliers.csv │   ├── filtered_senior_high_salary.csv │   ├── sorted_by_age.csv │   ├── X_input.csv │   ├── Y_output.csv │   └── ... ├── README.md                             # Project documentation (this file) └── .gitignore                            # Files/folders to exclude from Git tracking

---

## ✨ Features

- Generates a synthetic population dataset using Python and Faker
- Handles missing values and imputes numerical data
- Extracts features and labels for model-ready formats
- Detects outliers and visualizes key data distributions
- Saves all outputs as CSVs and images for easy reuse

---

## 📊 Visualizations Included

- Age distribution histogram  
- Gender proportion pie chart  
- Average salary by country bar plot  
- Numeric correlation heatmap  
- Device usage by subscription tier chart

---

## ⚙️ Requirements

- Python 3.8+
- pandas, numpy, matplotlib, seaborn, scikit-learn, faker

To install dependencies:

```bash
pip install -r requirements.txt


```

## 🧾 License
This project is released under the MIT License. You are free to use, modify, and distribute with proper attribution.

## 👤 Author
Maintained by @Gyanankur23
📧 gyanankurcricket20@gmail.com

If you find this project useful or want to contribute improvements, feel free to fork or raise a pull request!
