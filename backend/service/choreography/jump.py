import threading
import time

from scipy.spatial.distance import cosine, euclidean
import pygame
pygame.mixer.init()

is_playing_lock_jump = threading.Lock()
last_play_time = 0
sound = pygame.mixer.Sound("backend/sounds/cymbal.mp3")


def jump(compare_manager, choreography_manager, index):
    global last_play_time
    sound_duration = 1
    size = choreography_manager.return_size("j")
    YOUR_THRESHOLD = 0.1

    dp_sum = 0
    for i in range(6):
        reference_pos = compare_manager.jump[i][index-size][0:3]
        for j in range(size):
            euclid = euclidean(compare_manager.jump[i][index-size+j][0:3] - reference_pos, choreography_manager.jump[i][j][0:3])
            cos_sim = cosine(compare_manager.jump[i][index-size+j][3:6], choreography_manager.jump[i][j][3:6])
            dp_value = euclid*cos_sim
            dp_sum += dp_value

    ave = dp_sum/(size*8)
    # print(dp_per_joints)
    print("jump ave : ", ave)

    if ave < YOUR_THRESHOLD:
        current_time = time.time()
        with is_playing_lock_jump:  # ロックを取得して音声再生の状態を更新
            if (current_time - last_play_time) > sound_duration:
                last_play_time = current_time
                threading.Thread(target=cymbal).start()

    
def cymbal():
    print("音楽再生開始")
    print(time.time())
    channel = pygame.mixer.find_channel()  # 空いているチャンネルを探す
    if channel:
        channel.play(sound)
    print("音楽再生終了")
    
