import pandas as pd
import random
import numpy as np
from faker import Faker

fake = Faker()
random.seed(42)
np.random.seed(42)

countries = ['India', 'USA', 'Germany', 'France', 'Japan', 'Brazil', 'Canada', 'Nigeria', 'Australia', 'South Korea', 'UK', 'Mexico', 'Egypt', 'China', 'Russia']
genders = ['Male', 'Female', 'Non-Binary']
education_levels = ['High School', 'Bachelor', 'Master', 'PhD', 'Diploma']
employment_statuses = ['Employed', 'Unemployed', 'Self-Employed', 'Student']
purchase_choices = ['Yes', 'No']
devices = ['Mobile', 'Desktop', 'Tablet']
platforms = ['iOS', 'Android', 'Windows', 'macOS', 'Linux']
sign_up_sources = ['Email', 'Social Media', 'Referral', 'Direct', 'Ad Campaign']
marital_statuses = ['Single', 'Married', 'Divorced', 'Widowed']
industries = ['IT', 'Finance', 'Education', 'Healthcare', 'Retail', 'Manufacturing', 'Logistics']
internet_usage = ['Light', 'Moderate', 'Heavy']
languages = ['English', 'Hindi', 'Spanish', 'French', 'Mandarin', 'Arabic', 'Portuguese']
subscription_types = ['Free', 'Basic', 'Premium', 'Enterprise']

n_rows = 20000

df = pd.DataFrame({
    'UserID': [f"U{100000+i}" for i in range(n_rows)],
    'First Name': [fake.first_name() for _ in range(n_rows)],
    'Last Name': [fake.last_name() for _ in range(n_rows)],
    'Email': [fake.email() for _ in range(n_rows)],
    'Country': [random.choice(countries) for _ in range(n_rows)],
    'City': [fake.city() for _ in range(n_rows)],
    'Age': np.random.randint(18, 70, n_rows),
    'Gender': [random.choice(genders) for _ in range(n_rows)],
    'Marital Status': [random.choice(marital_statuses) for _ in range(n_rows)],
    'Education': [random.choice(education_levels) for _ in range(n_rows)],
    'Employment Status': [random.choice(employment_statuses) for _ in range(n_rows)],
    'Industry': [random.choice(industries) for _ in range(n_rows)],
    'Years of Experience': np.random.randint(0, 40, n_rows),
    'Annual Salary (USD)': np.random.randint(15000, 200000, n_rows),
    'Device Used': [random.choice(devices) for _ in range(n_rows)],
    'Platform': [random.choice(platforms) for _ in range(n_rows)],
    'Internet Usage Level': [random.choice(internet_usage) for _ in range(n_rows)],
    'Preferred Language': [random.choice(languages) for _ in range(n_rows)],
    'Signed Up From': [random.choice(sign_up_sources) for _ in range(n_rows)],
    'Date Joined': [fake.date_between(start_date='-5y', end_date='today') for _ in range(n_rows)],
    'Last Active Date': [fake.date_between(start_date='-30d', end_date='today') for _ in range(n_rows)],
    'Purchased': [random.choice(purchase_choices) for _ in range(n_rows)],
    'Subscription Type': [random.choice(subscription_types) for _ in range(n_rows)],
    'Account Verified': [random.choice(['Yes', 'No']) for _ in range(n_rows)],
    'Credit Score': np.random.randint(300, 850, n_rows),
    'Referral Used': [random.choice(['Yes', 'No']) for _ in range(n_rows)],
    'Number of Logins': np.random.randint(1, 500, n_rows),
    'Cart Abandonment Rate (%)': np.round(np.random.uniform(0, 100, n_rows), 2),
    'Loyalty Score': np.random.randint(1, 10, n_rows),
    'Customer Segment': [random.choice(['Budget', 'Mid-tier', 'Premium']) for _ in range(n_rows)]
})

df.to_csv('population_dataset.csv', index=False)
print("✅ Dataset with 30 columns and 20,000 rows generated: 'rich_population_dataset.csv'")