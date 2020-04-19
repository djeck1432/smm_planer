# SMM Planer

```SMM planer``` – this code will help you to organize and make post by the date and time in such social networks and messengers as: ```Vkontakte```, ```Facebook```, ```Telegram```. 
Create and fill in Google Sheets as in an  <a href='https://docs.google.com/spreadsheets/d/1uzAoBYWrmxAGAyENIZ7EJ0HwHD_JxtWSELG4ppYVvT0/edit?ts=5e20d988#gid=0'>example</a> and save your time.


## How to install

Python3 have to be already installed. Then use pip (or pip3, there is a contravention with Python2) to install dependencies:<br>
``` https://github.com/djeck1432/smm_planer.git ```

After you downloaded the repository open a folder ```post_in_socialnetworks``` using next command: <br>

```cd smm_planer```

Now all of the required libraries and modules have to be installed:<br>

```pip install -r requirements.txt ```<br>

Now we are ready for the script .

## What you need to know: 
  ### Enviroment variabels: 
```SPREAD_SHEET_ID``` - ```id``` your table;
 <br>
 <br>
  In social network ```Vk```:
<br>
```VK_PHONE```- registered phone number  ```Vk```;
<br>
```VK_PASSWORD ```-  password;
<br>
```VK_ALBUM_ID```- ```id``` album in your group ;
<br>
```VK_OWNER_ID```- ```id``` your page;
<br>
<br>
In social network ```Fb```:
<br>
```FACEBOOK_TOKEN```-  token from ```Fb```;
<br>
```FACEBOOK_GROUP_ID```- group ```id``` in ```Fb```;
<br>
<br>
In messanger ```Telegram```:
<br>
```TELEGRAM_TOKEN```- token ```Telegram```;
<br>
```TELEGRAM_CHAT_ID```- username of account ```Telegram```;
<br> 
### Receiving keys from ```Google Sheets Api```

1. Follow this <a href='https://developers.google.com/sheets/api/quickstart/python'>link</a>
2. Push the button ```Enable the Google Sheets API``` to download the keys to your account in ```Google```
3. Put in data in the folder of the project.

### How to connect ```Google Sheets ```

1. Open the web-site ```Google Sheets```.

2. In the address bar there will be a link of this type: ```https://docs.google.com/spreadsheets/d/1uzAoBYWrmxAGAyENIZ7EJ0HwHD_JxtWSELG4ppYVvT0/edit?ts=5e20d988#gid=0```.<br>
3.```1uzAoBYWrmxAGAyENIZ7EJ0HwHD_JxtWSELG4ppYVvT0``` - this is your ```SPREAD_SHEET_ID```

## How to run the code

In ```bash``` run the following command: 
<br>
<br>
```python3 main.py```
<br>
<br>
After running the code, a window will open in your browser for authorization to your ```Google Drive```.
<br>
After authorization, close the window.
<br>
Your program is up and running, congratulations!


