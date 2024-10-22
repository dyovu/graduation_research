import numpy as np
import json

with open('backend/dump_data/right_arm/bottom.json', 'r') as file:
    bottom = json.load(file)

with open('backend/dump_data/right_arm/front.json', 'r') as file:
    front = json.load(file)

with open('backend/dump_data/right_arm/side.json', 'r') as file:
    side = json.load(file)

with open('backend/dump_data/right_arm/top.json', 'r') as file:
    top = json.load(file)



def convert_to_numpy(data_list):
    right_arm = [
        np.zeros((7, len(data_list))),
        np.zeros((7, len(data_list))),
        np.zeros((7, len(data_list))),
        np.zeros((7, len(data_list)))
    ]
    
    for idx, item in enumerate(data_list.values()):
        right_arm[idx]= np.array(item) 

    return right_arm

# 関数を使って変換する
bottom_r = convert_to_numpy(bottom)
front_r = convert_to_numpy(front)
side_r = convert_to_numpy(side)
top_r = convert_to_numpy(top)

print(bottom)
print(front)
print(side)
print(top)

