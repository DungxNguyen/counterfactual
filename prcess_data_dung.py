import pandas as pd
import torch
from tqdm import tqdm
import numpy as np
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument('--moving_window', type=int, default=0)
parser.add_argument('--root', type=str, default="./Data/Processed")


args = parser.parse_args()


start_date = pd.to_datetime("2020-03-03")
period = pd.to_timedelta(350+args.moving_window*7, unit='D')
end_date = start_date + period


data = pd.read_csv(os.path.join(args.root, "private_agg.csv"))

data["date"] = pd.to_datetime(data["date"], format='%Y-%m-%d')
data["merch_postal_code"] = data["merch_postal_code"].apply(str)

data = data[data.merch_postal_code.str.startswith("11")]
data_selected = data[(data["date"] <= end_date) & (data["date"] >= start_date)]

all_location_time_series = pd.DataFrame([])
ret = []
for g_idx, item in tqdm(data_selected.groupby(["merch_postal_code"])):
    item_new = item.set_index('date').resample('D').ffill().reset_index()
    all_location_time_series = pd.concat((item_new, all_location_time_series))
    ret.append(item_new["spendamt_clipped"].values)

final_ret = torch.from_numpy(np.array(ret))
torch.save(final_ret, "./Data/Processed/transaction_private_lap_{}_moving.pt".format(args.moving_window))