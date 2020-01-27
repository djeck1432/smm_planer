# SMM Planer

```SMM Planer``` - этот код, поможет организовать и выкладывать посты по дате и времени в таких социальных сетях и мессенджере, как : ```Vkontakte```,```Facebook```,
```Telegram```. Создайте и заполните  ```Google Sheets```, как в <a href='https://docs.google.com/spreadsheets/d/1uzAoBYWrmxAGAyENIZ7EJ0HwHD_JxtWSELG4ppYVvT0/edit?ts=5e20d988#gid=0'>примере</a> и cэкономте время.


## Как установить 

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:<br>

``` https://github.com/djeck1432/smm_planer.git ```

После того, как скачали репозиторий, откройте в терминале(MacOs) или в консоли(Linux) папку ```smm_planer``` следующей командой:<br>

```cd smm_planer```

Для того, что бы запустить код, нужно установить необходимые библиотеки:<br>

```pip install -r requirements.txt ```<br>

Готово, мы установили проект и все необходимые библиотеки у нас на компьютере.


## Что нужно знать: 
  ### Переменные окружения: 
```SPREAD_SHEET_ID``` - ```id``` вашей таблицы
 <br>
 <br>
  В социальной сети ```Vk```:
<br>
```VK_PHONE```- номер телефона, на который зарегестрирован  ```Vk```;
<br>
```VK_PASSWORD ```- пароль от учетной записи;
<br>
```VK_ALBUM_ID```- ```id``` альбома в вашей группе;
<br>
```VK_OWNER_ID```- ```id``` вашей страницы;
<br>
<br>
В социальной сети ```Fb```:
<br>
```FACEBOOK_TOKEN```-  токен доступа от ```Fb```;
<br>
```FACEBOOK_GROUP_ID```- ```id``` группы в ```Fb```;
<br>
<br>
В месенджере ```Telegram```:
<br>
```TELEGRAM_TOKEN```- токен доступа от ```Telegram```;
<br>
```TELEGRAM_CHAT_ID```- имя вашего чата/канала в ```Telegram```;
<br> 
### Получения ключей от ```Google Sheets Api```

1. Перейдите по <a href='https://developers.google.com/sheets/api/quickstart/python'>ссылке</a>
2. Нажмите на кнопку ```Enable the Google Sheets API``` для загрузки ключей от вашего аккаунта в ```Google```
3. Вставте данный файл в папку проекта.

### Как подключить ```Google Sheets ```

1.Откройте свой ```Google Sheets```.
<br>
2.В адресной строке будет ссылка такого типа : ```https://docs.google.com/spreadsheets/d/1uzAoBYWrmxAGAyENIZ7EJ0HwHD_JxtWSELG4ppYVvT0/edit?ts=5e20d988#gid=0```.<br>
3.```1uzAoBYWrmxAGAyENIZ7EJ0HwHD_JxtWSELG4ppYVvT0``` - это есть ваш ```SPREAD_SHEET_ID```

## Как запустить код

В ```bash``` выполните следующую команду: 
<br>
<br>
```python3 main.py```
<br>
<br>
После запуска кода, у вас откроется в браузере окно для авторизации к вашему ```Google Drive```.
<br>
После прохождения авторизации, закройте окно.
<br>
Ваша програма запущенна и работает, поздравляю!


