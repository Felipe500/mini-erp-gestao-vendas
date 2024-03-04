#--- CONFIGURANDO SERVIDOR LINUX ---#

# UPDATE E UPGRADE
sudo apt-get update && sudo apt-get upgrade

#INSTALAÇÃO PYTHON 3.10
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.10

#INSTALAÇÃO PYTHON 3.10 E DEPENDENCIAS
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
sudo apt-get install libpq-dev

sudo apt install python3.10-dev python3.10-venv -y
sudo apt install python3.10-venv
sudo apt install python3.10-distutils
sudo apt install python3.10-lib2to3
sudo apt install python3.10-gdbm
sudo apt install python3.10-tk

# INSTALAÇAÕ GIT
sudo apt install git

# PARA SERVIDOR APACHE CASO ESTEJA RODANDO
systemctl stop apache2

# INSTALAÇÃO E CONFIGURAÇÃO NGINX
sudo apt install ufw
sudo ufw app list
sudo ufw allow 'Nginx FULL'

service nginx status
service nginx start



