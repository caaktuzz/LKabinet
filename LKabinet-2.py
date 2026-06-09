
import time
import random

print('ℹ️  система : start')

# база данных администраторов
admins = {
   'admin01' : {'code': '1378'}
 }

# база данных пользователей 
users = {
 # id 
    'idishki' : {
     1000 : {1000},
     1001 : {1001},
     1002 : {1002},
    },
 # full info 
    "Nikola" : {
        "full name": "Nikolay Artyushenkov",
        "password": "1234",
        "age": 32,
        "email": "nikola@ya.ru",
        'id': 1000,
        "status": 'Active'
                },
    "Artur" : {
        "full name": "Artur Migrant",
        "password": "1234",
        "age": 45,
        "email": "arturchek@ya.ru",
        'id': 1001,
        "status": 'Active'
                },
    "Evgeniy" : {
        "full name": "Evgeniy Norvegiya",
        "password": "1234",
        "age": 39,
        "email": "evgesha@ya.ru",
        'id': 1002,
        "status": 'Blocked'
                },    
    }

# жалобы пользователей
complaints = {}

time.sleep(1)
print('  ❗ Проверка систем [1]'), time.sleep(0.1)
print('ℹ️  система : ', users), time.sleep(0.1)
print('ℹ️  система : ', users['Artur']), time.sleep(0.1)
print('ℹ️  система : ', users['Artur']['age']), time.sleep(1)

 # код доступа администратора - admin01 > 1378 
# основная страница

while True:
 print(" - - Основная страница - - ")
 print("[«1»] - Авторизоваться")
 print("[«2»] - *Действие 2*")
 print("[«3»] - *Действие 3*")
 print("[«4»] - *Действие 4*")
 deystvie0 = input(">> ")
 if deystvie0 in admins:
  print("⚠️", " Администратор «01»"), time.sleep(0.5)
  admin_code = input("Введите код доступа: ")
  if admin_code == admins[deystvie0]['code']:
    print("✔️"," Доступ в систему администрирования получен"), time.sleep(1)
    while True: 
      print("[1] - База данных пользователей"), time.sleep(0.1)
      print("[2] - Поиск пользователя"), time.sleep(0.1)
      print("[3] - Жалобы"), time.sleep(0.1)
      print("[4] - История махинаций")
      print("[5] - Выйти")
      deystvie_admina = input('>> ')
      if deystvie_admina == '1':
        print(users)
        time.sleep(5)
        continue
      elif deystvie_admina == '2':
        print('[1] - Назад')
        poisk = input("Введите юзернейм пользователя: ")
        if poisk in users: 
         print("ага, нашли", users[poisk]), time.sleep(0.5)
         print('[1] - Назад'), time.sleep(0.1)
         print('[2] - Заблокировать'), time.sleep(0.1)
         print('[3] - Удалить данные пользователя'), time.sleep(0.1)
         deystvie_admina01 = input('>> ')
         if deystvie_admina01 == '1':
           break
         elif deystvie_admina01 == '2':
          print("❗ Вы действительно хотите заблокировать аккаунт пользователя",poisk,'?')
          print('[1] - Передумал'), time.sleep(0.1)
          print('[2] - Да'), time.sleep(0.1)
          deystvie_admina02 = input('>> ')
          if deystvie_admina02 == '1':
           continue
          elif deystvie_admina02 == '2':
           print("Аккаунт заблокирован")
           users[poisk]['status'] = 'Blocked'
           print(users[poisk])
         elif deystvie_admina01 == '3':
          print("❗ Вы действительно хотите удалить аккаунт пользователя",poisk,'?')
          print('[1] - Передумал'), time.sleep(0.1)
          print('[2] - Да'), time.sleep(0.1)
          deystvie_admina02 = input('>> ')
          if deystvie_admina02 == '1':
            continue
          elif deystvie_admina02 == '2':
           print("Аккаунт удалён")
           del users[poisk]
           print(users), time.sleep(1)
           continue
        elif poisk == '1':
          continue
        else: print("нету таких")

      elif deystvie_admina == '3':
        print(complaints)
      elif deystvie_admina == '5':
       break

  if admin_code != admins[deystvie0]['code']:
    print("❌"," Код неверный"), time.sleep(0.5)
    print("⚠️"," Доступ запрещён"), time.sleep(1)
    continue
  
 if deystvie0 == '1':
   print("[«1»] - Войти в аккаунт")
   print("[«2»] - Создать учётную запись")
   print("[«3»] - Назад")
   deystvie01 = input(">> ")
   if deystvie01 == '3':
     continue

   if deystvie01 == '1':
