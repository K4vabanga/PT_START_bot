import logging
import re
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
import paramiko
import psycopg2
from psycopg2 import Error
import os
#from dotenv import load_dotenv

#load_dotenv()

TMP = []
connection = None

host = os.getenv('HOST')
port = os.getenv('PORT')
username = os.getenv('USER')
password = os.getenv('PASSWORD')

db_user=os.getenv('DBUSER')
db_password=os.getenv('DBPASSWORD')
db_host=os.getenv('DBHOST')
db_port=os.getenv('DBPORT')
db_database=os.getenv('DBNAME')

TOKEN = os.getenv('TOKEN')

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


def get_release(update: Update, context):
    client.connect(hostname=host, username=username, password=password, port=port)
    logging.debug('SSH conected')
    stdin, stdout, stderr = client.exec_command('cat /etc/os-release')
    data = stdout.read() + stderr.read()
    client.close()
    data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
    update.message.reply_text(data)
    logging.debug('get_release succes')

def get_uname(update: Update, context):
    client.connect(hostname=host, username=username, password=password, port=port)
    logging.debug('SSH conected')
    stdin, stdout, stderr = client.exec_command('uname -a')
    data = stdout.read() + stderr.read()
    client.close()
    data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
    update.message.reply_text(data)
    logging.debug('get_uname succes')

def get_uptime(update: Update, context):
    client.connect(hostname=host, username=username, password=password, port=port)
    logging.debug('SSH conected')
    stdin, stdout, stderr = client.exec_command('uptime')
    data = stdout.read() + stderr.read()
    client.close()
    data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
    update.message.reply_text(data)
    logging.debug('get_uptime succes')

def get_df(update: Update, context):
    client.connect(hostname=host, username=username, password=password, port=port)
    logging.debug('SSH conected')
    stdin, stdout, stderr = client.exec_command('LANG=en_US.UTF-8 df')
    data = stdout.read() + stderr.read()
    client.close()
    data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
    update.message.reply_text(data)
    logging.debug('get_df succes')

def get_free(update: Update, context):
    client.connect(hostname=host, username=username, password=password, port=port)
    logging.debug('SSH conected')
    stdin, stdout, stderr = client.exec_command('LANG=en_US.UTF-8 free')
    data = stdout.read() + stderr.read()
    client.close()
    data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
    update.message.reply_text(data)
    logging.debug('get_free succes')

def get_mpstat(update: Update, context):
    client.connect(hostname=host, username=username, password=password, port=port)
    logging.debug('SSH conected')
    stdin, stdout, stderr = client.exec_command('LANG=en_US.UTF-8 mpstat')
    data = stdout.read() + stderr.read()
    client.close()
    data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
    update.message.reply_text(data)
    logging.debug('get_mpstat succes')

def get_w(update: Update, context):
    client.connect(hostname=host, username=username, password=password, port=port)
    logging.debug('SSH conected')
    stdin, stdout, stderr = client.exec_command('LANG=en_US.UTF-8 w')
    data = stdout.read() + stderr.read()
    client.close()
    data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
    update.message.reply_text(data)
    logging.debug('get_w succes')

def get_auths(update: Update, context):
    client.connect(hostname=host, username=username, password=password, port=port)
    logging.debug('SSH conected')
    stdin, stdout, stderr = client.exec_command('LANG=en_US.UTF-8 last -n 10')
    data = stdout.read() + stderr.read()
    client.close()
    data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
    update.message.reply_text(data)
    logging.debug('get_auths succes')

def get_critical(update: Update, context):
    client.connect(hostname=host, username=username, password=password, port=port)
    logging.debug('SSH conected')
    stdin, stdout, stderr = client.exec_command('LANG=en_US.UTF-8 journalctl -p crit -n 5')
    data = stdout.read() + stderr.read()
    client.close()
    data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
    update.message.reply_text(data)
    logging.debug('get_critical succes')

