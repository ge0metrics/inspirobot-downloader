import requests,urllib.request,os,datetime

def generate(count):
    now=datetime.datetime.now().strftime("%d%m%y-%H%M%S")
    path="./{}".format(now)
    os.mkdir(path)
    
    for x in range(0,count):
        r=requests.get("http://inspirobot.me/api?generate=true")
        i=r.text
        
        filename="{}/{}.jpg".format(path,x)

        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(i,filename)

        print(filename)

opener=urllib.request.build_opener()
opener.addheaders=[("User-agent","Mozilla/5.0")]

while True:
    print("How many to download? (0 to exit)")
    c=input()
    try:
        c=int(c)
        if c==0:
            break
        else:
            generate(int(c))
    except ValueError:
        print("You must enter a number!")
