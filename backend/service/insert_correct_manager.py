import numpy as np
from backend.manager.compare_corrected_data import CompareCorrectDataManager, get_compare_correct_data_manager

"""
    何も計算せずにquaternionと相対座標値のみ入れていく
"""
def insert_correct_manager(
    data,
    compare_correct_data_manager: CompareCorrectDataManager = get_compare_correct_data_manager(),
):
    choreo = [
        "hip", "torso_1", "torso_2", "torso_3", "torso_4", "torso_5", "torso_6", "torso_7",
        "neck_1", "neck_2", "head", "l_shoulder", "l_up_arm", "l_low_arm", "l_hand",
        "r_shoulder", "r_up_arm", "r_low_arm", "r_hand", "l_up_leg", "l_low_leg", "l_foot",
        "l_toes", "r_up_leg", "r_low_leg", "r_foot", "r_toes"
    ]
    index = compare_correct_data_manager.current_index
    print("CompareCorrectDataManager index : ", index)

    if "skdf" in data:
        # print("skdf")
        pass
    else:
        tran = data["fram"]["btrs"]
        for i, value in enumerate(tran):
            compare_correct_data_manager[choreo[i]][index] = np.array([tran["tran"]])
        compare_correct_data_manager.current_index += 1
