import os
import json
from selenium.webdriver.common.by import By

def write_followers_list(file_path, followers_list):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(followers_list, file)

def write_followings_list(file_path, followings_list):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(followings_list, file)

def write_followers_log(file_path, followers_list):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("Seguidores:\n")
        for idx, follower in enumerate(followers_list):
            file.write(f'{follower}\n')

def write_followings_log(file_path, followings_list):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("Seguidos:\n")
        file.write('\n'.join(followings_list))

def write_lost_followers(file_path, lost_followers):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(lost_followers))

def write_not_following_back(file_path, not_following_back):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(not_following_back))

def extract_number_of_followers(driver):
    followers_link = driver.find_element(By.PARTIAL_LINK_TEXT, "seguidores")
    num_followers = int(followers_link.find_element(By.TAG_NAME, 'span').text)
    return num_followers

def extract_number_of_followings(driver):
    followings_link = driver.find_element(By.PARTIAL_LINK_TEXT, "seguidos")
    num_followings = int(followings_link.find_element(By.TAG_NAME, 'span').text)
    return num_followings

def read_previous_followers(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []

def read_previous_followings(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []

def compare_followers_lists(previous_list, current_list):
    new_followers = list(set(current_list) - set(previous_list))
    lost_followers = list(set(previous_list) - set(current_list))
    return new_followers, lost_followers
