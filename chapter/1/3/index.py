import os
import sys
import tqdm
import pygame
import time
pygame.mixer.init()
se_boom = pygame.mixer.Sound("./se/boom.mp3")
se_beep = pygame.mixer.Sound("./se/beep.mp3")
se_sti1 = pygame.mixer.Sound("./se/shooting1.mp3")
se_sti2 = pygame.mixer.Sound("./se/shooting2.mp3")
se_dialup = pygame.mixer.Sound("./se/dial-modem-sound-effect-042160010_nw_prev_new.mp3")
print("幻想乡，727号公路旁的枫叶林，min家 | 2017-04-10")
pygame.mixer.music.load("./music/Year-Round_Absorbed_Curiosity_Chiptune_remix_and_no_main_melody__--_minqwq.mp3")
pygame.mixer.music.play()
print("音乐:Year-Round Absorbed Curiosity(Chiptune remix and no main melody) | by minqwq")
print("<minqwq> (伸腰)")
input()
print("然后远处传来了爆炸声。")
input()
print("<minqwq> ?")
input()
print("我从窗外看去。")
input()
print("我看到了两个人在用很强的魔法战斗。")
input()
se_sti1.play()
print("<???> 啊啊啊啊啊啊！！！！！！")
input()
se_sti2.play()
print("<???> 哈--------！！！！")
input()
print("...没动静了？")
input()
print("好像有一方受伤了...")
input()
print("<minqwq> 我可能需要打个救护车过来...")
input()
se_beep.play()
print("(启动电脑...)")
input()
print("* Screen View *")
input()
print("PY OS Improved 2.6.1_pre")
while True:
    pcloginuser = input("Localhost login: ")
    if pcloginuser == "minqwq":
        break
    else:
        print("Unknown user, please retry...(tips:minqwq)")
print("* Player View *")
print("Welcome to PY OS Improved!")
print("tips:type 'mail'")
print("autoexec.py | Line 1 | dialup")
se_dialup.play()
time.sleep(16)
print("Welcome to the Internet!")
print("You dont have any new mail received.")
while True:
    cmd = input("/ # ")
    if cmd == "mail":
        break
print("emergency@genhospital.moe\nFrom:minqwq\nTitle:这里有一个女孩受伤了\nContent:\n位置:727号公路旁树林\n如需详细位置，请回邮。")
input()
print("<minqwq> 好，发送")
input()
print("伴随着一阵刺耳的拨号上网音，邮件成功发出去了。")
input()
print("接下来就是等着了。")