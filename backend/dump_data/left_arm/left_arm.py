import numpy as np
import json

with open('backend/dump_data/left_arm/bottom.json', 'r') as file:
    bottom = json.load(file)

with open('backend/dump_data/left_arm/front.json', 'r') as file:
    front = json.load(file)

with open('backend/dump_data/left_arm/side.json', 'r') as file:
    side = json.load(file)

with open('backend/dump_data/left_arm/top.json', 'r') as file:
    top = json.load(file)



def convert_to_numpy(data_list):
    left_arm = [
        np.zeros((7, len(data_list))),
        np.zeros((7, len(data_list))),
        np.zeros((7, len(data_list))),
        np.zeros((7, len(data_list)))
    ]
    
    for idx, item in enumerate(data_list):
        left_arm[idx] = np.array(item['tran'])  

    return left_arm

# 関数を使って変換する
bottom_l = convert_to_numpy(bottom)
front_l = convert_to_numpy(front)
side_l = convert_to_numpy(side)
top_l = convert_to_numpy(top)


