import requests
import smtplib
from sys import stdout
from time import sleep
from bs4 import BeautifulSoup as bs

DPW_GAME_ID = 157247 # GAME ID YOU'RE INTERESTED IN GOES HERE
DPW_REFRESH_MINUTES = 30

DPW_GMAIL_UID = '' # YOUR FULL GMAIL ADDRESS GOES HERE e.g. dipwatch@gmail.com  
DPW_GMAIL_ASP = '' # YOUR APPLICATION SPECIFIC PASSWORD GOES HERE

game_state = {'season':'Winter', 'year':'1900', 'phase':'Pre-Game'}
headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'en-US,en;q=0.8,es;q=0.6,ms;q=0.4',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Host':'webdiplomacy.net',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'
}
orders_url = 'http://webdiplomacy.net/board.php?gameID=%d&viewArchive=Orders' % DPW_GAME_ID

def getState(gameDateTag, gamePhaseTag):
        for gameDate in gameDateTag.children:
                pass
        for gamePhase in gamePhaseTag.children:
                pass

        season, year = str(gameDate).split(', ')
        return {'season':season, 'year':year, 'phase':str(gamePhase)}

def notifyMe():
        if DPW_GMAIL_UID and DPW_GMAIL_ASP:
                msg = 'From: %s\r\nTo: %s\r\n' % ('updates@webdip', DPW_GMAIL_UID)
                msg += 'Subject: Game %s progressed to %s, %s %s\r\n\r\n' % (DPW_GAME_ID, game_state['phase'], game_state['season'], game_state['year'])
                msg += 'Make my move: webdiplomacy.net/board.php?gameID=%s' % DPW_GAME_ID

                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.login(DPW_GMAIL_UID, DPW_GMAIL_ASP)
                server.sendmail('updates@webdip', DPW_GMAIL_UID, msg)
                server.quit()

def refreshState():
        global game_state
        r = requests.get(orders_url, headers=headers)

        # with open('page', 'w') as w:
        #        w.write(r.content)

        soup = bs(r.content)
        now_state = (getState(gameDate, gamePhase) for gameDate in soup.find_all('span', 'gameDate') for gamePhase in soup.find_all('span', 'gamePhase')).next()

        if game_state == now_state:
                print 'State unchanged'
        else:
                game_state = now_state
                print 'Game updated. %s %s, %s' % (game_state['phase'], game_state['season'], game_state['year'])
                notifyMe()

if __name__=='__main__':
        while True:
                try:
                        refreshState()
                except Exception as e:
                        print 'Script went derp, will try again later:', e

                stdout.flush()
                sleep(60 * DPW_REFRESH_MINUTES)

