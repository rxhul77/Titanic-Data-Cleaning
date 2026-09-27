import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------
# 1. Load the Titanic dataset
# -----------------------------------

df = pd.read_csv("Titanic-Dataset.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset information:")
print(df.info())

print("\nMissing values before cleaning:")
print(df.isnull().sum())


# -----------------------------------
# 2. Clean missing data
# -----------------------------------

# Fill missing Age values with the median age
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Embarked values with the most common value
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Drop Cabin because it contains a large number of missing values
df = df.drop(columns=["Cabin"])


# -----------------------------------
# 3. Encode Sex
# -----------------------------------

# Male = 0, Female = 1
df["Sex"] = df["Sex"].map({
    "male": 0,
    "female": 1
})


# -----------------------------------
# 4. Encode Embarked
# -----------------------------------

# Convert C, Q, S into numeric values
df["Embarked"] = df["Embarked"].map({
    "C": 0,
    "Q": 1,
    "S": 2
})


# -----------------------------------
# 5. Check missing values again
# -----------------------------------

print("\nMissing values after cleaning:")
print(df.isnull().sum())


# -----------------------------------
# 6. Visualize Age Distribution
# -----------------------------------

plt.figure(figsize=(8, 5))

sns.histplot(
    df["Age"],
    bins=30,
    kde=True
)

plt.title("Age Distribution of Titanic Passengers")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")

plt.savefig("age_distribution.png")

plt.show()


# -----------------------------------
# 7. Save cleaned dataset
# -----------------------------------

df.to_csv("titanic_cleaned.csv", index=False)

print("\nCleaned dataset saved as: titanic_cleaned.csv")

print("\nCleaned dataset:")
print(df.head())