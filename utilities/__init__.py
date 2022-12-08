import os,sys,time

def echo(text):
    print(text)

def write(e):
    for i in e+"\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(00.1)