def get_ps(update: Update, context):
    client.connect(hostname=host, username=username, password=password, port=port)
    logging.debug('SSH conected')
    stdin, stdout, stderr = client.exec_command('LANG=en_US.UTF-8 ps aux')
    data = stdout.read() + stderr.read()
    client.close()
    data = (str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1])[:4000]
    update.message.reply_text(data)
    logging.debug('get_ps succes')

def get_ss(update: Update, context):
    client.connect(hostname=host, username=username, password=password, port=port)
    logging.debug('SSH conected')
    stdin, stdout, stderr = client.exec_command('LANG=en_US.UTF-8 ss -tuln')
    data = stdout.read() + stderr.read()
    client.close()
    data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
    update.message.reply_text(data)
    logging.debug('get_ss succes')

def get_apt_list(update: Update, context):
    client.connect(hostname=host, username=username, password=password, port=port)
    logging.debug('SSH conected')
    stdin, stdout, stderr = client.exec_command('LANG=en_US.UTF-8 apt list --installed')
    data = stdout.read() + stderr.read()
    client.close()
    data = (str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1])[:4000]
    update.message.reply_text(data)
    logging.debug('get_apt_list succes')

def get_services(update: Update, context):
    client.connect(hostname=host, username=username, password=password, port=port)
    logging.debug('SSH conected')
    stdin, stdout, stderr = client.exec_command('LANG=en_US.UTF-8 systemctl list-units --type=service')
    data = stdout.read() + stderr.read()
    client.close()
    data = (str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1])[:4000]
    update.message.reply_text(data)
    logging.debug('get_services succes')

def get_repl_logs(update: Update, context):
    client.connect(hostname=host, username=username, password=password, port=port)
    logging.debug('SSH conected')
    stdin, stdout, stderr = client.exec_command(f"LANG=en_US.UTF-8 echo '{password}' | sudo -S docker logs -n 40 db")
    data = stdout.read() + stderr.read()
    client.close()
    data = (str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1])[:4000]
    update.message.reply_text(data)
    logging.debug('get_repl_logs succes')

def get_emails(update: Update, context):
    try:
        connection = psycopg2.connect(user=db_user,
                                    password=db_password,
                                    host=db_host,
                                    port=db_port, 
                                    database=db_database)

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM emails;")
        EmailList = cursor.fetchall()
        Emails = 'ID    Email\n' # Создаем строку, в которую будем записывать email
        for i in range(len(EmailList)):
            Emails += f'{EmailList[i][0]}. {EmailList[i][1]}\n' # Записываем очередной email
        update.message.reply_text(Emails)
        logging.debug('get_emails succes')
    except (Exception, Error) as error:
        update.message.reply_text('Не удалось выполнить: %s', error)
        logging.error("Ошибка при работе с PostgreSQL: %s", error)
    finally:
        if connection is not None:
            cursor.close()
            connection.close()
            logging.info("Соединение с PostgreSQL закрыто")

def get_phone_numbers(update: Update, context):
    try:
        connection = psycopg2.connect(user=db_user,
                                    password=db_password,
                                    host=db_host,
                                    port=db_port, 
                                    database=db_database)

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM phones;")
        PhoneList = cursor.fetchall()
        Phones = 'ID    PhoneNumber\n' # Создаем строку, в которую будем записывать phone
        for i in range(len(PhoneList)):
            Phones += f'{PhoneList[i][0]}. {PhoneList[i][1]}\n' # Записываем очередной phone
        update.message.reply_text(Phones)
        logging.debug('get_phone_numbers succes')
    except (Exception, Error) as error:
        update.message.reply_text('Не удалось выполнить: %s', error)
        logging.error("Ошибка при работе с PostgreSQL: %s", error)
    finally:
        if connection is not None:
            cursor.close()
            connection.close()
            logging.info("Соединение с PostgreSQL закрыто")

def start(update: Update, context):
    user = update.effective_user
    update.message.reply_text(f'Привет {user.full_name}!')
    logging.debug('Bot started')

