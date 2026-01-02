import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/nyc_payroll_sample.csv")

# Clean currency columns
currency_cols = ["Regular Gross Paid", "Total OT Paid"]
for col in currency_cols:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
    )
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

# Total gross pay
df["Total Gross Pay"] = df["Regular Gross Paid"] + df["Total OT Paid"]

#1. Overtime share over time

ot_share = (
    df.groupby("Fiscal Year")[["Total OT Paid", "Total Gross Pay"]]
    .sum()
)

ot_share["OT Share (%)"] = (
    ot_share["Total OT Paid"] / ot_share["Total Gross Pay"] * 100
)

plt.figure()
ot_share["OT Share (%)"].plot(marker="o")
plt.title("Overtime as a Percentage of Total Payroll")
plt.xlabel("Fiscal Year")
plt.ylabel("Overtime Share (%)")
plt.grid(True)
plt.tight_layout()
plt.show()


#2. Agencies with highest overtime 

agency_ot = (
    df.groupby("Agency Name")[["Total OT Paid", "Total Gross Pay"]]
    .sum()
)

agency_ot["OT Share (%)"] = (
    agency_ot["Total OT Paid"] / agency_ot["Total Gross Pay"] * 100
)

top_ot_agencies = agency_ot.sort_values(
    "OT Share (%)", ascending=False
).head(10)

plt.figure()
top_ot_agencies["OT Share (%)"].plot(kind="barh")
plt.title("Top 10 Agencies by Overtime Share")
plt.xlabel("Overtime Share (%)")
plt.tight_layout()
plt.show()


#printing insights
print("\nOvertime Share Summary:")
print(ot_share["OT Share (%)"].describe())

print("\nTop Agencies by Overtime Share:")
print(top_ot_agencies["OT Share (%)"])
