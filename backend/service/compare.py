import threading
import time

from scipy.spatial.distance import cosine, euclidean
import pygame

from backend.manager.compare_manager import CompareManager, get_compare_manager

is_playing_lock = threading.Lock()
pygame.mixer.init()

sound_duration = 0.5
last_play_time = 0


def compare(
    choreography_manager,
    lock,
    compare_manager:CompareManager = get_compare_manager()
):
    current_index = compare_manager.current_index
    print("current_index is ", ValueError)

    if compare_manager.current_index >= 11000:
        print("current_index exceed max frame")

    if compare_manager.current_index%6 == 0 and  (compare_manager.current_index > choreography_manager.return_size("c")):
        start = time.time()
        clap_over_head(compare_manager, choreography_manager, current_index)
        print(time.time() - start)


    # if compare_manager.current_index%6 == 0 and  (compare_manager.current_index > choreography_manager.return_size("d")):
    #     start = time.time()
    #     down_two_times_size(compare_manager, choreography_manager, current_index)
    #     print("run time : " ,time.time() - start)



"""
    値が小さい方が類似度が高い、閾値を上限としてそれ以下なら音を鳴らす
    予定としては 0.2(m)*0.3(45度)で0.06以下なら音を鳴らす?
    frameの数が違うから平均とか合計じゃない方がいいかも？
"""
def clap_over_head(compare_manager, choreography_manager, index):
    global last_play_time
    size = choreography_manager.return_size("c")
    index = compare_manager.current_index

    YOUR_THRESHOLD =0.8
    sum_left_arm = 0

    dp_sum = 0
    for i in range(8):
        for j in range(size):
            euclid = euclidean(compare_manager.clap_over_head[i][index-size+j][0:3], choreography_manager.clap_over_head[i][j][0:3])
            cos_sim = cosine(compare_manager.clap_over_head[i][index-size+j][3:6], choreography_manager.clap_over_head[i][j][3:6])
            dp_value = euclid*cos_sim
            print("eculid", euclid)
            print("cos_sim", cos_sim)
            print("dp_value", dp_value)
            dp_sum += dp_value

    ave = dp_sum/size

    if ave > YOUR_THRESHOLD:
        current_time = time.time()
        with is_playing_lock:  # ロックを取得して音声再生の状態を更新
            if (current_time - last_play_time) > sound_duration:
                last_play_time = current_time
                threading.Thread(target=play_drum2_snare).start()
                # asyncio.create_task(play_sound(cached_song))





def down_two_times_size(compare_manager, choreography_manager, index):
    pass



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