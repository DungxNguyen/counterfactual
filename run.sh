# python prepare_dataset.py --moving_window 0 --week 49
# python prepare_dataset.py --moving_window 0 --week 53 --test
# python prcess_data_dung.py --moving_window 0
# python main.py -st MA -j -d 0 -ew 202036 --seed 1234 -m meta -di bogota -date "0_moving"

python prepare_dataset.py --moving_window 1 --week 50
python prepare_dataset.py --moving_window 1 --week 54 --test
python prcess_data_dung.py --moving_window 1
python main.py -st MA -j -d 0 -ew 202036 --seed 1234 -m meta -di bogota -date "1_moving"

# python prepare_dataset.py --moving_window 2 --week 51
# python prcess_data_dung.py --moving_window 2
