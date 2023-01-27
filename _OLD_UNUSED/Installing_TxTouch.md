# Installing TxTouch

LATEST INSTALL METHOD on Bullseye 64-bit Lite

TODO: add instructions to burn Bullseye to micro sd card.

## BEGIN

\$ cd

\$ sudo apt update

\$ sudo apt full-upgrade -y

\$ sudo apt autoremove

\$ sudo rpi-eeprom-update -a

	and proceed as neccessary

\$ sudo reboot

## INSTALL GIT

\$ sudo apt install git -y

SEE: https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup

\$ git config --global user.name "ea7kir"
\$ git config --global user.email "mikenaylorspain@icloud.com"
\$ git config --global init.defaultBranch main

## INSTALL PYENV

\$ sudo apt-get update

\$ sudo apt-get install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

\$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv

\$ echo 'export PYENV_ROOT="\$HOME/.pyenv"' >> ~/.bashrc

\$ echo 'export PATH="\$PYENV_ROOT/bin:\$PATH"' >> ~/.bashrc

\$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "\$(pyenv init --path)"\nfi' >> ~/.bashrc

\$ exec \$SHELL

## INSTALL PYTHON

\$ sudo apt install wget build-essential libreadline-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev -y

\$ pyenv global system

\$ pyenv versions

	* system (set by /home/pi/.pyenv/version)

\$ pyenv install 3.11.1

\$ pyenv versions

	* system (set by /home/pi/.pyenv/version)
	3.11.1

\$ pyenv global 3.11.1

	* system 3.11.1 (set by /home/pi/.pyenv/version)
	3.9.2

## UPGRADE PIP

\$ pip install --upgrade pip

## INSTALL PYSIMPLEGUI, WEBSOCKETS & PyYAML

\$ pip install pysimplegui websockets PyYAML

## INSTALL PIGPIO (for PTT and MUTE)

PERHAPS THIS SHOULD BE INSTALLED BEFORE PYTHON 3.11.1

\$ sudo apt install pigpio python-pigpio python3-pigpio

\$ sudo systemctl enable pigpiod

\$ sudo systemctl start pigpiod

## INSTALL A GUI

\$ sudo apt install raspberrypi-ui-mods

## RUN PASPI-CONFIG

\$ sudo raspi-config

	and SELECT 1 Sytem -> S5 Boot -> Auto Login -> B4 Desktop Auto Login

\$ sudo reboot

## Clone my repo in VSCODE
