#!/bin/sh

# 1. Install Docker
sudo yum update -y
sudo yum -y install docker
sudo service docker start
sudo usermod -a -G docker ec2-user
sudo chmod 666 /var/run/docker.sock
docker version

# 2. Install docker-compose
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose version

# 3. Install git
sudo yum install git -y

# 4. Clone repository
git clone https://github.com/tomas-lucena/app-example.git

cd app-example

# 6. Run application
docker-compose up --no-deps --force-recreate  --build    