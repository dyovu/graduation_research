from fastapi import Depends
from scipy.spatial.distance import cosine


from backend.manager.db_data_manager import DbDataManager, get_db_data_manager

def compare(
    compare_manager,
    db_data_manager: DbDataManager = Depends(get_db_data_manager),
):
    size = db_data_manager.right_arm_frame
    index = compare_manager.current_index
    result = {
        "r_shoulder": [],
        "r_uparm": [],
        "r_lowarm": [],
        "r_hand": []
    }
    for i in range(7):
        cosine_similarity_r_shoulder = cosine(
            compare_manager.right_arm["r_shoulder"][i][index-size+1:index+1], 
            db_data_manager.right_arm["r_shoulder"][i]
        )
        cosine_similarity_r_uparm = cosine(
            compare_manager.right_arm["r_uparm"][i][index-size+1:index+1], 
            db_data_manager.right_arm["r_uparm"][i]
        )
        cosine_similarity_r_lowarm = cosine(
            compare_manager.right_arm["r_lowarm"][i][index-size+1:index+1], 
            db_data_manager.right_arm["r_lowarm"][i]
        )
        cosine_similarity_r_hand = cosine(
            compare_manager.right_arm["r_hand"][i][index-size+1:index+1], 
            db_data_manager.right_arm["r_hand"][i]
        )

        result["r_shoulder"].append(cosine_similarity_r_shoulder)
        result["r_uparm"].append(cosine_similarity_r_uparm)
        result["r_lowarm"].append(cosine_similarity_r_lowarm)
        result["r_hand"].append(cosine_similarity_r_hand)

    print(result)
