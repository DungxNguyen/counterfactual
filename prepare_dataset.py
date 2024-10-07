import pandas as pd
import matplotlib.pyplot as plt
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument('--moving_window', type=int, default=0)
parser.add_argument('--test', action='store_true')
parser.add_argument('--root', type=str, default="./Data/Processed")
parser.add_argument('--week', type=int, default=49)

args = parser.parse_args()

start_date = pd.to_datetime("2020-03-03")
test_period = 28 if args.test else 0
period = pd.to_timedelta(350+args.moving_window*7 + test_period, unit='D')

end_date = start_date + period


data = pd.read_csv(os.path.join(args.root, "minimal_dataset.csv"))
data = data[data["region"] == "Bogota"]
data.drop(columns="Unnamed: 0", inplace=True)
data["date"] = pd.to_datetime(data.date, format='%Y-%m-%d')
data_selected = data[(data["date"] <= end_date) & (data["date"] >= start_date)]



GHT = pd.read_csv(os.path.join(args.root,"multiTimeline.csv"))
GHT['Week'] = pd.to_datetime(GHT.Week, format='%Y-%m-%d')
GHT = GHT[(GHT["Week"] <= end_date) & (GHT["Week"] >= start_date)]

GHT = GHT.set_index('Week').resample('D').ffill().reset_index()

pcr_data = pd.read_csv(os.path.join(args.root,"Pruebas_PCR_procesadas_de_COVID-19_en_Colombia__Departamental__20240910.csv"))

pcr_data['Fecha'] = pd.to_datetime(pcr_data.Fecha, format='%Y-%m-%d')
# data = data.set_index('Fecha')
pcr_data = pcr_data[["Fecha", "Bogota"]]
pcr_data['incremental'] = pcr_data['Bogota'].diff()
pcr_data.drop(columns="Bogota", inplace=True)

pcr_data = pcr_data[(pcr_data["Fecha"] <= end_date) & (pcr_data["Fecha"] >= start_date)]
# pcr_data.drop(columns="Fecha", inplace=True)
pcr_data = pcr_data.fillna(0)
print(data_selected.shape)
print(GHT.shape)
print(pcr_data.shape)


merged_dataset = pd.merge(pd.merge(data_selected,GHT,left_on='date', right_on="Week"),pcr_data, left_on='date', right_on="Fecha")
merged_dataset.drop(columns=["Week", "date", "year", "Fecha", "epi_week", "region", "incremental", "covid-19 vacuna"], inplace=True)
merged_dataset.to_csv(os.path.join(args.root, "{}_{}_moving.csv".format("test" if args.test else "train", args.moving_window)), index=None)

print(merged_dataset.shape[0] / 7)
assert args.week == merged_dataset.shape[0] / 7
print(merged_dataset.shape)
