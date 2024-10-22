for i in $(seq 0 1)
do
train_week=$((49 + $i))
test_week=$((49 + $i+4))
python prepare_dataset.py --moving_window $i --week $train_week
python prepare_dataset.py --moving_window $i --week $test_week --test
python prcess_data_dung.py --moving_window $i
python main.py -st MA -j -d 0 -ew 202036 --seed 1234 -m meta -di bogota -date "${i}_moving"
done