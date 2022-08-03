# Python CSV Email Sender

Send multiple emails from a CSV file with a python script 📨

## Prerequisite :
1) Turn on [Less Secure App access](https://myaccount.google.com/lesssecureapps) of your Google Account :

![image](https://user-images.githubusercontent.com/43397636/116787412-0e031500-aace-11eb-8770-76e0f3bc970c.png)

2) Create a CSV file name `email.csv` which contains receiver email address at first column, name of recepient at second column, and subscription plan at the third column (subscription plan is just an example, change it to what ever you want) :

![image](https://user-images.githubusercontent.com/43397636/116787485-7520c980-aace-11eb-8d68-4e1ed9f3eeee.png)

In the picture above, you can see that :
- `johndoe@gmail.com` is receiver email address
- `John Doe` is name of recepient
- `Premium` is subscription plan

**Note: please put `email.csv` in the same directory as this project**

3) Create environment varibles (`.env`) in the root directory of this project by modifying `.env.example` :
Here is an example :

![image](https://user-images.githubusercontent.com/43397636/116787598-1c9dfc00-aacf-11eb-8369-db55b3a0beed.png)

In the example above :
- `kaidoe@gmail.com` is the sender email address
- `kaidoe123` is the password of the sender email address which is `kaidoe@gmail.com`
- `Subscription Plan` is the subject of the email

## How to Run :
These steps below assume you have completed [prerequisites](#prerequisite-) steps above, thank you.

1) Open your terminal or command prompt(CMD) then clone this repository :<br/>
`git clone https://github.com/kevinadhiguna/python-csv-email-sender`

2) Change directory to this application :<br/>
`cd python-csv-email-sender`

3) Install dependency :<br/>
`pip install -r requirements.txt` or `pip3 install -r requirements.txt`

4) Run the application :<br/>
`python send.py` or `python3 send.py`

## Demo

<img src="https://s3.gifyu.com/images/send-mail_iphone12black_portrait.png" alt="sendmail.py - result" border="0" height="550px" />

## Reference

- [How To Send Multiple Emails from CSV Using Python by I know python](https://youtu.be/J027R2cgXhc)

[![Visits Badge](https://badges.pufler.dev/visits/kevinadhiguna/antdpro-strapi-auth)](https://github.com/kevinadhiguna)
