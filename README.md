Dipwatch is a python script that lets you generate email notifications
for your gunboat games, saving your workday productivity hours. This is
the third best thing since bread came sliced, the second obviously being
chips and guacamole.

Steps to get Dipwatch functional
---------------------------------

1. Install python dependencies: requests and BeautifulSoup. This should
   be as easy as

        - pip install requests
        - pip install beautifulsoup4

   Look at the documentation for those packages for help

2. Only notifications to your Gmail account are supported at the moment.
   Replace the header DPW_GMAIL_UID with your email address, and DPW_GMAIL_ASP
   with an Application-Specific Password for this script. You can configure
   these at https://accounts.google.com

3. Set DPW_REFRESH_MINUTES to your desired update frequency. No emails 
   will be sent unless the game changes state. Please DO NOT use a number
   lower than 10 minutes, be nice to the server.

How to Run
-----------------------------------

I recommend doing

    python dipwatch.py >dipwatch.log 2>&1 &

Occassionally examine dipwatch.log to make sure everything is okay. You
should get an email as soon as you start the script when it fetches current
state, things are probably working if you do.

Known Bugs and Issues
------------------------------------

Treat this as a hack I threw together to fix something that was annoying me. 
If you'd like to help me fix issues or add features, I will be grateful for 
an extended period of time. 


To-Do
------------------------------------

Here are some ideas for extending dipwatch. Feel free to submit pull requests!

1. Blocking alert. Inform me if my 'Not Ready' vote is holding up the game
2. Update summary. Tell me what happened in this phase. Did I gain centers or
   lose them? Do I have to make retreats?
3. New Messages. Alert me if I've received any new messages. Including a summary
   of each message would be fantastic!

De-cloaking Research
1. Attempt to identify other players in an anonymous games, if you know who's 
   playing the game. Compare game state changes (received messages, votes or
   saved move sets) with last seen times on player profiles. Is such de-cloaking
   possible on webdiplomacy? If it is, perhaps last seen times should not be
   shown on the profile except to moderators. 