'''def get_apt_listComand(update: Update, context):
    update.message.reply_text('Введите название пакета:')
    logging.debug('get_apt_listComand asked')
    return 'get_apt_list' '''

def helpCommand(update: Update, context):
    update.message.reply_text('/start\n/help\n/find_email\n/find_phone_number\n/verify_password')
    logging.debug('Help asked')


def findEmailCommand(update: Update, context):
    update.message.reply_text('Введите текст для поиска email: ')
    logging.debug('TextEmail bot ask')
    return 'findEmail'

def findPhoneNumbersCommand(update: Update, context):
    update.message.reply_text('Введите текст для поиска телефонных номеров: ')
    logging.debug('TextPhone bot ask')
    return 'findPhoneNumbers'

def VerifyPasswordCommand(update: Update, context):
    update.message.reply_text('Введите пароль для проверки его сложности: ')
    logging.debug('Passwd bot ask')
    return 'VerifyPassword'

'''def get_apt_list (update: Update, context):
    user_input = update.message.text
    logging.debug('get_apt_list get ans')
    client.connect(hostname=host, username=username, password=password, port=port)
    logging.debug('SSH conected')
    stdin, stdout, stderr = client.exec_command('LANG=en_US.UTF-8 apt-cache show {user_input}')
    data = stdout.read() + stderr.read()
    client.close()
    data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
    update.message.reply_text(data)
    logging.debug('get_apt_list succes')
    return ConversationHandler.END # Завершаем работу обработчика диалога'''

def addEmail (update: Update, context):
    user_input = update.message.text
    logging.debug('addEmail get ans')
    if user_input == 'Да':
        try:
            connection = psycopg2.connect(user=db_user,
                                        password=db_password,
                                        host=db_host,
                                        port=db_port, 
                                        database=db_database)

            cursor = connection.cursor()
            for i in range (len(TMP)):
                cursor.execute(f"INSERT INTO emails (Email) VALUES ('{TMP[i]}');")
                connection.commit()
            update.message.reply_text('Адреса успешно добавлены!')
            logging.debug('addEmail succes')
        except (Exception, Error) as error:
            update.message.reply_text('Не удалось выполнить: %s', error)
            logging.error("Ошибка при работе с PostgreSQL: %s", error)
        finally:
            if connection is not None:
                cursor.close()
                connection.close()
                logging.info("Соединение с PostgreSQL закрыто")
        return ConversationHandler.END # Завершаем работу обработчика диалог
    elif user_input == 'Нет':
        update.message.reply_text('ОК 👌')
        logging.debug('Отказ addEmail')
        return ConversationHandler.END # Завершаем работу обработчика диалога
    else:
        update.message.reply_text('Некоректный ввод')
        logging.error('Некоректный ввод addEmail')
        return ConversationHandler.END # Завершаем работу обработчика диалога

def findEmail (update: Update, context):
    global TMP
    user_input = update.message.text # Получаем текст, содержащий(или нет) почту
    logging.debug('TextEmail get ans')
    EmailRegex = re.compile(r'[a-zA-Z0-9.]+@[a-z]+\.[a-z]+') # формат abc@abc.abc

    EmailList = EmailRegex.findall(user_input) # Ищем email
    TMP = EmailList
    if not EmailList: # Обрабатываем случай, когда email нет
        logging.debug('No email in text')
        update.message.reply_text('Email не найдены')
        return ConversationHandler.END# Завершаем выполнение функции
    
    Emails = '' # Создаем строку, в которую будем записывать email
    for i in range(len(EmailList)):
        Emails += f'{i+1}. {EmailList[i]}\n' # Записываем очередной email
        
    update.message.reply_text(Emails+'\nХотите сохранить найденые email в базу данных? (Да/Нет)')# Отправляем сообщение пользователю
    logging.debug('TextEmail sent ans')
    return 'addEmail'

