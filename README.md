# SMM Planer

`SMM planer` – this code will help you to organize and make post by the date and time in such social networks and messengers as: `Vkontakte`, `Facebook`, `Telegram`. 
Create and fill in Google Sheets as in an  <a href='https://docs.google.com/spreadsheets/d/1uzAoBYWrmxAGAyENIZ7EJ0HwHD_JxtWSELG4ppYVvT0/edit?ts=5e20d988#gid=0'>example</a> and save your time.


## How to install

Python3 have to be already installed. Then use pip (or pip3, there is a contravention with Python2) to install dependencies:
```
https://github.com/djeck1432/smm_planer.git
```
After you downloaded the repository open a folder `post_in_socialnetworks` using next command:
```
cd smm_planer
```
Now all of the required libraries and modules have to be installed:
```
pip install -r requirements.txt 
```

Now we are ready for the script .

## What you need to know: 
  ### Environment variables: 
`SPREAD_SHEET_ID` - `id` your table;
 <br>
 <br>
  In social network `Vk`:
<br>
`VK_PHONE`- registered phone number  `Vk`;
<br>
`VK_PASSWORD `-  password;
<br>
`VK_ALBUM_ID`- `id` album in your group ;
<br>
`VK_OWNER_ID`- `id` your page;
<br>
<br>
In social network `Fb`:
<br>
`FACEBOOK_TOKEN`-  token from `Fb`;
<br>
`FACEBOOK_GROUP_ID`- group `id` in `Fb`;
<br>
<br>
In messenger `Telegram`:
<br>
`TELEGRAM_TOKEN`- token `Telegram`;
<br>
`TELEGRAM_CHAT_ID`- username of account `Telegram`;
<br> 
### Receiving keys from `Google Sheets API`
<ol>
  <li>Follow this <a href='https://developers.google.com/sheets/api/quickstart/python'>link</a>.</li>
  <li>Push the button `Enable the Google Sheets API` to download the keys to your account in `Google`.</li>
  <li>Put in data in the folder of the project.</li> 
</ol>


### How to connect `Google Sheets `
<ol>
  <li>Open the website, `Google Sheets`.</li>
  <li>In the address bar, there will be a link of this type: `https://docs.google.com/spreadsheets/d/1uzAoBYWrmxAGAyENIZ7EJ0HwHD_JxtWSELG4ppYVvT0/edit?ts=5e20d988#gid=0`.</li>
  <li>`1uzAoBYWrmxAGAyENIZ7EJ0HwHD_JxtWSELG4ppYVvT0` - this is your `SPREAD_SHEET_ID`</li>
</ol>

## How to run the code

In `bash` run the following command: 
```
python3 main.py
```
After running the code, a window will open in your browser for authorization to your `Google Drive`.

After authorization, close the window.

Your program is up and running, congratulations!


