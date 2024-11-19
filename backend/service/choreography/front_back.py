import threading
import time

from scipy.spatial.distance import cosine, euclidean
import pygame
pygame.mixer.init()

is_playing_lock = threading.Lock()
last_play_time = 0


def front_back(compare_manager, choreography_manager, index):
    sound_duration = 1
    global last_play_time
    size = choreography_manager.return_size("f")
    YOUR_THRESHOLD = 0.79
    dp_per_joints = [0]*9

    dp_sum = 0
    for i in range(9):
        reference_pos = compare_manager.front_back[i][index-size][0:3]
        for j in range(size):
            euclid = euclidean(compare_manager.front_back[i][index-size+j][0:3] - reference_pos, choreography_manager.front_back[i][j][0:3])
            cos_sim = cosine(compare_manager.front_back[i][index-size+j][3:6], choreography_manager.front_back[i][j][3:6])
            dp_value = euclid*cos_sim
            dp_sum += dp_value
        dp_per_joints[i] = float(dp_sum)-dp_per_joints[i-1]

    ave = dp_sum/(size*8)
    # print(dp_per_joints)
    print("front_back ave : ", ave)

    if ave < YOUR_THRESHOLD:
        current_time = time.time()
        with is_playing_lock:  # ロックを取得して音声再生の状態を更新
            if (current_time - last_play_time) > sound_duration:
                last_play_time = current_time
                threading.Thread(target=piano1_2re).start()



def piano1_2re():
    print("音楽再生開始")
    sound = pygame.mixer.Sound("backend/sounds/piano1_2re.mp3")
    channel = pygame.mixer.find_channel()  # 空いているチャンネルを探す
    if channel:
        channel.play(sound)
    print("音楽再生終了")