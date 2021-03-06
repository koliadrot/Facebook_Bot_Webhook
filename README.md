EN:

Facebook Bot with Webhook

The main task of this bot, to respond to user requests, which can be easily added.
See repository - https://github.com/koliadrot/Telegram_Bot_Webhook

This bot works as follows: A bot accepts a request from a Facebook server and the bot processes the data,
sent to the server.

This method is effective compared to the reverse method of Webhook (the bot itself requests (spam) facebook server,
and facebook the server is responsible for it), since the delay between the bot and the server almost disappears and
disappears satisfactory results that could pass between requests.

Useful notes to get started:
1. Do not forget to insert your Facebook token ("Page", not "user") in the data_api_bot file - the variable "token"

2. The bot itself was placed on the site of the service - https://www.pythonanywhere.com
   The cost of the service is free, you only need to renew it every 3 months, it is also free!

Details about the methods of Facebook bot look at - https://developers.facebook.com/docs/pages

Useful material for developing user access - https://towardsdatascience.com/how-to-use-facebook-graph-api-and-extract-data-using-python-1839e19d6999

Attention!!!

There are two types of Facebook bots:
1. Bot with user access key
2. Bot with community access key


This example uses a bot with a community key.

To make your bot available to all users of the community, you need to send your application for review!

RU: 

Facebook Бот с Webhook 

Главная задача этого бота, отвечать на запросы пользователей,которые могут быть легко добавлены.
Смотри хранилище(репозиторий) - https://github.com/koliadrot/Telegram_Bot_Webhook 

Данный бот работает по следующему принципу: Бот принимает запрос от Facebook сервера и бот обрабатывая дан- 
ные, отправляет данные серверу. 

Данный метод эффективен по сравнению с методом обратному Webhook(Бот сам запрашивает(спамит) facebook сервер, 
а facebook сервер ему отвечает), так как задержка между ботом и сервером практически исчезает и пропадают 
не удовлетворительные результаты, которые могли проходить между запросами. 

Полезные заметки для начала работы: 
1. Не забудьте вставить ваш токен ("page", а не "user") Facebook в файле data_api_bot - переменная "token"

2. Сам бот размещался на сайте сервиса - https://www.pythonanywhere.com
   Стоимость услуги бесплатная, нужно только каждые 3 месяца продливать, это тоже бесплатно!

Подробно о методах Facebook бота смотреть на - https://developers.facebook.com/docs/pages

Полезный материал по созданию бота с ключом доступа пользователя - https://towardsdatascience.com/how-to-use-facebook-graph-api-and-extract-data-using-python-1839e19d6999

Важно!!!
Есть два типа ботов Facebook:
1. Бот с ключом доступа пользователя
2. Бот с ключом доступа сообщества

В данном примере используется бот с ключом сообщества.
Чтобы ваш бот стал доступным для всех пользователей сообщества, вам нужно отправить на проверку ваше приложение!

