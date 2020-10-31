sudo apt update
echo $PATH
yes | sudo apt install apt-transport-https ca-certificates curl software-properties-common
echo $PATH
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
yes | sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
sudo apt update
apt-cache policy docker-ce
yes | sudo apt install docker-ce
yes | sudo systemctl status docker