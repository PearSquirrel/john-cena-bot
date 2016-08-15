import time
import praw
import getpass

r = praw.Reddit('John Cena Comment Monitor by u/PearSquirrel v 1.0.')
username = raw_input("Username: ")
password = getpass.getpass()
r.login(username, password)

cache = []
triggers = ['john cena']
while True:
    print "You know his name..."
    subreddit = r.get_subreddit('JohnCena')
    for submission in subreddit.get_hot(limit=3):
        title = submission.title.lower()
        has_cena = any(string in title for string in triggers)
        if submission.id not in cache and has_cena:
            print "JOHN CENA!!!"
            msg = '[JOHN CENA](%s)' % submission.short_link
            r.send_message(username, 'John Cena Link', msg)
            cache.append(submission.id)
    time.sleep(1800)
