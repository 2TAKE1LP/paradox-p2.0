import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
import sys
import os
import time
import requests 
from vk_api.longpoll import VkLongPoll, VkEventType
from distutils.dir_util import copy_tree
import time
import datetime
import random

#------------------------------ KEYBOARDS
def start():
    vk_session = vk_api.VkApi(token='vk1.a.DDjQTJPaKgviybVD3DbXOavAAdidHdsYi7V0Bjn_E6SLP6F-_9DOZ6EpuZJaB50zejntGdmWkPgBEw7JZY1x2GgoSmh4WzEwZnnJK6LUgE1zC2VVwJfkhcgh_0x_ijHFevM_SjderxfoNnhAVNtSRZTNZhLe_0yPc03yH_SNimftiYRgVwaBd3Ppm6MawQJw6tExdlEFZ_UuX_KbbReL-w')
    vk = vk_session.get_api() 

    keyboard = VkKeyboard(one_time=True)

    keyboard.add_button('Подключить Бота', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Купить Подписку', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Включить Бота', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Отключить Бота', color=VkKeyboardColor.POSITIVE)
    


    mss = 'Приветствую! Следуйте по кнопкам ниже:'
                               

    vk.messages.send(
        peer_id=prr,
        random_id=get_random_id(),
        keyboard=keyboard.get_keyboard(),
        message=mss
    )

def sub_mess():
    vk_session = vk_api.VkApi(token='vk1.a.DDjQTJPaKgviybVD3DbXOavAAdidHdsYi7V0Bjn_E6SLP6F-_9DOZ6EpuZJaB50zejntGdmWkPgBEw7JZY1x2GgoSmh4WzEwZnnJK6LUgE1zC2VVwJfkhcgh_0x_ijHFevM_SjderxfoNnhAVNtSRZTNZhLe_0yPc03yH_SNimftiYRgVwaBd3Ppm6MawQJw6tExdlEFZ_UuX_KbbReL-w')
    vk = vk_session.get_api() 

    keyboard = VkKeyboard(one_time=True)

    keyboard.add_button('Подключить Бота', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Купить Подписку', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Включить Бота', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Отключить Бота', color=VkKeyboardColor.POSITIVE)
    


    mss = 'За приобретением подписки обращаться к Администратору @id587742332 (PARADOX) [Резервный аккаунт: @id598198767 (Akame)] ~'
                               

    vk.messages.send(
        peer_id=prr,
        random_id=get_random_id(),
        keyboard=keyboard.get_keyboard(),
        message=mss
    )

def dont_understand():
    vk_session = vk_api.VkApi(token='vk1.a.DDjQTJPaKgviybVD3DbXOavAAdidHdsYi7V0Bjn_E6SLP6F-_9DOZ6EpuZJaB50zejntGdmWkPgBEw7JZY1x2GgoSmh4WzEwZnnJK6LUgE1zC2VVwJfkhcgh_0x_ijHFevM_SjderxfoNnhAVNtSRZTNZhLe_0yPc03yH_SNimftiYRgVwaBd3Ppm6MawQJw6tExdlEFZ_UuX_KbbReL-w')
    vk = vk_session.get_api() 

    keyboard = VkKeyboard(one_time=True)

    keyboard.add_button('Подключить Бота', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Купить Подписку', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Включить Бота', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Отключить Бота', color=VkKeyboardColor.POSITIVE)
    
    
                               

    vk.messages.send(
        peer_id=prr,
        random_id=get_random_id(),
        keyboard=keyboard.get_keyboard(),
        message='Выберите доступное действие: '
    )







#------------------------------------- SUB 

id_pid = os.getpid()
file = open('id_get_pid_group.txt', 'w+')
file.write(str(id_pid))
file.close()


def func():
    if os.path.isdir(str(us)) == True:
        file = open(str(us) + '\\token.txt', 'w+', encoding='utf-8')
        file.write(str(your_string.strip()))
        file.close()
        os.system('cd ' + str(us) + ' & start paradox.py')
        return
    else:

        path = 'Bot'
        to_directory = str(us)
        copy_tree(path, to_directory)
        file = open(to_directory + '\\token.txt', 'w+', encoding='utf-8')
        file.write(str(your_string.strip()))
        file.close()
        os.system('cd ' + str(us) + ' & start paradox.py')
        return


def valid():
    try:
        vk_session = vk_api.VkApi(token=your_string.strip())
        longpoll = VkLongPoll(vk_session)
        vk = vk_session.get_api() 
        vk8.messages.send(peer_id=event.peer_id, message='Вы подключили Бота, зайдите в избранное!', random_id=0)
        func()
        return
    except Exception as e:
        print(e)
        vk8.messages.send(peer_id=event.peer_id, message='Invalid Token', random_id=0)
        return


vk_session8 = vk_api.VkApi(token='vk1.a.DDjQTJPaKgviybVD3DbXOavAAdidHdsYi7V0Bjn_E6SLP6F-_9DOZ6EpuZJaB50zejntGdmWkPgBEw7JZY1x2GgoSmh4WzEwZnnJK6LUgE1zC2VVwJfkhcgh_0x_ijHFevM_SjderxfoNnhAVNtSRZTNZhLe_0yPc03yH_SNimftiYRgVwaBd3Ppm6MawQJw6tExdlEFZ_UuX_KbbReL-w')
longpoll = VkLongPoll(vk_session8)
vk8 = vk_session8.get_api()       

while True:
    try:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                text_ev_ev = event.text.lower()
                us = event.user_id
                id_message_for_delete = event.message_id
                prr = event.peer_id
                if text_ev_ev.startswith(f'/go'):
                    file = open('sub_list.txt', 'r')
                    rrrr = file.read()
                    file.close()
                    if rrrr.find(str(us)) != -1:
                        pass
                    else:
                        vk8.messages.send(peer_id=event.peer_id, message='У Вас нет подписки!', random_id=0)
                        break

                    your_string = event.text
                    s = your_string.split('&', 1)[0] + '&'
                    removal_list = ["/go", "https://oauth.vk.com/blank.html#access_token=", "&"]
                    for word in removal_list:
                        your_string = s.replace(word, "")
                    removal_list2 = ["https://oauth.vk.com/blank.html#access_token="]
                    for word in removal_list2:
                        your_string2 = your_string.replace(word, "")
                    removal_list3 = ["/go"]
                    for word in removal_list3:
                        your_string = your_string2.replace(word, "")

                    us=event.user_id
                    if your_string == '':
                        vk8.messages.send(peer_id=event.peer_id, message='Вы не отправили токен.', random_id=0)
                    else:
                        valid()
                        
                elif text_ev_ev.startswith(f'начать'):
                    start()
                elif text_ev_ev.startswith(f'купить подписку'):
                    sub_mess()
                elif text_ev_ev.startswith(f'привет'):
                    start()
                elif text_ev_ev.startswith(f'отключить бота'):
                    file = open('sub_list.txt', 'r')
                    rrrr = file.read()
                    file.close()
                    if rrrr.find(str(us)) != -1:
                        pass
                    else:
                        vk8.messages.send(peer_id=event.peer_id, message='У Вас нет подписки!', random_id=0)
                        break
                    file = open(str(us) + '\\PID_OBM_LP.txt', 'r')
                    a = file.read()
                    file.close()

                    os.system('taskkill /PID ' + str(a) + ' /F')
                    vk8.messages.send(peer_id=event.peer_id, message='Работа Бота остановлена', random_id=0)
                elif text_ev_ev.startswith(f'подключить бота'):
                    file = open('sub_list.txt', 'r')
                    rrrr = file.read()
                    file.close()
                    if rrrr.find(str(us)) != -1:
                        pass
                    else:
                        vk8.messages.send(peer_id=event.peer_id, message='У Вас нет подписки!', random_id=0)
                        break
                    vk8.messages.send(peer_id=event.peer_id, message='Для подключения Бота, перейдите в Телеграм-канал: https://t.me/+r0A1w3YiOq9kNmIy ; сам токен -> ВК Админ\nЗатем пишете команду /go (ссылка с токеном/токен)', random_id=0)
                elif text_ev_ev.startswith(f'включить бота'):
                    file = open('sub_list.txt', 'r')
                    rrrr = file.read()
                    file.close()
                    if rrrr.find(str(us)) != -1:
                        pass
                    else:
                        vk8.messages.send(peer_id=event.peer_id, message='У Вас нет подписки!', random_id=0)
                        try:
                       	    file = open(us + '\\PID_OBM_LP.txt', 'r')
                       	    llll = file.read()
                       	    file.close()
                       	    os.system('taskkill /PID ' + str(llll) + ' /F')
                       	except:
                       	    pass
                        break
                    try:
                        file = open(str(us) + '\\PID_OBM_LP.txt', 'r')
                        file.close()
                        os.system('cd ' + str(us) + ' & start paradox.py')
                        vk8.messages.send(peer_id=event.peer_id, message='Бот включен.', random_id=0)
                    except:
                        vk8.messages.send(peer_id=event.peer_id, message='Ваш Бот не подключен.', random_id=0)

                
                else:
                    dont_understand()




                        
    except Exception as e:
        print(e)