def addPhoneNumbers (update: Update, context):
    user_input = update.message.text
    logging.debug('addPhoneNumbers get ans')
    if user_input == 'Да':
        try:
            connection = psycopg2.connect(user=db_user,
                                        password=db_password,
                                        host=db_host,
                                        port=db_port, 
                                        database=db_database)

            cursor = connection.cursor()
            for i in range (len(TMP)):
                cursor.execute(f"INSERT INTO phones (PhoneNumber) VALUES ('{TMP[i]}');")
                connection.commit()
            update.message.reply_text('Номер успешно добавлены!')
            logging.debug('addPhoneNumbers succes')
        except (Exception, Error) as error:
            update.message.reply_text('Не удалось выполнить: %s', error)
            logging.error("Ошибка при работе с PostgreSQL: %s", error)
        finally:
            if connection is not None:
                cursor.close()
                connection.close()
                logging.info("Соединение с PostgreSQL закрыто")
        return ConversationHandler.END # Завершаем работу обработчика диалог
    elif user_input == 'Нет':
        update.message.reply_text('ОК 👌')
        logging.debug('Отказ addPhoneNumbers')
        return ConversationHandler.END # Завершаем работу обработчика диалога
    else:
        update.message.reply_text('Некоректный ввод')
        logging.error('Некоректный ввод addPhoneNumbers')
        return ConversationHandler.END # Завершаем работу обработчика диалога

def findPhoneNumbers (update: Update, context):
    global TMP
    TMP = []
    user_input = update.message.text # Получаем текст, содержащий(или нет) номера телефонов
    logging.debug('TextPhoneNumbers get ans')
    phoneNumRegex = re.compile(r'(8|\+7)( |-)?(\(\d{3}\)|\d{3})( |-)?(\d{3}-\d{2}-\d{2}|\d{7}|\d{3} \d{2} \d{2})')

    phoneNumberList = phoneNumRegex.findall(user_input) # Ищем номера телефонов
    logging.debug(phoneNumberList)
    if not phoneNumberList: # Обрабатываем случай, когда номеров телефонов нет
        logging.debug('No PhoneNumbers in text')
        update.message.reply_text('Телефонные номера не найдены')
        return # Завершаем выполнение функции
    
    phoneNumbers = '' # Создаем строку, в которую будем записывать номера телефонов
    for i in range(len(phoneNumberList)):
        phoneNumbers += f'{i+1}. '
        tmp = ''
        for j in range(len(phoneNumberList[i])):
            phoneNumbers += f'{phoneNumberList[i][j]}' # Записываем очередной номер
            tmp += f'{phoneNumberList[i][j]}'
        TMP.append(tmp)
        phoneNumbers += f'\n'
        
    update.message.reply_text(phoneNumbers + '\nХотите сохранить найденые номера в базу данных? (Да/Нет)') # Отправляем сообщение пользователю
    logging.debug('TextPhoneNumbers sent ans')
    return 'addPhoneNumbers' # Завершаем работу обработчика диалога

def PSWD(user_input):
    PasswdRegex1 = re.compile(r'.{8}+')
    PasswdRegex2 = re.compile(r'[A-Z]+')
    PasswdRegex3 = re.compile(r'[a-z]+')
    PasswdRegex4 = re.compile(r'[0-9]+')
    PasswdRegex5 = re.compile(r'[!@#$%^&*()]+')
    if not PasswdRegex1.search(user_input):
        raise Exception('Пароль должен содержать не менее восьми символов.')
    if not PasswdRegex2.search(user_input):
        raise Exception('Пароль должен включать как минимум одну заглавную букву (A–Z).')
    if not PasswdRegex3.search(user_input):
        raise Exception('Пароль должен включать хотя бы одну строчную букву (a–z).')
    if not PasswdRegex4.search(user_input):
        raise Exception('Пароль должен включать хотя бы одну цифру (0–9).')
    if not PasswdRegex5.search(user_input):
        raise Exception('Пароль должен включать хотя бы один специальный символ, такой как !@#$%^&*().')

    return 1
    

