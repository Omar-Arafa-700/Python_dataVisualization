import pandas as pd

df = pd.read_csv(
    "data/Citywide_Payroll_Data__Fiscal_Year_.csv",
    low_memory=False
)

sample_df = (
    df
    .groupby(["Fiscal Year", "Agency Name"], group_keys=False)
    .apply(lambda x: x.sample(frac=0.03, random_state=42))
    .reset_index(drop=True)
)

sample_df.to_csv("data/nyc_payroll_sample.csv", index=False)