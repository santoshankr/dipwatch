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

2. Replace the header DPW_WEBDIP_COOKIE with your WebDiplomacy cookie. 
   Remember to check the 'Keep me signed in' option before you extract
   the cookie so you don't have to keep changing it. This is a stopgap
   solution, if you'd like to implement the full login, I'm happy to
   accept pull requests

3. Only notifications to your Gmail account are supported at the moment.
   Replace the header DPW_GMAIL_UID with your email address, and DPW_GMAIL_ASP
   with an Application-Specific Password for this script. You can configure
   these at accounts.google.com

4. Set DPW_REFRESH_MINUTES to your desired update frequency. No emails 
   will be sent unless the game changes state. Please DO NOT use a number
   lower than 10 minutes, be nice to the server.

How to Run
-----------------------------------

I recommend doing

python dipwatch.py 2>&1 >dipwatch.log &

Occassionally examine dipwatch.log to make sure everything is okay. You
should get an email as soon as you start the script when it fetches current
state, things are probably working if you do.

Known Bugs and Issues
------------------------------------

I am absolutely positive that almost everything is broken. Treat this
as a hack I threw together to fix something that was annoying me. If 
you'd like to help me fix this, I will be grateful for an extended period
of time. 