def VerifyPassword (update: Update, context):
    user_input = update.message.text # Получаем текст, c паролем
    logging.debug('Passwd get ans')
    try:
        ans = PSWD(user_input)
    except Exception as err:
        update.message.reply_text('Пароль простой: ' + str(err))
    if ans:
        update.message.reply_text('Пароль сложный')
    logging.debug('Passwd sent ans')
    return ConversationHandler.END # Завершаем работу обработчика диалога


def echo(update: Update, context):
    update.message.reply_text(update.message.text)
    logging.debug('Echo ans')


def main():
    updater = Updater(TOKEN, use_context=True)

    # Получаем диспетчер для регистрации обработчиков
    dp = updater.dispatcher

    # Обработчик диалога email
    convHandlerFindEmails = ConversationHandler(
        entry_points=[CommandHandler('find_email', findEmailCommand)],
        states={
            'findEmail': [MessageHandler(Filters.text & ~Filters.command, findEmail)],
            'addEmail': [MessageHandler(Filters.text & ~Filters.command, addEmail)]
        },
        fallbacks=[]
    )

    # Обработчик диалога phone
    convHandlerFindPhoneNumbers = ConversationHandler(
        entry_points=[CommandHandler('find_phone_number', findPhoneNumbersCommand)],
        states={
            'findPhoneNumbers': [MessageHandler(Filters.text & ~Filters.command, findPhoneNumbers)],
            'addPhoneNumbers': [MessageHandler(Filters.text & ~Filters.command, addPhoneNumbers)]
        },
        fallbacks=[]
    )

    # Обработчик диалога passwd
    convHandlerVerifyPassword = ConversationHandler(
        entry_points=[CommandHandler('verify_password', VerifyPasswordCommand)],
        states={
            'VerifyPassword': [MessageHandler(Filters.text & ~Filters.command, VerifyPassword)],
        },
        fallbacks=[]
    )

    # Обработчик диалога apt
    '''
    convHandlerAPT = ConversationHandler(
        entry_points=[CommandHandler('get_apt_list', get_apt_listComand)],
        states={
            'get_apt_list': [MessageHandler(Filters.text & ~Filters.command, get_apt_list)],
        },
        fallbacks=[]
    )
    '''	
    # Регистрируем обработчики команд
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", helpCommand))
    dp.add_handler(convHandlerFindEmails)
    dp.add_handler(convHandlerFindPhoneNumbers)
    dp.add_handler(convHandlerVerifyPassword)
    dp.add_handler(CommandHandler("get_release", get_release))
    dp.add_handler(CommandHandler("get_uname", get_uname))
    dp.add_handler(CommandHandler("get_uptime", get_uptime))
    dp.add_handler(CommandHandler("get_df", get_df))
    dp.add_handler(CommandHandler("get_free", get_free))
    dp.add_handler(CommandHandler("get_mpstat", get_mpstat))
    dp.add_handler(CommandHandler("get_w", get_w))
    dp.add_handler(CommandHandler("get_auths", get_auths))
    dp.add_handler(CommandHandler("get_critical", get_critical))
    dp.add_handler(CommandHandler("get_ps", get_ps))
    dp.add_handler(CommandHandler("get_ss", get_ss))
    dp.add_handler(CommandHandler("get_apt_list", get_apt_list))
    #dp.add_handler(convHandlerAPT)
    dp.add_handler(CommandHandler("get_services", get_services))
    dp.add_handler(CommandHandler("get_emails", get_emails))
    dp.add_handler(CommandHandler("get_phone_numbers", get_phone_numbers))
    dp.add_handler(CommandHandler("get_repl_logs", get_repl_logs))
		
	# Регистрируем обработчик текстовых сообщений
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
		
	# Запускаем бота
    updater.start_polling()

	# Останавливаем бота при нажатии Ctrl+C
    updater.idle()


if __name__ == '__main__':
    main()