# авторизация 
    while True:
     print("Войдите в аккаунт")
     print("[«1»] - Назад")
     username1 = input("Введите юзернейм: ")
     if username1 not in users:
      print("Пользователя с таким именем не существует!")
      continue
     if username1 == '1':
      print("назад")
      break
     password1 = input("Введите пароль: ")
     if users[username1]['status'] == 'Active':
        print("Вход в аккаунт совершён успешно")
        log = username1, users[username1]['id']
     if users[username1]['status'] == 'Blocked':
        print('Ваша учётная запись заблокирована!')
        print('[1] - Назад' )
        print('[2] - Написать в поддержку' )
        de1 = input('>> ')
        if de1 == '1':
         continue
        if de1 == '2':
         complaints1 = input("Пожалуйста, опишите вашу проблему: ")
         print("Ваша жалоба зарегистрирована. Скоро модератор рассмотрит её и свяжется с вами!")
         complaints[username1] = {complaints1}
         break
     if username1 in users and users[username1]['password'] == password1:
        print("Вход в аккаунт совершён успешно")
        break
     else:
        print("Неверный логин или пароль. повторите попытку") 
        continue
     
# создание учётной записи 
   if deystvie01 == '2':
    while True:
     print("Создайте учётную запись")
     username1 = input('Введите ваше юзернейм: ')
     if username1 in users :
        print('Пользователь с таким юзернейом уже существует! Попробуйте другой.')
        continue
     name1 = input("Введите ваше настоящее имя: ")
     if len(username1) > 50:
        print("Юзернейм не может содержать более 50 символов! Попробуйте другой.")
     if len(username1) < 3: 
        print("Имя должено может иметь не менее 3-х символов!")
        continue
     password1 = input('Придумайте пароль: ')
     if len(password1) < 4: 
        print("Пароль должен быть не менее 4-х символов!")
        continue
# проврека пользователем введенных данных
     print("Подтвердите корректность данных: ")
     print("Никнейм:", username1)
     print("Имя:", name1)
     print("Пароль:", password1)

     correct = input("Введите «1», если всё верно, или «2», если хотите изменить: ")
     if correct == "1":
      print('Аккаунт зарегистрирован')
      # определение айди последнего зарегистрировавшегося пользователя
      last_element = list(users.items())[-1]
      # привязка айди
      id1 = last_element[-1]['id'] + 1
      print('ℹ️  система : ', id1)
      # сохранение данных
      users[username1] = {
       'name' : name1,
       'password' : password1,
       'age' : None,
       'email' : None,
       'id': id1,
       'status': 'Active'
       }
      users['idishki'][id1] = {id1}
      print('ℹ️  система : ', users)
      break
     elif correct == "2":
      print("Заполните данные с начала")
      continue
     else:
      print("Введите «1», если всё верно, или «2», если хотите изменить.")
# авторизация свежего аккаунта
    while True:
     print("Войдите в аккаунт")
     username2 = input("Введите юзернейм: ")
     if username2 not in users:
      print("Пользователя с таким именем не существует!")
      continue
     password2 = input("Введите пароль: ")
     if username2 in users and users[username2]['password'] == password2:
        print("Вход в аккаунт совершён успешно")
        log = username1, users[username1]['id']
        break
     else:
        print("Неверный логин или пароль. повторите попытку") 
        continue

# предложение привязки почты к аккаунту
    while True:
     print("Рекомендуем привязать электронную почту")
     print("С ней у вас будет возможность в случае утери пароля восстановить доступ к аккаунту")
     print(" [«1»] - привязать почту")
     print(" [«2»] - отказаться")
     a = input('>> ')
     if a == "1":
      email = input("Введите адрес электронной почты: ")
      if "@" not in email or "." not in email:
       print("Введите корректный email!")
       continue
      if email == '@' or '.':
       # обновление данных
       print("Электронная почта успешно привязана!")
       users[username1] = {
        "email": email
        }
       print('ℹ️  система : ', users)
       break
     if a == "2":
      print("Ненененененееее.. Это была иллюзия выбора. вы привяжете почту. иначе пожалеете...")  
      continue
  
