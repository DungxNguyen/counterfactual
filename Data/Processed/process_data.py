import pandas as pd

data = pd.read_csv("rr_county.csv")

data.drop(columns=["Unnamed: 0", "doctor_visits", "doctor_visits_quantized", "doctor_visits_prior"],inplace=True)
data.to_csv("rr_county_randomized.csv", index=False)

data = pd.read_csv("rr_county.csv")
data.drop(columns=["Unnamed: 0", "doctor_visits", "doctor_visits_quantized", "doctor_visits_randomized"],inplace=True)
data.to_csv("rr_county_randomized_prior.csv", index=False)