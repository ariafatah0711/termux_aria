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
  <summary><b>apache2</b></summary>

  - apt install apache2
  - nano ../usr/etc/apache2/httpd.conf
  - cd ../usr/share/apache2/default-site/htdocs/
    - nano index.html
  - apache2 -k start -f "/path/to/your/httpd.conf" -D "Listen 8080"
  - apache2 -k stop
</details>

<p id="download"></p>

## 🔨 download

1. Open a terminal or command prompt on your computer.
2. Navigate to the directory where you want to save this project.
3. Use the following command to download the project from the GitHub repository:
   ```sh
   git clone https://github.com/ariafatah0711/dicoding_3.git
   ```

<p id="related"></p>

## 📈 related
<a href="" alt="DEMO"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=DEMO&message=WEB&color=000000"></a>

<p id="license"></p>

## ©️ license
<a href="https://github.com/ariafatah0711" alt="CREATED"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=CREATED%20BY&message=ariafatah0711&color=000000"></a>
<a href="https://github.com/ariafatah0711/ariafatah0711/blob/main/LICENSE" alt="LICENSE"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=LICENSE&message=MIT&color=000000"></a>