# главное меню
   while True:
    print("Главное меню")
    print("[«1»] - Настройки профиля")
    print("[«2»] - *Действие 2*")
    print("[«3»] - *Действие 3*")
    print("[«4»] - Покинуть учётную запись")
    deystvie = input(">> ")

    if deystvie == '1':
     # настройки профиля
     while True:
      print("")
      print(" - - Настройки профиля - - " )
      print(" Имя:", users[log[0]]['full name'],'.',"Почта:", users[username1]['email'])
      print("[«1»] - Изменить юзернейм")
      print("[«2»] - Изменить имя")
      print("[«3»] - Изменить пароль")
      print("[«4»] - Отвязать почту")
      print("[«5»] - Вернуться в меню")
      print("[«6»] - Удалить аккаунт")
     
      deystvie2 = input(">> ")
      
      if deystvie2 == '1':
       # смена юзернейма 
       print("[«1»] - Я передумал")
       reusername = input("Придумайте новый юзернейм: ")
       if reusername == '1':
        break
      if deystvie2 == '2':
       rename = input("Введите новый юзернейм: ")
       rename = users[username1]
       print("Юзернейм изменён.")
       time.sleep(1)
       continue
     
      if deystvie2 == '3':
      # смена пароля 
       while True:
        proverka = input("Введите старый пароль: ")
        if proverka == users[username1]['password']:
         repass = input("Введите новый пароль: ")
         repass = password1
         print("Новый пароль успешно сохранён!")
         break
        if proverka != users[username1]['password']:
         print("Неверный пароль")
         print("[«1»] - Повторить попытку")
         print("[«2»] - Восстановить пароль через почту")
         deystvie3 = input('>> ')
         if deystvie3 == '1':
          continue
         
         elif deystvie3 == '2':
          while True:
           print("На вашу почту было отправлено письмо с кодом восстановления, введите его сюда")
           email_code = "1234" # да, код задан изначально
           print("[«1»] - Мне не приходит код")
           email_code1 = input('>> ')
           if email_code1 == email_code:
            repass = input('Введите новый пароль: ')
            repass1 = input("Подтвердите пароль: ")
            if repass == repass1:
              users[username1]['email'] = repass
              print("Новый пароль успешно сохранён!")
           elif email_code1 == '1':
            print("Отправили новый код на вашу почту")
            email_code = "1234" # да, код задан изначально
            print("[«1»] - Мне все ровно не приходит код")
            email_code1 = input('>> ')
            if email_code1 == email_code:
              repass = input('Введите новый пароль: ')
              repass1 = input("Подтвердите пароль: ")
              if repass == repass1:
                users[username1]['email'] = repass
                print("Новый пароль успешно сохранён!")
            elif email_code1 == '1':
              print("[«1»] - Отправить код повторно")
              print("[«2»] - Назад")
              deystvie8 = ('>> ')
              if deystvie8 == '1':
               continue
              if deystvie8 == '2':
               break      
              else: 
               continue     

           

# смена или отвязка электронной почты
      if deystvie2 == '4':
       print("Вы действительно хотите отявзять свой адрес", '«', users[username1]['email'], '»'"?")
       print("Без неё вы не сможете в случае утери пароля восстановить доступ к аккунту.")
       print("[«1»] - есс")
       print("[«2»] - Назад")
       deystvie6 = input('>> ')
       if deystvie6 == '1':
        print("Электронная почта отвязана.")
        users[username1]['email'] = None
        print('ℹ️  система : ', users)
        print("Не желайте ли привязать другую?")
        print("[«1»] - Да")
        print("[«2»] - Нет")
        deystvie7 = input('>> ')
        if deystvie7 == '1':
         while True:
          print('Введите новый адрес электронной почты')
          email = input('>> ')
          if "@" not in email or "." not in email:
           print("Введите корректный email!")
           continue
          if email == '@' or '.':
           print("Электронная почта успешно привязана!")
           email = users[username1]['email']
           break

      elif deystvie2 == '5': break
      elif deystvie2 == '6': 
        print("Вы действительно хотите удалить свой аккаунт?")
        print('[1] - де')
        print('[2] - нет')
        de = input('>> ')
        if de == '1': 
         print("Аккаунт удалён"), time.sleep(1)
         del users['idishki'][log[1]]
         del users[log[0]]
         print(users)
        elif de == '2':
         continue 
# выход из аккаунта
      if deystvie == '4':
       print("Вы действительно хотите выйти из аккаунта?")
       print("[«1»] - Да")
       print("[«2»] - Нет")
       deystvie5 = input('>> ')
       if deystvie5 == '1':
        print("Вы вышли из аккаунта")
        print("*типа покинул акк*")
       if deystvie5 == '2':
        continue
      
       


 if deystvie0 == '2':
  print("Всё")
  break
 


print('ℹ️  система : stop')
