# termux_aria

My file bash, and configurate for termux

<p align="center">
  <a href="#introduction">introduction</a> •
  <a href="#table-of-contents">table of contents</a> •
  <a href="#download">Download</a> •
  <a href="#related">Related</a> •
  <a href="#license">License</a>
</p>

<p id="introduction"></p>

## 🚀 introduction
this is my termux conf, and my file for run termux

<p align="left"> <a href="#">
  <img alt='Bash' src='https://img.shields.io/badge/-Bash-4EAA25?style=flat-square&logo=gnu-bash&logoColor=white'>
  <img alt="linux" src="https://img.shields.io/badge/-Linux-FCC624?style=flat-square&logo=linux&logoColor=black" />
  </a>
</p>

<p id="table-of-contents"></p>

## 📋 Table of Contents
<details>
  <summary><b>set up termux</b></summary>

  - setup
    ```
    termux-setup-storage # akses storage
    termux-change-repo # change repository
    ```
  - update repo
    ```
    pkg update pkg upgrade upgrade # or pkg-get <option>
    ```
  - install package
    ```
    pkg install git wget zip unzip nano
    pkg install python python2 python3 ruby
      - gem install lolcat
    pkg install cmatrix neofetch toilet # showfigfonts ex: toilet -f big -F gat ariafatah
    ```
  - install package opsional for developer
    ```
    pkg install nodejs clang php # opsional
    ```
</details>

<details>
  <summary><b>change font</b></summary>

  - open browser go to url nerdfonts.com
    - Donwodl > and search JetBrains > copy url link
  - mkdir fonts; cd fonts
    - wget url_link
    - unzip nama_file.zip
  - cp JetBrainsMonoNerdFont-Bold.ttf ~/.termux/font.ttf
</details>

<details>
  <summary><b>ssh</b></summary>

  - server
    - Pkg install openssh
    - passwd
      - sshd #nyalain ssh
      - pidof sshd #cek ssh udh nyala
    - Ifconfig #wlan 0
       - Nmap 10.10.10.1 #port 8022/tcp

  - client
    - ```ssh username@ip_address -p 8022```
</details>

### package

<details>
  <summary><b>apache2</b></summary>

  - apt install apache2
  - nano ../usr/etc/apache2/httpd.conf
  - cd ../usr/share/apache2/default-site/htdocs/
    - nano index.html
  - apache2 -k start -f "/path/to/your/httpd.conf" -D "Listen 8080"
  - apache2 -k stop
</details>

<details>
  <summary><b>nginx</b></summary>

  - apt install nginx
  - nano ../usr/etc/nginx/nginx.conf
  - cd ../usr/share/nginx/html/
    - nano index.html
  - nginx -h
  - nginx -s start -f "/path/to/your/httpd.conf" -D "Listen 8080"
  - nginx -s stop
</details>

<details>
  <summary><b>weeman</b></summary>

  - pip2 install beautifulsoup bs4
  - git clone https://github.com/evait-security/weeman
  - python2 weeman/weeman.py
    - set url https://facebook.com
    - set action_url https://facebook.com
    - set port 8080
    - run
</details>

<details>
  <summary><b>ngrok</b></summary>

  - Login acc  https://ngrok.com/
    - Donwoald Linux arms64
  - cd storage/downloads
    - cp -f nama_file.tgz $HOME
    - tar -xvzf namafile.tgz
    - chmod +x ngrok
  - copy  ur acc Authtoken
    - ./ngrok config add-authtoken your_token
    - ./ngrok config upgrade
  - use VPN to safety and Turn on hotspot
    - ./ngrok http 8080
    - ./ngrok http http://localhost:8080
</details>

<details>
  <summary><b>neovim</b></summary>

  - pkg install neovim git wget nodejs python lua-language-server -y
  - open browser go to url https://nvchad.com/
    - click install
    - copy git clone
  - git clone https://github.com/NvChad/NvChad ~/.config/nvim --depth 1 && nvim
  - example custom config? N
    - Waiting and :q enter
  - Code suggestions and auto complete
    - pkg install clang -y
    - cd .config/nvim
    - nvim
      - Ctrl n
      - https://nvchad.com/docs/config/lsp ::configuration
