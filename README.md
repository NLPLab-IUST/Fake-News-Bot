# Fake-News-Bot


# table of contents


1.   About our bot
2.   Create a bot on Telegram
3.   Getting started



## About our bot

The purpose of this bot is to check the truthness of the combination of a text and an image from social media, thus it takes a text and an image as inputs, then it passes this inputs to our fact checking model. The output of this bot is a percentage that indicates the possibility that this corresponding news is fake.

#### **Note: We didn't fully implement this bot yet. It's taking inputs, then searches them in google and shows the result to the user.**


## Create a bot on Telegram

We need to ask telegram to create a new bot on the platform, it's a fairly simple process, you can do so in your telegram app(on windows/linux/android/ios/web) you need to go to **botfather** which is basically a bot himself that automate the process of creating your bot.

You will need to ask him using the / prefix to start a command, once you start typing it will autocomplete itself, the command you need is /newbot, which will take you to the flow of creating your bot, the bot will prompt you for a name and username for the bot (the username has to be unique), then it will respone with a message like so:



```
Done! Congratulations on your new bot. You will find it at t.me/{bot-username}. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

Use this token to access the HTTP API:
{Your_Token}
Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api
```





## Getting started

First of all we need to create a virtualenv for this project. if you don't have anaconda take a look at this [website](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/), otherwise go [here](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/)


After cloning this repository on your computer, you need to install all of required packages which are listed in requirements.txt. you can install them with following code:


```
pip install -r requirements.txt
```

In the next step you should open bot.py file and copy your bot's token which is given by **botfather** to the Token in line 10.

Now you are ready to run the bot.py file. **Remember that if you IP address is from iran, you need to turn on your VPN.**

#### **Note: you can run this code on colab by copying the code inside bot.py.**





