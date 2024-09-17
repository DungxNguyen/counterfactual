# Grad-Metapopulation Method

## Requirements

Use the package manager [conda](https://docs.conda.io/en/latest/) to install required Python dependencies. Note: We used Python 3.7.

```bash
conda env create -f enviroment.yml
```

## Training

The following command will train and predict for all counties in MA state:

```bash
python -u main.py -st MA -j -d cpu -ew 202036 --seed 1234 -m meta -di COVID
```

The following command will train and predict for all age_groups in the Bogota city:

```bash
python -u main.py -st MA -j -d cpu -ew 202036 --seed 1234 -m meta -di bogota
```

The following command will differentially private train and predict for all counties in MA state:

```bash
python -u main.py -st MA -j -d cpu -ew 202036 --seed 1234 -m meta -di COVID --privacy
```

