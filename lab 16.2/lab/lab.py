import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()
np.random.seed(0)

# Generate synthetic data
data = []
for i in range(1, 101):
    adm_date = fake.date_between('-1y', 'today')
    dis_date = adm_date + pd.Timedelta(days=random.randint(1, 15))
    data.append({
        'patient_id': i,
        'admission_date': adm_date if random.random() > 0.1 else None,
        'discharge_date': dis_date if random.random() > 0.1 else None,
        'diagnosis': random.choice(['Flu', 'Asthma', 'Diabetes', None]),
        'bill_amount': random.uniform(500, 10000) if random.random() > 0.1 else None,
        'insurance_provider': random.choice(['Aetna', 'Cigna', None])
    })

df = pd.DataFrame(data)

# Clean missing values
df['admission_date'] = df['admission_date'].fillna(method='ffill').fillna(method='bfill')
df['discharge_date'] = df['discharge_date'].fillna(method='ffill').fillna(method='bfill')
df['bill_amount'] = df['bill_amount'].fillna(df['bill_amount'].median())
df['diagnosis'] = df['diagnosis'].fillna(df['diagnosis'].mode()[0])
df['insurance_provider'] = df['insurance_provider'].fillna(df['insurance_provider'].mode()[0])

# Add derived columns
df['length_of_stay'] = (pd.to_datetime(df['discharge_date']) - pd.to_datetime(df['admission_date'])).dt.days
df['is_insured'] = df['insurance_provider'].notna()

# Standardize dates
df['admission_date'] = pd.to_datetime(df['admission_date']).dt.strftime('%Y-%m-%d')
df['discharge_date'] = pd.to_datetime(df['discharge_date']).dt.strftime('%Y-%m-%d')

# Save to CSV
df.to_csv('hospital_admissions_clean.csv', index=False)