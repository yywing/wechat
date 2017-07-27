#/usr/bin/python3.6
#coding=utf-8
import os
import random
from wxpy import *

bot = Bot()

def get_dir_list(file_path):
    file_list=os.listdir(file_path)
    dir_list=[]
    for i in file_list:
        abs_i = os.path.join(file_path,i)
        if os.path.isdir(abs_i):
            dir_list.append(i)
    return dir_list

def random_one(o_list):
    max_num = len(o_list)-1
    min_num = 0
    ran_num = random.randint(min_num,max_num)
    return o_list[ran_num]

@bot.register(User,TEXT)
def picture_reply(msg):
    if msg.text == "bot online?":
        msg.reply("i am here.")
    if msg.text == "picture":
        file_path = os.path.join(os.path.abspath("web-nb"),"zhihu_girls")
        dir_list = get_dir_list(file_path)
        if "collection" in dir_list:
            dir_list.remove("collection")
        while True :
            ran_one_dir = random_one(dir_list)
            picture_path = os.path.join(file_path,ran_one_dir)
            file_list=os.listdir(picture_path)
            if "qa.txt" in file_list:
                file_list.remove("qa.txt")
            if file_list:
                break
        ran_one_file = random_one(file_list)
        file_path = os.path.join(picture_path,ran_one_file)
        msg.reply_image(file_path)
    if msg.sender == bot.self and msg.text == "bot offline" : # no use
        bot.logout()
    if msg.text == "help":
        msg.reply("picture:for picture")
embed()
