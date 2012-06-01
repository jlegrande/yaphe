import os, time

filename = "page_test"
mtime = os.stat(filename).st_mtime

while True:
    cur_mtime = os.stat(filename).st_mtime
    if cur_mtime > mtime:
        os.system("rm -f ~/WebDev/pws2-flask/templates/home.html;./page_test >> ~/WebDev/pws2-flask/templates/home.html")
        mtime = cur_mtime
    time.sleep(1)
