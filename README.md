# Grad-Metapopulation Method

## Requirements

Use the package manager [conda](https://docs.conda.io/en/latest/) to install required Python dependencies. Note: We used Python 3.7.

```bash
conda env create -f enviroment.yml
```

## Training

### Quick Demo
To quickly evaluate our method on the Bogota dataset, run the following command:

```bash
bash run.sh 
```

If you want to acess our system with a user-friendly GUI: simply run the code:

```python
python index.py
```

### Detailed Steps
Our pipeline consists of two steps:

**Step 1: Data Preparation**
We use two types of data sources:
- **public dataset** such as Google Heath Trends, PCR, and so on
- **private dataset**, i.e., transacation dataset

To prepare the public dataset, use the following commands:
```python
python prepare_dataset.py --moving_window $i --week $train_week
python prepare_dataset.py --moving_window $i --week $test_week --test
```
- The week parameter controls the length of the training period (default: 49 weeks starting from 2020-03-01).
- The moving_window parameter specifies how many windows to expand from the given training period.
- The --test flag extends the data by an additional four weeks, corresponding to the prediction horizon.

To prepare the private dataset, use the following command:
```python
python prcess_data_dung.py --moving_window $i
```
- The moving_window parameter is used similarly here to control the expansion of windows.

**Step 2: Data Preparation**

After preparing the datasets, run the following command to perform epidemic simulation and prediction:


```python
python main.py -st MA -j -d 0 --seed 1234 -m meta -di bogota -date "${i}_moving"
```
