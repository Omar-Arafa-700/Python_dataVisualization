import pandas as pd
import matplotlib.pyplot as plt

# Load and prepare data
df = pd.read_csv("data/nyc_payroll_sample.csv")

# Clean currency columns and create total gross pay
currency_cols = ["Regular Gross Paid", "Total OT Paid", "Total Other Pay"]
for col in currency_cols:
    df[col] = df[col].astype(str).str.replace('$', '', regex=False).str.replace(',', '', regex=False)
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

df["Total Gross Pay"] = df["Regular Gross Paid"] + df["Total OT Paid"] + df["Total Other Pay"]

# Calculate aggregations
yearly_payroll = df.groupby("Fiscal Year")["Total Gross Pay"].sum().sort_index()
avg_pay = df.groupby("Fiscal Year")["Total Gross Pay"].mean().sort_index()
top_agencies = df.groupby("Agency Name")["Total Gross Pay"].sum().sort_values(ascending=False).head(10)

# Create visualizations
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("NYC Payroll Trends Dashboard", fontsize=16, fontweight='bold')

# Total Payroll Over Time
yearly_payroll.plot(ax=axes[0, 0], marker='o')
axes[0, 0].set_title("Total NYC Payroll Over Time")
axes[0, 0].set_xlabel("Fiscal Year")
axes[0, 0].set_ylabel("Total Gross Pay ($)")
axes[0, 0].grid(True)

# Average Pay Over Time
avg_pay.plot(ax=axes[0, 1], marker='s')
axes[0, 1].set_title("Average Gross Pay per Employee Over Time")
axes[0, 1].set_xlabel("Fiscal Year")
axes[0, 1].set_ylabel("Average Gross Pay ($)")
axes[0, 1].grid(True)

# Top Agencies
top_agencies.plot(kind='barh', ax=axes[1, 0])
axes[1, 0].set_title("Top 10 Agencies by Total Payroll")
axes[1, 0].set_xlabel("Total Gross Pay ($)")
axes[1, 0].grid(True)

# Year-over-Year Growth
yearly_payroll_growth = yearly_payroll.pct_change() * 100
yearly_payroll_growth.plot(kind='bar', ax=axes[1, 1])
axes[1, 1].set_title("Year-over-Year Payroll Growth (%)")
axes[1, 1].set_xlabel("Fiscal Year")
axes[1, 1].set_ylabel("Growth Rate (%)")
axes[1, 1].axhline(y=0, color='black', linestyle='-', linewidth=0.5)
axes[1, 1].grid(True)

plt.tight_layout()
plt.show()

# Print summary
print(f"\nTotal Payroll: {yearly_payroll.index[0]}-{yearly_payroll.index[-1]}")
print(f"  Change: {((yearly_payroll.iloc[-1] / yearly_payroll.iloc[0]) - 1) * 100:.2f}%")
print(f"\nAverage Pay: {avg_pay.index[0]}-{avg_pay.index[-1]}")
print(f"  Change: {((avg_pay.iloc[-1] / avg_pay.iloc[0]) - 1) * 100:.2f}%")