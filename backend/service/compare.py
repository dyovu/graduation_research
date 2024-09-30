import threading
import asyncio
import time

from fastapi import Depends
from scipy.spatial.distance import cosine

# from pydub import AudioSegment
# from pydub.playback import play
import pygame


# cached_mp3 = AudioSegment.from_mp3("backend/sounds/drum2_snare.mp3")

is_playing_lock = threading.Lock()
pygame.mixer.init()

sound_duration = 0.5
last_play_time = 0

async def compare_right_arm(
    compare_manager,
    db_data_manager
):
    global last_play_time
    right_arm_size = db_data_manager.right_arm_frame
    index = compare_manager.current_index

    YOUR_THRESHOLD =0.8
    sum_right_arm = 0
    sum_left_arm = 0
    result = {
        "r_shoulder": [],
        "r_uparm": [],
        "r_lowarm": [],
        "r_hand": []
    }

    for i in range(7):
        cosine_similarity_r_shoulder = 1 - cosine(
            compare_manager.right_arm["r_shoulder"][i][index-right_arm_size+1:index+1], 
            db_data_manager.right_arm["r_shoulder"][i]
        )
        cosine_similarity_r_uparm = 1- cosine(
            compare_manager.right_arm["r_uparm"][i][index-right_arm_size+1:index+1], 
            db_data_manager.right_arm["r_uparm"][i]
        )
        cosine_similarity_r_lowarm = 1 - cosine(
            compare_manager.right_arm["r_lowarm"][i][index-right_arm_size+1:index+1], 
            db_data_manager.right_arm["r_lowarm"][i]
        )
        cosine_similarity_r_hand = 1 - cosine(
            compare_manager.right_arm["r_hand"][i][index-right_arm_size+1:index+1], 
            db_data_manager.right_arm["r_hand"][i]
        )
        sum_right_arm += cosine_similarity_r_shoulder + cosine_similarity_r_uparm + cosine_similarity_r_lowarm + cosine_similarity_r_hand

        result["r_shoulder"].append(cosine_similarity_r_shoulder)
        result["r_uparm"].append(cosine_similarity_r_uparm)
        result["r_lowarm"].append(cosine_similarity_r_lowarm)
        result["r_hand"].append(cosine_similarity_r_hand)

    print(result)
    average_right_arm = sum_right_arm/28
    
    print("sum right: ", sum)
    print("average right: ", average_right_arm)

    if average_right_arm > YOUR_THRESHOLD:
        current_time = time.time()
        print(current_time - last_play_time)
        with is_playing_lock:  # ロックを取得して音声再生の状態を更新
            if (current_time - last_play_time) > sound_duration:
                last_play_time = current_time
                threading.Thread(target=play_sound).start()
                # asyncio.create_task(play_sound(cached_song))


async def compare_left_arm(
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
            compare_manager.left_arm["l_shoulder"][i][index-left_arm_size+1:index+1], 
            db_data_manager.left_arm["l_shoulder"][i]
        )
        cosine_similarity_l_uparm = 1- cosine(
            compare_manager.left_arm["l_uparm"][i][index-left_arm_size+1:index+1], 
            db_data_manager.left_arm["l_uparm"][i]
        )
        cosine_similarity_l_lowarm = 1 - cosine(
            compare_manager.left_arm["l_lowarm"][i][index-left_arm_size+1:index+1], 
            db_data_manager.left_arm["l_lowarm"][i]
        )
        cosine_similarity_l_hand = 1 - cosine(
            compare_manager.left_arm["l_hand"][i][index-left_arm_size+1:index+1], 
            db_data_manager.left_arm["l_hand"][i]
        )
        sum_left_arm += cosine_similarity_l_shoulder + cosine_similarity_l_uparm + cosine_similarity_l_lowarm + cosine_similarity_l_hand

    average_left_arm = sum_left_arm/28

    print("sum left : ", sum)
    print("average left : ", average_left_arm)

    if average_left_arm > YOUR_THRESHOLD:
        current_time = time.time()
        print(current_time - last_play_time)
        with is_playing_lock:  # ロックを取得して音声再生の状態を更新
            if (current_time - last_play_time) > sound_duration:
                last_play_time = current_time
                threading.Thread(target=play_sound2).start()
                # asyncio.create_task(play_sound(cached_song))



def play_sound():
    print("音楽再生開始")
    pygame.mixer.music.load("backend/sounds/drum2_snare.mp3")
    pygame.mixer.music.play()
    # while pygame.mixer.music.get_busy():  # 再生が終わるまで待機
    #     continue
    print("音楽再生終了")

def play_sound2():
    print("音楽再生開始")
    pygame.mixer.music.load("backend/sounds/guitar3.mp3")
    pygame.mixer.music.play()
    # while pygame.mixer.music.get_busy():  # 再生が終わるまで待機
    #     continue
    print("音楽再生終了")


