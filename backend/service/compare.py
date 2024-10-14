import threading
import time

from scipy.spatial.distance import cosine
import pygame

is_playing_lock = threading.Lock()
pygame.mixer.init()

sound_duration = 0.5
last_play_time = 0

def compare(
    compare_manager,
    db_data_manager
):
    if compare_manager.current_index%5 == 0 and  (compare_manager.current_index > db_data_manager.right_arm_frame):
        # start = time.time()
        # compare_right_arm(compare_manager, db_data_manager)
        # print(time.time() - start)
        pass
        
    if compare_manager.current_index%5 == 0 and  (compare_manager.current_index > db_data_manager.left_arm_frame):
        # start = time.time()
        # 
        # compare_left_arm(compare_manager, db_data_manager)

        compare_left_arm_by_time(compare_manager, db_data_manager)
        # print("run time : " ,time.time() - start)
        pass



def compare_right_arm(
    compare_manager,
    db_data_manager
):
    global last_play_time
    right_arm_size = db_data_manager.right_arm_frame
    index = compare_manager.current_index

    YOUR_THRESHOLD =0.8
    sum_right_arm = 0
    result = {
        "r_shoulder": [],
        "r_uparm": [],
        "r_lowarm": [],
        "r_hand": []
    }

    for i in range(7):
        cosine_similarity_r_shoulder = 1 - cosine(
            compare_manager.right_arm[0][i][index-right_arm_size+1:index+1], 
            db_data_manager.right_arm[0][i]
        )
        cosine_similarity_r_uparm = 1- cosine(
            compare_manager.right_arm[1][i][index-right_arm_size+1:index+1], 
            db_data_manager.right_arm[1][i]
        )
        cosine_similarity_r_lowarm = 1 - cosine(
            compare_manager.right_arm[2][i][index-right_arm_size+1:index+1], 
            db_data_manager.right_arm[2][i]
        )
        cosine_similarity_r_hand = 1 - cosine(
            compare_manager.right_arm[3][i][index-right_arm_size+1:index+1], 
            db_data_manager.right_arm[3][i]
        )
        sum_right_arm += cosine_similarity_r_shoulder + cosine_similarity_r_uparm + cosine_similarity_r_lowarm + cosine_similarity_r_hand

        result["r_shoulder"].append(cosine_similarity_r_shoulder)
        result["r_uparm"].append(cosine_similarity_r_uparm)
        result["r_lowarm"].append(cosine_similarity_r_lowarm)
        result["r_hand"].append(cosine_similarity_r_hand)

    print(result)
    average_right_arm = sum_right_arm/28
    
    print("sum right: ", sum_right_arm)
    print("average right: ", average_right_arm)

    if average_right_arm > YOUR_THRESHOLD:
        current_time = time.time()
        print(current_time - last_play_time)
        with is_playing_lock:  # ロックを取得して音声再生の状態を更新
            if (current_time - last_play_time) > sound_duration:
                last_play_time = current_time
                threading.Thread(target=play_guitar3).start()
                # asyncio.create_task(play_sound(cached_song))


def compare_left_arm(
    compare_manager,
    db_data_manager
):
    global last_play_time
    left_arm_size = db_data_manager.left_arm_frame
    index = compare_manager.current_index

    YOUR_THRESHOLD =0.8
    sum_left_arm = 0

    for i in range(7):
        cosine_similarity_l_shoulder = 1 - cosine(
            compare_manager.left_arm[0][i][index-left_arm_size+1:index+1], 
            db_data_manager.left_arm[0][i]
        )
        cosine_similarity_l_uparm = 1- cosine(
            compare_manager.left_arm[1][i][index-left_arm_size+1:index+1], 
            db_data_manager.left_arm[1][i]
        )
        cosine_similarity_l_lowarm = 1 - cosine(
            compare_manager.left_arm[2][i][index-left_arm_size+1:index+1], 
            db_data_manager.left_arm[2][i]
        )
        cosine_similarity_l_hand = 1 - cosine(
            compare_manager.left_arm[3][i][index-left_arm_size+1:index+1], 
            db_data_manager.left_arm[3][i]
        )
        sum_left_arm += cosine_similarity_l_shoulder + cosine_similarity_l_uparm + cosine_similarity_l_lowarm + cosine_similarity_l_hand

    average_left_arm = sum_left_arm/28

    print("sum left : ", sum_left_arm)
    print("average left : ", average_left_arm)

    if average_left_arm > YOUR_THRESHOLD:
        current_time = time.time()
        print(current_time - last_play_time)
        with is_playing_lock:  # ロックを取得して音声再生の状態を更新
            if (current_time - last_play_time) > sound_duration:
                last_play_time = current_time
                threading.Thread(target=play_drum2_snare).start()
                # asyncio.create_task(play_sound(cached_song))



def compare_left_arm_by_time(
    compare_manager,
    db_data_manager
):
    # 
    # 時間順に、7つのデータのまとまりとしてcos類似度を計算する
    # 
    global last_play_time
    left_arm_size = db_data_manager.left_arm_frame
    index = compare_manager.current_index

    YOUR_THRESHOLD =0.8
    sum_left_arm = 0

    print("compare_left_arm_time")

    for i in range(left_arm_size):
        cosine_similarity_l_shoulder = 1 - cosine(
            compare_manager.left_arm_time[0][index-left_arm_size+i][4:7], 
            db_data_manager.left_arm_time[0][i][4:7]
        )
        cosine_similarity_l_uparm = 1- cosine(
            compare_manager.left_arm_time[1][index-left_arm_size+i][4:7], 
            db_data_manager.left_arm_time[1][i][4:7]
        )
        cosine_similarity_l_lowarm = 1 - cosine(
            compare_manager.left_arm_time[2][index-left_arm_size+i][4:7], 
            db_data_manager.left_arm_time[2][i][4:7]
        )
        cosine_similarity_l_hand = 1 - cosine(
            compare_manager.left_arm_time[3][index-left_arm_size+i][4:7], 
            db_data_manager.left_arm_time[3][i][4:7]
        )
        tmp_sum = cosine_similarity_l_shoulder + cosine_similarity_l_uparm + cosine_similarity_l_lowarm + cosine_similarity_l_hand
        sum_left_arm += tmp_sum
        print("index: ", index-left_arm_size+i, " cosint is ", tmp_sum/4)

    average_left_arm = sum_left_arm/(4*left_arm_size)

    # print("sum left : ", sum_left_arm)
    print("average left : ", average_left_arm)

    if average_left_arm > YOUR_THRESHOLD:
        current_time = time.time()
        with is_playing_lock:  # ロックを取得して音声再生の状態を更新
            if (current_time - last_play_time) > sound_duration:
                last_play_time = current_time
                threading.Thread(target=play_drum2_snare).start()
                # asyncio.create_task(play_sound(cached_song))



def play_drum2_snare():
    print("音楽再生開始")
    sound = pygame.mixer.Sound("backend/sounds/drum2_snare.mp3")
    channel = pygame.mixer.find_channel()  # 空いているチャンネルを探す
    if channel:
        channel.play(sound)
    print("音楽再生終了")


def play_guitar3():
    print("音楽再生開始")
    sound = pygame.mixer.Sound("backend/sounds/guitar3.mp3")
    channel = pygame.mixer.find_channel()  # 空いているチャンネルを探す
    if channel:
        channel.play(sound)
    print("音楽再生終了")


