import telebot
import config
import random
import copy

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

main = {'А': ["Абаза", "Абакан", "Абдулино", "Абердин", "Абиджан", "Афины", "Ахалцихе", "Ахен", "Ахмадабад", "Ахмаднагар", "Ахтубинск"],
'Б': ["Бабаево", "Бабушкин", "Бавлы", "Багдад", "Бакал", "Белгород", "Белград", "Белебей", "Белёв"],
'В': ["Вадодара", "Валдай", "Валенсия", "Валуйки", "Варна", "Варшава", "Вашингтон", "Веймар", "Вена", "Венеция"],
'Г': ["Гаага", "Габала", "Габалдон", "Габане", "Габартов", "Габес", "Габилей", "Габиче-Маре", "Габороне Габри"],
'Д': ["Дета", "Детва", "Детройт", "Деттельбах", "Детчино", "Деуба", "Дехак", "Данблейн", "Данвилл", "Данвиль"],
'Е': ["Еббибу", "Евла", "Евлах", "Евлашево", "Евле", "Евпатория", "Егвард", "Егорлыкская", "Егорьевск", "Едвабне"],
'Ж': ["Жамблу", "Жампрука", "Жан-Рабель", "Жанаозен", "Жанатас", "Жанауба", "Жангада", "Жесеаба", "Жет", "Жетулина"],
'З': ["Закигандж", "Закличин", "Закопане", "Закрочим", "Заксенхаген", "Заксенхайм", "Закупи", "Залалёвё", "Залари"],
'И': ["Инсурэцей", "Инта", "Интань", "Интенденте-Альвеар", "Интибука", "Инторсура-Бузэулуй", "Исеть", "Исехара Инувик"],
'Й': ["Йеллоунайф", "Йена", "Йенбай"],
'К': ["Кабугао", "Кабударе", "Кабуйяро", "Кабукгаян", "Кабул", "Кабунталан", "Кабусао", "Кабуянда"],
'Л': ["Ла-Ринконада", "Ла-Риоха", "Ла-Робла", "Ла-Рода", "Ла-Рода-де-Андалусиа", "Ла-Рока-дель-Вальес", "Ла-Ромаин Ла-Романа"],
'М': ["Мадрид", "Мадридехос", "Мадурай", "Мадхавпур", "Мадхепура", "Мадхубани", "Мадхугири", "Мадхукхали", "Мадхупур"],
'Н': ["Нaма", "Нааван", "Наама", "Наантали", "Набаван", "Набадвип", "Набарангпур", "Набари", "Набару", "Набас"],
'О': ["Ознаго", "Озоппо", "Озориу", "Озоркув", "Озуар-ля-Феррьер", "Озургети", "Озуэстри", "Оиба", "Оиката"],
'П': ["Падарауна", "Падасука", "Паденге-суль-Гарда", "Падер", "Падерборн", "Падерно-д'Адда", "Падерно-Дуньяно", "Падерно-Франчьякорта", "Падилья"],
'Р': ["Ракитово", "Ракка", "Раккониги", "Рако-Рахо", "Раковник", "Раковски", "Раконевице", "Ракопс", "Раксаул-Базар", "Ралстон"],
'С': ["Салгаду", "Филью", "Салгаду-ди-Сан-Фелис", "Салгар", "Салгейру", "Салданья", "Салданья-Маринью", "Салдус", "Сале", "Сале-Маразино"],
'Т': ["Тайжина", "Тайлай", "Тайлак", "Тайландия", "Тайлер", "Тайнань", "Тайнмут", "Тайно", "Тайо", "Тайобейрас", "Тайога", "Тайоло"],
'У': ["Утрехт", "Утта", "Утулау", "Утхирамерур", "Утьель", "Уусикаарлепюу", "Уусикаупунки", "Уфа"],
'Ф': ["Фальцес", "Фальчёпинг", "Фальчьяно-дель-Массико", "Фама", "Фамагуста", "Фамаильа"],
'Х': ["Халинув", "Халкабад", "Халкида", "Халлайн", "Халле", "Халленберг", "Халлоуэлл", "Халль-ин-Тироль", "Халльштадт", "Халонг"],
'Ц': ["Цецебджве", "Цешанув", "Цешин", "Цзаочжуан", "Цзесю"],
'Ч': ["Чавакачери", "Чавинь", "Чаглаянджерит", "Чагода", "Чагуанас", "Чагуани", "Чадан", "Чадеган"],
'Ш': ["Шанталь", "Шанхай", "Шанхассен", "Шанцю", "Шанчжи", "Шаншере", "Шаньвэй", "Шаньтоу", "Шаогуань"],
'Щ': ["Щёкино", "Щекоцины", "Щелкино", "Щёлково", "Щербинка"],
'Ы': ["Ыйджу", "Ыйрён", "Ыйсон"],
'Э': ["Экс-ле-Бен", "Эксетер", "Эксмор", "Эксмут", "Экуадор", "Экуок", "Экшё", "Эланкур", "Элберт-Таун", "Элбертвилл", "Элва"],
'Ю': ["Юбари", "Юберлинген", "Юбилейный", "Ювяскюля"],
'Я': ["Ямагути", "Яманаси", "Ямаса", "Ямато", "Яматокорияма", "Яматотакада", "Ямбио", "Ямбол", "Яме"]}

words = ['ЪЪЪ', 'ЪЪЪ', 'ЪЪЪ']

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('static/hello.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
	item1 = types.KeyboardButton("Начать игру")
	item2 = types.KeyboardButton("Закончить игру")

	markup.add(item1, item2)	

	bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - бот с именем {1.first_name}. Создан, чтобы играть с тобой в города :3".format(message.from_user, bot.get_me()), reply_markup=markup)

cities = copy.deepcopy(main) ###

@bot.message_handler(content_types=['text'])
def lalala(message):

	global cities ###
	
	if message.text == 'Начать игру':
		sti = open('static/lets_start.webp', 'rb')
		bot.send_sticker(message.chat.id, sti)
		bot.send_message(message.chat.id, "Хорошо, начинайте")
		words.append('ЪЪЪ')
		words.append('ЪЪЪ')
		words.append('ЪЪЪ')

		cities = copy.deepcopy(main) ###

	elif message.text == 'Закончить игру':
		sti = open('static/bye.webp', 'rb')
		bot.send_sticker(message.chat.id, sti)
		bot.send_message(message.chat.id, "Спасибо за игру, мне было весело. Надеюсь вам тоже)")
		words.clear()

		cities.clear() ###

	elif len(words)!=0 and message.text[0] != words[-1][-1].upper() and words[-1][-1].upper()!='Ъ' and words[-1][-1].upper()!='Ь':
		bot.send_message(message.chat.id, "Похоже, что вы сказали слово не на ту букву.")

	elif message.text[-1].upper() in cities and len(cities[message.text[-1].upper()])!=0:
		x = random.choice(cities[message.text[-1].upper()])
		bot.send_message(message.chat.id, x)
		d = cities[message.text[-1].upper()].index(x)
		cities[message.text[-1].upper()].pop(d)
		words.append(x)

	elif message.text[-1].upper() == 'Ь' and len(cities[message.text[-2].upper()])!=0:
		x = random.choice(cities[message.text[-2].upper()])
		bot.send_message(message.chat.id, x)
		d = cities[message.text[-2].upper()].index(x)
		cities[message.text[-2].upper()].pop(d)
		words.append(x)
	
	else:
		bot.send_message(message.chat.id, "Извините, я не знаю, что ответить(\nЧтобы начать новую игру нажмите 'Начать игру'")

# RUN
bot.polling(none_stop=True)