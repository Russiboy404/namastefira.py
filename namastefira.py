try:
 import requests,uuid,instaloader,os
except ModuleNotFoundError:
 os.system('pip install instaloader')
 os.system('pip install requests')
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
P = '\u001b[35m'
S = '\033[1;33m'
logo=(f"""{E}==========Fira-Coin-Scraper=========
{B}[+] TeleGram : @NamasteAbhiJi
{G}[+] Youtube    : AbhinavBhardwaj
{S}[+] TelegramNetwork  : @NamasteGangNetwork
{E}====================================""")
print(logo)
def Fira(id,user,firauser):
 url = "https://dashboard.heroku.com/apps/namastefirapy/deploy/heroku-git "
 data = {'inscoo':'Cookie: mid=YgAyMAABAAHu2kbxOf9R0zMuwzYZ; ig_did=EEE996AA-EE36-4B42-A169-BB6A52475851; ig_nrcb=1; csrftoken=52DjRg73fRnpT9q83QapXoptVIYskqaS; ds_user_id=50696117930; sessionid=50666617930%3AYyFIPIO3axBfc3%3A9; shbid="10025\05450696117930\0541675716033:01f78e7ae2425f66393adf2fdcf5f80bb0b30562ad49be07603b84932c59afaf18ec2b45"; shbts="1644180033\05450696117930\0541675716033:01f70c59782e88915e2334975f16ea1bc95ccac787914aa9246fc370815729b092c5ffa0"; rur="PRN\05450696117930\0541675716033:01f7536b4cf1ca3b6c9e5b5c56a347dab161e4226f10aa97322ec08d535e3c3b073707f6"""""',
 'pkx':id,
 'uname':firauser,
 'submit':'submit'}
 namaste=requests.post(url,data=data)
 info=str(namaste.text)
 like=str(info.split('Like Coin- :')[1])
 likecoin=like.split('<br>')[0]
 follow=str(info.split('Follow Coin- :')[1])
 followcoin=follow.split('\n')[0]
 inf=(f"""
{E}ID ==> {id} {E}User ==> {user}
{B}Follow Coin ==>{followcoin} {B}Like Coin ==>{likecoin}""")
 if 'Status- : ok' in info:
  print(f"""{G}Send To ==> {firauser}
{inf}
{G}Success""")
 if 'Status- : nok' in info:
  print(f"""{inf}
{P}Not Success""")
 if 'Blocked' in info:
  print(f"""{E}Blocked User""")
 else:
  print(inf)
def UserID(user,firauser):
 L = instaloader.Instaloader()
 profile = str(instaloader.Profile.from_username(L.context,user))
 idd=str(profile.split(')>')[0])
 id=idd.split(' (')[1]
 Fira(id,user,firauser)
def Start():
 os.system('clear')
 print(logo)
 firauser=input(B+"Enter Your Fira UserName : ")
 USER = input(G+"Enter Insta UserName For Login : ")
 PASSWORD =input(S+"Enter Insta PassWord For Login : ")
 L = instaloader.Instaloader()
 L.login(USER, PASSWORD)
 link1 = input(E+"Enter Post Half Link : ")
 Post = instaloader.Post.from_shortcode(L.context, link1)
 for like in Post.get_likes():
   user=like.username
   UserID(user,firauser)
os.system('clear')
print(logo)
Start()
