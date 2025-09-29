import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def preprocess_data(file_path):
    df = pd.read_csv(file_path, encoding='ascii')
    df.columns = ['No', 'Age', 'Gender', 'Height', 'Weight', 'Physical Activity']
    df = df[1:]  
    df.reset_index(drop=True, inplace=True)
    # Converting relevant columns to numeric types
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
    df['Height'] = pd.to_numeric(df['Height'], errors='coerce')
    df['Weight'] = pd.to_numeric(df['Weight'], errors='coerce')
    df['Physical Activity'] = pd.to_numeric(df['Physical Activity'], errors='coerce')
    return df

file_path = r'C:\Users\PC\Desktop\ESISA\4 eme - Semestre 2\Data Mining\Projet santé 2\Projet santé 2\Anonymized_Patient_Parameters_Atherosclerosis.csv'
df = preprocess_data(file_path)


# Displaying the cleaned dataframe head to verify changes
print(df.head())
# Display basic information about the dataset
print("\nDataset Info:")
print(df.info())

print("\nFirst few rows of the dataset:")
print(df.head())

print("\nMissing values in each column:")
print(df.isnull().sum())

# Basic statistical description
print("\nStatistical description of numerical columns:")
print(df.describe())


plt.figure(figsize=(15, 10))

# Age distribution
plt.subplot(2, 2, 1)
sns.histplot(df['Age'], bins=10, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')

# Height distribution
plt.subplot(2, 2, 2)
sns.histplot(df['Height'], bins=10, kde=True)
plt.title('Height Distribution')
plt.xlabel('Height (cm)')
plt.ylabel('Frequency')

# Weight distribution
plt.subplot(2, 2, 3)
sns.histplot(df['Weight'], bins=10, kde=True)
plt.title('Weight Distribution')
plt.xlabel('Weight (kg)')
plt.ylabel('Frequency')

# Physical Activity distribution
plt.subplot(2, 2, 4)
sns.histplot(df['Physical Activity'], bins=10, kde=True)
plt.title('Physical Activity Distribution')
plt.xlabel('Physical Activity Level')
plt.ylabel('Frequency')

# Displaying the plots
plt.tight_layout()
plt.show()



correlation_matrix = df[['Age', 'Height', 'Weight', 'Physical Activity']].corr()

# Displaying the correlation matrix
print(correlation_matrix)

def process_data():
    # Read the CSV file
    df = pd.read_csv('notebook/merged_data.csv')
    
    # Check for null values
    null_counts = df.isnull().sum()
    print("\nNull values in each column:")
    print(null_counts)
    
    # Handle null values if they exist
    if null_counts.any():
        # For numeric columns, fill with median
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        for col in numeric_columns:
            if df[col].isnull().any():
                df[col] = df[col].fillna(df[col].median())
        
        # For categorical columns, fill with mode
        categorical_columns = df.select_dtypes(include=['object']).columns
        for col in categorical_columns:
            if df[col].isnull().any():
                df[col] = df[col].fillna(df[col].mode()[0])
    
    # Save the processed data
    df.to_csv('processed_data.csv', index=False)
    print("\nData has been processed and saved to 'processed_data.csv'")
    
    return df

if __name__ == "__main__":
    processed_df = process_data()