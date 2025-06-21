import requests
import os
import time

print("[?] Installing libs for program...")
os.system("sudo apt install xz-utils curl")

i = input("need to install zapret? (0 or 1): ")
if i == "1":
    print("[?] Installing zapret...")
    time.sleep(0.5)
    os.system("git clone https://github.com/Sergeydigl3/zapret-discord-youtube-linux.git")
    print("[+] Zapret installed!")
    print("running zapret...")
    time.sleep(1.5)
    os.system("ip a;sudo bash ~/zapret-discord-youtube-linux/main_script.sh")
else:
    print("[?] Downloading discord ...")
    time.sleep(0.5)
    os.system("touch discord-aaa.deb")
    with open("discord-aaa.deb","wb") as f:
         r = requests.get("https://stable.dl2.discordapp.net/apps/linux/0.0.98/discord-0.0.98.deb")
         f.write(r.content)
    print("[+] Discord downloaded!")
    time.sleep(0.5)
    print("[?] Discord installing...")
    time.sleep(0.5)
    os.system("sudo dpkg -i discord-aaa.deb")
    print("[+] Discord installed")
    print("[?] Installing and Downloading Telegram Desktop")
    time.sleep(0.5)
    os.system("touch tg.tar.xz")
    with open("tg.tar.xz","wb") as f:
        r = requests.get("https://td.telegram.org/tlinux/tsetup.5.15.4.tar.xz")
        f.write(r.content)
    os.system("tar xf tg.tar.xz")
    print("[+] Close telegram for installing!")
    time.sleep(2)
    os.system("~/Telegram/Telegram")
    iaa = input("YouTube Music or Yandex Music or Spotify? (yo,ya,sp): ")
    if iaa == "yo":
        print("[?] Installing YouTube Music Desktop ...")
        with open("yo.deb","wb") as f:
            r = requests.get("https://github.com/th-ch/youtube-music/releases/download/v3.9.0/youtube-music_3.9.0_amd64.deb")
            f.write(r.content)
        os.system("sudo dpkg -i yo.deb;rm yo.deb")
    if iaa == "ya":
        print("[+] Yandex Music Installing ...")
        with open("ya.deb","wb") as f:
            r = requests.get("https://github.com/cucumber-sp/yandex-music-linux/releases/download/v5.56.0/yandex-music_5.56.0_amd64.deb")
            f.write(r.content)
        os.system("sudo dpkg -i ya.deb;rm ya.deb")
    if iaa == "sp":
        print("[?] Installing Spotify ...")
        os.system('''curl -sS https://download.spotify.com/debian/pubkey_C85668DF69375001.gpg | sudo gpg --dearmor --yes -o /etc/apt/trusted.gpg.d/spotify.gpg
echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list''')
        os.system('''sudo apt-get -y update && sudo apt-get -y install spotify-client''')
    print("[?] Installing GIMP ...")
    os.system("sudo apt -y install gimp")
    print("[+] Deleting all temp files ...")
    os.system("rm tg.tar.xz discord-aaa.deb")
    print("[+] Goodbye User!")