</details>

### linux gui

<details>
  <summary><b>termux x11</b></summary>

  - install termux x11 in https://github.com/termux/termux-x11
  - open termux
    - pkg install x11-repo
    - pkg install termux-x11-nightly
    - pkg install proot-distro
  - proot-distro -h
    - proot-distro list
    - proot-distro install debian
  - login distro
    - proot-distro login debian
    - apt update -y
    - apt install nano adduser
    - apt install sudo
    - adduser ariafatah
    - nano /etc/sudoers
      ```
      # User privilege specification
      root    ALL=(ALL:ALL) ALL
      ariafatah       ALL=(ALL:ALL) ALL
      ```
    - su ariafatah
    - sudo apt install xfce4 -y
    - exit, exit
  - termux
    - wget https://raw.githubusercontent.com/LinuxDroidMaster/Termux-Desktops/main/startxfce4_debian.sh
    - chmod +x startxfce4_debian.sh
    - nano startxfce4_debian.sh
    - change user
    - ./startxfce4_debian.sh
  - how use
    - Dalam mode emulasi touchpad Anda dapat menggunakan gerakan berikut:
      - Ketuk klik
      - Ketuk dua kali untuk klik dua kali
      - Ketuk dua jari untuk klik kanan
      - Ketuk tiga jari untuk klik tengah
      - Gesek vertikal dua jari untuk gulir vertikal
      - Gesek horizontal dua jari untuk gulir horizontal
      - Gesek tiga jari ke bawah untuk memperlihatkan-menyembunyikan bilah tombol tambahan.
    - Mode layar sentuh simulasi.
    - Dalam mode layar sentuh simulasi, Anda dapat menggunakan gerakan berikut:
      - Ketuk sekali untuk klik tombol kiri.
      - Ketuk lama untuk memegang mouse.
      - Ketuk dua kali untuk klik dua kali
      - Ketuk dua jari untuk klik kanan
      - Ketuk tiga jari untuk klik tengah
      - Gesek vertikal dua jari untuk gulir vertikal
      - Gesek horizontal dua jari untuk gulir horizontal
      - Gesek tiga jari ke bawah untuk memperlihatkan-menyembunyikan bilah tombol tambahan.
</details>

<details>
  <summary><b>xfce4</b></summary>

  - apt install xfce4-terminal
  - chrome
    - apt install chromium -y
    - chromium --no-sandbox
    - setting panel, remove browser default, setting laucher, add chromium, and change command add --no-sandbox
  - visual studio
    - install visual studio in browser .deb
      - sudo dpkg -i package.deb
      - setting panel, add laucher, setting laucher, add vscode
      - add add paramter --no-sandbox
</details>

<details>
  <summary><b>vnc server</b></summary>

  - proot distro
    - apt install tigervnc-standalone-server
    - apt install dbus-x11
    - which startxfce4
    - vncserver -xstartup /usr/bin/startxfce4
    - vncserver -xstartup /usr/bin/startxfce4 -localhost no
    - vncserver -kill :1
  - if have many local port
    - rm -f /tmp/.X11-unix/X1 /tmp/.X1-lock /tmp/.X11-unix/X2 /tmp/.X2-lock
</details>

<p id="download"></p>

## 🔨 download

1. Open a terminal or command prompt on your computer.
2. Navigate to the directory where you want to save this project.
3. Use the following command to download the project from the GitHub repository:
   ```sh
   git clone https://github.com/ariafatah0711/termux_aria.git
   ```

<p id="related"></p>

## 📈 related

<p id="license"></p>

## ©️ license
<a href="https://github.com/ariafatah0711" alt="CREATED"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=CREATED%20BY&message=ariafatah0711&color=000000"></a>
<a href="https://github.com/ariafatah0711/ariafatah0711/blob/main/LICENSE" alt="LICENSE"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=LICENSE&message=MIT&color=000000"></a>
