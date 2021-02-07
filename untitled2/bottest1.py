import vk_api, random, time
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import  datetime
import tok
token=tok.tokkate()
vk_session=vk_api.VkApi(token=token)

session_api=vk_session.get_api()
longpoll=VkLongPoll(vk_session)
x,mess1,cit="",[],0
hell=["сап, крошка", "привет, детка", "здаров", "миллион приветов", "ку", "ну привет","тебя приветсвую","привет, слушаю...","хола"]
def sender(id, text):
    vk_session.method("messages.send", {"user_id" : id, "message" : text, "random_id":0})
def pluselem(idd,simph,plus,minus,col,mess1,pred,post,cit,x):
    for i in range(len(mess1)):
        if mess1[i] == simph: cit += 1
        if cit == len(mess):
            kell=len(mess)
            if plus==True: kell+=col
            if minus==True: kell-=col
            for i in range(kell): x += simph;
            sender(idd, pred+x+post)

while True:
    for event in longpoll.listen():
        if event.type==VkEventType.MESSAGE_NEW:
            print("сообщение пришло в ", datetime.strftime(datetime.now(), "%H:%M:%S"))
            print(event.user_id," текст сообщения: ", event.text)
            mess=event.text.lower();mess1=list(mess);lenmess=len(mess1);
            if event.from_user and not (event.from_me):
                if mess == "привет" or mess == "сап" or mess =="ку" or mess =="здаров":sender(event.user_id, hell[random.randint(0,len(hell)-1)])
                elif mess == "что делаешь?" or mess == "что делаешь":sender(event.user_id, "веселюсь с мамой владика а4")
                elif mess == "как дела?" or mess == "как дела":sender(event.user_id, "дрочу в ванной")
                elif mess == "вася":sender(event.user_id, "да-да?")
                elif mess == "пошел нахуй" or mess == "пошёл нахуй" or mess == "иди нахуй":sender(event.user_id, "говна наверни, пидор")
                elif mess == "ты не можешь написать симфонию":sender(event.user_id, "а ты?")
                elif mess == "да":sender(event.user_id, "пизда")
                elif mess == "нет":sender(event.user_id, "пидора ответ")
                elif mess == "ок":sender(event.user_id, "хуйок")
                elif mess == "ч" or mess == "чё" or mess == "че" or mess == "чё?" or mess == "че?" or mess == "ч?":sender(event.user_id, "в очо")
                elif mess == "шлюхи аргумент":sender(event.user_id, "аргумент не нужен пидор обнаружен")
                elif mess == "ты не можешь написать симфонию":sender(event.user_id, "а ты?")
                elif mess == "алё":sender(event.user_id, "хуем по лбу не далё?")
                elif mess == "але":sender(event.user_id, "хуем по лбу не дале?")
                elif mess == "ало":sender(event.user_id, "хуем по лбу не дало?")
                elif mess == "хуй":sender(event.user_id, "пизда?")
                elif mess == "пизда":sender(event.user_id, "хуй?")
                elif mess == "бота?":sender(event.user_id, "нет блять тебя, сынок ёбаный")
                elif mess == "он хорош" or mess=="ты хорош":sender(event.user_id, "твоя мама лучше")
                elif mess == "соси яйца" or mess == "лижи яйца":sender(event.user_id, "давай, давай их сюда")
                elif mess == "лижи писю" or mess == "лижи пизду" or mess == "соси пизду" or mess == "лижи писечку" or mess == "лижи писячку" or mess == "лижи писичку":sender(event.user_id, "мммм... присаживайся мне на личико")
                elif mess == "соси хуй":sender(event.user_id, "ахахахаха, и до зуба не достанешь")
                elif mess == "слит":sender(event.user_id, "слит? как конча твоего бати в туалет? в которой мог оказаться и ты, ущерб?")
                elif mess == "утро доброе":sender(event.user_id, "доброе утро")
                elif mess == "доброе утро":sender(event.user_id, "утро доброе")
                elif mess == "день добрый":sender(event.user_id, "добрый день")
                elif mess == "добрый день":sender(event.user_id, "день добрый")
                elif mess == "хуй на":sender(event.user_id, "а?")
                elif mess == "го":sender(event.user_id, "збс")
                elif mess == "буду знать" or mess == "учту" or mess == "хорошо, учту" or mess == "буду знать" or mess=="ладно, учту" or mess == "хорошо, буду знать" or mess == "ладно буду знать" or mess == "ладно учту" or mess == "хорошо буду знать" or mess == "хорошо учту":sender(event.user_id, "день добрый")
                elif mess == "лох" or mess == "пидор" or mess == "ты лох"  or mess == "ты пидор":sender(event.user_id, "ок")
                elif mess == "ладно":sender(event.user_id, "прохладно епта")
                elif mess == "брат" or mess == "братик":sender(event.user_id, "семпай?")
                elif mess == "понял":sender(event.user_id, "вот и славно")
                elif mess == "короче" or mess == "короч" or mess == "кароче" or mess == "кароч" or mess == "крч":sender(event.user_id, "длиннее епта")
                elif mess == "seenbreaker0.5":time.sleep(1800)
                elif mess == "seenbreaker1":time.sleep(3600)
                elif mess == "seenbreaker2":time.sleep(7200)
                elif mess == "полина":sender(event.user_id, "дрочу на неё 24/7")
                pluselem(event.user_id,'?',True,False,1,mess1,"","",cit,x)
                pluselem(event.user_id, 'а', False, False, 0, mess1,"хуй н","",cit,x)
                pluselem(event.user_id, ')', True, False, 1, mess1, "","", cit, x)
                pluselem(event.user_id, '(', True, False, 1, mess1, "", "", cit, x)
                pluselem(event.user_id, 'е', False, False, 0, mess1, "по пизд","", cit, x)






#"привет" or "сап" or "ку" or "здаров"