import time

import pygame

from backend.manager.compare_manager import CompareManager, get_compare_manager
from backend.service.choreography.clap_over_head import clap_over_head
from backend.service.choreography.down_two_times import down_two_times
from backend.service.choreography.front_back import front_back
from backend.service.choreography.jump import jump
from backend.service.choreography.l_arm_and_leg_side import l_arm_and_leg_side
from backend.service.choreography.r_arm_and_leg_side import r_arm_and_leg_side

"""
    値が小さい方が類似度が高い、閾値を上限としてそれ以下なら音を鳴らす
    予定としては 0.2(m)*0.3(45度)で0.06以下なら音を鳴らす?
    frameの数が違うから平均とか合計じゃない方がいいかも？
"""

def compare(
    choreography_manager,
    compare_manager:CompareManager = get_compare_manager()
):  
    current_index = compare_manager.current_index - 1
    # print("current_index is ", current_index)

    if compare_manager.current_index >= 11000:
        print("current_index exceed max frame")
    
    # start = time.time()
    if compare_manager.current_index%6 == 0 and  (compare_manager.current_index > choreography_manager.return_size("c")):
        # start = time.time()
        clap_over_head(compare_manager, choreography_manager, current_index)
        # print("run time clap_over_head : " ,time.time() - start)
        pass
    
    if compare_manager.current_index%6 == 0 and  (compare_manager.current_index > choreography_manager.return_size("f")):
        # start = time.time()
        front_back(compare_manager, choreography_manager, current_index)
        # print("run time front_back : " ,time.time() - start)
        pass

    if compare_manager.current_index%6 == 0 and  (compare_manager.current_index > choreography_manager.return_size("j")):
        # start = time.time()
        jump(compare_manager, choreography_manager, current_index)
        # print("run time jump : " ,time.time() - start)
        pass
        
    if compare_manager.current_index%6 == 0 and  (compare_manager.current_index > choreography_manager.return_size("l")):
        # start = time.time()
        l_arm_and_leg_side(compare_manager, choreography_manager, current_index)
        # print("run time l_arm_and_leg_side : " ,time.time() - start)
        pass
    
    if compare_manager.current_index%6 == 0 and  (compare_manager.current_index > choreography_manager.return_size("r")):
        # start = time.time()
        r_arm_and_leg_side(compare_manager, choreography_manager, current_index)
        # print("run time r_arm_and_leg_side : " ,time.time() - start)
        pass

    if compare_manager.current_index%6 == 0 and  (compare_manager.current_index > choreography_manager.return_size("d")):
        # start = time.time()
        # down_two_times(compare_manager, choreography_manager, current_index)
        # print("run time down_two_times : " ,time.time() - start)
        pass
    # print("run time all : " ,time.time() - start)





def drum1_snare():
    print("音楽再生開始")
    sound = pygame.mixer.Sound("backend/sounds/drum1_snare.mp3")
    channel = pygame.mixer.find_channel()  # 空いているチャンネルを探す
    if channel:
        channel.play(sound)
    print("音楽再生終了")
