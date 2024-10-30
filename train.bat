cd codes/config/DANv1
python3 train.py -opt=options/setting1/train/train_setting1_x4.yml


python3 inference.py -input_dir=./inputs -output_dir=./outputs_1024
# 别用上面那个,直接去inference.py里运行