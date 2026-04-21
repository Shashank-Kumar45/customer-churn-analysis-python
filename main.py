import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid')

# -----------------------------
# Create plot folder
# -----------------------------
plot_folder = "plot"
os.makedirs(plot_folder, exist_ok=True)

def save_plot(name):
    plt.savefig(os.path.join(plot_folder, f"{name}.png"), bbox_inches='tight')

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv(r"C:\Users\nawad\Downloads\Telco-Customer-Churn.csv")
print("Dataset Loaded Successfully")
print(df.shape)

# print(df.info())


print("First 5 row")
print(df.head())

# Basic dataset info
print("\nDATASET INFO")
print(df.info())
print("\nShape of Coffee_Chain_sale")
print(df.shape)
print(df.describe())
print(df.isnull().sum())
print(df.isnull().sum().sum())

#--------------------------------------------------------
# replace blanks with 0
df['TotalCharges']=df['TotalCharges'].replace(" ","0")
df['TotalCharges']=df['TotalCharges'].astype("float")
#print(df.info())

print(df.duplicated().sum())
print(df['customerID'].duplicated().sum())

#---------------------------------------------------------
# Convert 0 and 1 of SeniorCitizen to "Yes" and "No"
def convert(value):
    if value == 1:
        return "Yes"
    else:
        return "No"

df['SeniorCitizen']=df['SeniorCitizen'].apply(convert)
#print(df.head(30))

#----------------------------------------------------------
# Count of Churn Customers
sns.countplot(x='Churn',data=df)
plt.title("Count of Churn Customers")

save_plot("churn_count")
plt.show()

#----------------------------------------------------------
# Pie Chart for customers by percentage
group_by=df.groupby("Churn").agg({'Churn':'count'})
plt.pie(group_by['Churn'],autopct="%1.2f%%", labels=group_by.index)
plt.title("Percentage of Churn Customers")

save_plot("churn_percentage")
plt.show()

# from the given pie chart we can conclude that 26.54% of our customers have churned out.
# not let's explore the reason behind it

#----------------------------------------------------------
# churn by gender
sns.countplot(x='gender', data=df,hue='Churn',palette="Set2",legend=True)
plt.title("Churn by Gender")

save_plot("churn_gender")
plt.show()

#----------------------------------------------------------
# churn by SeniorCitizen
sns.countplot(x='SeniorCitizen', data=df)
plt.title("Count of Customers by SeniorCitizen")

save_plot("churn_senior")
plt.show()

# -----------------------------------------------------
# Create cross-tab (counts)
ct = pd.crosstab(df['SeniorCitizen'], df['Churn'])

# Convert to percentage
ct_pct = ct.div(ct.sum(axis=1), axis=0) * 100

# Plot stacked bar chart
ax = ct_pct.plot(kind='bar', stacked=True, figsize=(5,5))

# Add percentage labels
for i in range(len(ct_pct)):
    cum_sum = 0
    for j in range(len(ct_pct.columns)):
        value = ct_pct.iloc[i, j]
        ax.text(i, cum_sum + value/2, f"{value:.1f}%",
                ha='center', va='center', color='white', fontsize=9)
        cum_sum += value

plt.title("Churn by SeniorCitizen (%)")
plt.ylabel("Percentage")
plt.xlabel("SeniorCitizen")
plt.legend(title="Churn")

save_plot("seniorcitizen_percentage")
plt.show()

# Comparative a greater percentage of people in senior citizen category have churned.

#----------------------------------------------------------
plt.hist(df["tenure"],bins=30,color='green',edgecolor='blue')
plt.xlabel("Tenure")
plt.ylabel("Count")
plt.title("Histogram of Tenure")
plt.xticks(rotation=45)
plt.yticks(rotation=45)

save_plot("tenure_hist")
plt.show()

# people who have used our services for a long time have stayed and pwople who have used our services.
# 1 or 2 months have churned.

#----------------------------------------------------------
plt.figure(figsize=(3,3))
sns.countplot(x='Contract', data=df,hue='Churn')
plt.title("Count of Customers by Contract")

save_plot("contract_churn")
plt.show()

# people who have month to month contract are likely to churn then from those who have 1 or 2 years or contract.

# print(df.columns.values)

#----------------------------------------------------------
cols = ['PhoneService', 'MultipleLines', 'InternetService',
        'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
        'TechSupport', 'StreamingTV', 'StreamingMovies']

# Set grid size (3x3 since 9 columns)
fig, axes = plt.subplots(3, 3, figsize=(14, 9))
axes = axes.flatten()

for i, col in enumerate(cols):
    sns.countplot(x=col, data=df, ax=axes[i], hue='Churn')
    axes[i].set_title(f"Count Plot of {col}")
    axes[i].tick_params(axis='x')

plt.tight_layout()

save_plot("services_analysis")
plt.show()

# 1.Customers without value-added services like OnlineSecurity, TechSupport, and
# DeviceProtection show much higher churn, indicating these services help retain users.
# 2.Fiber optic users have the highest churn rate, while DSL users are relatively more stable.
# 3.Having PhoneService or MultipleLines doesn’t strongly reduce churn, suggesting basic
# services alone aren’t enough for retention.
# 4.Customers with “No internet service” consistently show very low churn, meaning churn
# is mainly driven by active internet users.

#--------------------------------------------------------------------
# countplot for Payment Method
plt.figure(figsize=(3,3))
sns.countplot(x='PaymentMethod', data=df,hue='Churn')
plt.title("Churn Customers by PaymentMethod")
plt.xticks(rotation=45)

save_plot("payment_method")
plt.show()

# customer is likely to churn when he is using electronic check as a payment method.


#--------------------------------------------------------------------
# Correlation heatmap for numeric columns
plt.figure(figsize=(6,4))
numeric_corr = df.select_dtypes(include=[np.number])

sns.heatmap(numeric_corr.corr(), cmap="Greens", fmt="1.2f", annot=True, linewidths=0.5)
plt.title("Feature Correlation Heatmap For Churn Dataset")

save_plot("correlation_heatmap")
plt.show()

#-----------------------------------------------------------------------
# IQR Method Compute Q1 (25th percentage) and Q3 (75th peercentage)
Q1 = numeric_corr.quantile(0.25)
Q3 = numeric_corr.quantile(0.75)
IQR = Q3 - Q1

# Define outliers as values outside 1.5*IQR range
outliers = ((numeric_corr < (Q1 - 1.5 * IQR)) |
            (numeric_corr > (Q3 + 1.5 * IQR)))

outlier_counts = outliers.sum()

# Print rows contaning outliers
print("\nOutliers Detected: \n", df[outliers.any(axis=1)])

#----------------------------------------------------------
# Boxplot 
for col in numeric_corr.columns:
    plt.figure(figsize=(6,3))
    sns.boxplot(x=numeric_corr[col])
    plt.title(f"Boxplot of {col}")

    save_plot(f"boxplot_{col}")
    plt.show()
