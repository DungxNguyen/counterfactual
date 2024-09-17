from epiweeks import Week
from train_abm import train_predict
from train_abm_privacy import train_predict_privacy
import argparse
import os
import numpy as np
import traceback
from copy import copy
import os
import pandas as pd
import pdb 

def save_predictions(
    disease: str,
    model_name: str,
    region: str,
    pred_week: str,
    death_predictions: np.array,
    ):
    """
        Given an array w/ predictions, save as csv
    """
    data = np.array(
        [
            np.arange(len(death_predictions))+1,
            death_predictions
        ]
    )
    if disease=='COVID':
        df = pd.DataFrame(data.transpose(),columns=['k_ahead','deaths'])
    elif disease=='Flu':
        df = pd.DataFrame(data.transpose(),columns=['k_ahead','ili'])
    df['k_ahead'] = df['k_ahead'].astype('int8')
    path = './Results/{}/{}/'.format(disease,region)
    if not os.path.exists(path):
        os.makedirs(path)
    file_name = 'preds_{}_{}.csv'.format(model_name,pred_week)
    df.to_csv(path+file_name,index=False)


def save_params(
    disease: str,
    model_name: str,
    pred_week: str,
    param_values: np.array,
    ):
    """
        Given an array w/ predictions, save as csv
    """
    
    path = './Results/{}/'.format(disease)
    if not os.path.exists(path):
        os.makedirs(path)
    file_name = 'params_{}_{}.csv'.format(model_name,pred_week)
    with open(path+file_name, "ab") as f:
        np.savetxt(f, param_values[:-1], delimiter=',')
        np.savetxt(f, param_values[-1], delimiter=',')


if __name__ == "__main__":
    # Parsing command line arguments
    parser = argparse.ArgumentParser(description='GradABM for COVID-19 and Flu.')
    parser.add_argument('-m','--model_name', help='Model name.', default = 'GradABM')
    parser.add_argument('-di','--disease', help='Disease: COVID or Flu.', default = 'COVID')
    parser.add_argument('-s', '--seed', type=int, help='Seed for python random, numpy and torch', default = 6666)
    parser.add_argument('-n', '--num_runs', type=int, help='Number of runs', default = 1)
    parser.add_argument('-st','--state', help='State to predict', default = 'MA')
    parser.add_argument('-c','--county_id', help='County to predict, only when not using joint training', default = '25001')
    parser.add_argument('-d','--dev', nargs='+',type=str, default='0',help='Device number to use. Put list for multiple.')    
    parser.add_argument('-ew','--pred_ew',type=str, default='202021',help='Prediction week in CDC format')
    parser.add_argument('-j','--joint', action='store_true',help='Train all counties jointly')
    parser.add_argument('-i','--inference_only', action='store_true',help='Will not train if True, inference only')
    parser.add_argument('-no','--noise', type=int, help='Noise level for robustness experiments', default = 0)
    parser.add_argument('-f', '--results_file_postfix', help='Postfix to be appended to output dir for ease of interpretation', default = '')
    parser.add_argument('-da', '-dataset', default="./Data/Processed/county_data.csv")
    parser.add_argument('--privacy', action="store_true")
    # parser.set_defaults(joint=True)  # make true when removing no joint
    parser.set_defaults(inference_only=False)  # make true when removing no joint
    args = parser.parse_args()

    # get list of epiweeks for iteration
    disease = args.disease
    model_name = args.model_name
    pred_ew = Week.fromstring(args.pred_ew)

    def run_all_weeks(args, status):
        args.pred_week = pred_ew.cdcformat()
        try:
            if args.privacy:
                counties_predicted, predictions, learned_params = train_predict_privacy(args, status)
            else:
                counties_predicted, predictions, learned_params = train_predict(args, status) 
            num_counties = len(counties_predicted)
            # save_predictions(disease,model_name,counties_predicted,pred_ew,predictions[c,:])
            save_params(disease,model_name,pred_ew,learned_params)
        except Exception as e:
            print(f'exception: did not work for {args.state} week {pred_ew}: '+ str(e) + '\n')
            traceback.print_exc()
    

    import itertools
    from tqdm import tqdm

    stuff = list(range(10)) # number of counties
    all_seed_data = []
    for L in range(len(stuff) + 1):
        for subset in itertools.combinations(stuff, L):
            seed_status = {}
            for item in subset:
                seed_status[item] = 5
            all_seed_data.append(seed_status)
    
    all_seed_data = [{2:5, 3:5, 5:5, 7:5, 8:5, 9:5}]
    
    for status in tqdm(all_seed_data):
        print(status)
        run_all_weeks(copy(args), status)
