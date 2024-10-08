import threading
import time

from scipy.spatial.distance import cosine

from backend.manager.compare_manager import CompareManager, get_compare_manager
from backend.dump_data.left_arm.left_arm import bottom_l, front_l, side_l, top_l


def check_cos():
    compare_left_arm()


def compare_left_arm(
    compare_manager:CompareManager = get_compare_manager()
):
    index = compare_manager.current_index

    bottom = [0]*4
    front = [0]*4
    side = [0]*4
    top = [0]*4

    for i in range(4):
        cos_bot = 1 - cosine(
            compare_manager.left_arm_time[i][index-1], 
            bottom_l[i]
        )
        bottom[i] = float(cos_bot)

        cos_fro = 1 - cosine(
            compare_manager.left_arm_time[i][index-1], 
            front_l[i]
        )
        front[i] = float(cos_fro)

        cos_sid = 1 - cosine(
            compare_manager.left_arm_time[i][index-1], 
            side_l[i]
        )
        side[i] = float(cos_sid)

        cos_top = 1 - cosine(
            compare_manager.left_arm_time[i][index-1], 
            top_l[i]
        )
        top[i] = float(cos_top)

    print("index : ", index)
    print("bot", bottom)
    print("front", front)
    print("side", side)
    print("top", top)

    