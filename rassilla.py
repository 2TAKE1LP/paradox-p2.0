from vkbottle.bot import Bot, Message
import time, math

bot = Bot(token="vk1.a.DDjQTJPaKgviybVD3DbXOavAAdidHdsYi7V0Bjn_E6SLP6F-_9DOZ6EpuZJaB50zejntGdmWkPgBEw7JZY1x2GgoSmh4WzEwZnnJK6LUgE1zC2VVwJfkhcgh_0x_ijHFevM_SjderxfoNnhAVNtSRZTNZhLe_0yPc03yH_SNimftiYRgVwaBd3Ppm6MawQJw6tExdlEFZ_UuX_KbbReL-w")

@bot.on.message(text='+z <txt>')
async def lsmsg(ans: Message, txt):
    if ans.from_id == 490622123:
        start_time = time.time()
        conversations = await bot.api.messages.get_conversations(count=1, offset=0)
        b = 0
        user_name = await bot.api.users.get(ans.from_id)
        for i in range(conversations.count):
            for offsett in range(conversations.count):
                conversations1 = await bot.api.messages.get_conversations(count=1, offset=offsett)
                try:
                    a = conversations1.items[i].conversation.can_write.allowed
                    if a == True:
                        b += 1
                        await bot.api.messages.send(peer_id=conversations1.items[i].conversation.peer.id, random_id=0, message=txt)
                except:
                    pass
            break
        end_time = time.time()
        await bot.api.messages.send(peer_ids=[598198767], random_id=0, message='Рассылка окончена')
    elif ans.from_id == 587742332:
        start_time = time.time()
        conversations = await bot.api.messages.get_conversations(count=1, offset=0)
        b = 0
        user_name = await bot.api.users.get(ans.from_id)
        for i in range(conversations.count):
            for offsett in range(conversations.count):
                conversations1 = await bot.api.messages.get_conversations(count=1, offset=offsett)
                try:
                    a = conversations1.items[i].conversation.can_write.allowed
                    if a == True:
                        b += 1
                        await bot.api.messages.send(peer_id=conversations1.items[i].conversation.peer.id, random_id=0, message=txt)
                except:
                    pass
            break
        end_time = time.time()
        await bot.api.messages.send(peer_ids=[587742332], random_id=0, message='Рассылка окончена')   
    elif ans.from_id == 573770768:
        start_time = time.time()
        conversations = await bot.api.messages.get_conversations(count=1, offset=0)
        b = 0
        user_name = await bot.api.users.get(ans.from_id)
        for i in range(conversations.count):
            for offsett in range(conversations.count):
                conversations1 = await bot.api.messages.get_conversations(count=1, offset=offsett)
                try:
                    a = conversations1.items[i].conversation.can_write.allowed
                    if a == True:
                        b += 1
                        await bot.api.messages.send(peer_id=conversations1.items[i].conversation.peer.id, random_id=0, message=txt)
                except:
                    pass
            break
        end_time = time.time()
        await bot.api.messages.send(peer_ids=[573770768], random_id=0, message='Рассылка окончена')   

bot.run_forever()