# Grad-Metapopulation Method

## Requirements

Use the package manager [conda](https://docs.conda.io/en/latest/) to install required Python dependencies. Note: We used Python 3.7.

```bash
conda env create -f enviroment.yml
```

## Training

Step 1: Privatize the dataset by running the jupyet notebook "Pets_Input_Gen.ipynb" and put the generated file under the directory "./Data/Processed/"

Step 2: Run the following command to train and predict forecasting models for the bogota city

The following command will train and predict for all age_groups in the Bogota city:

```bash
python -u main.py -st MA -j -d cpu -ew 202036 --seed 1234 -m meta -di bogota
```

(Note you have to manually change the Line 42 to the data you generated in Step 1)
