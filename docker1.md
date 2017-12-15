# Docker 学习
-----
## 安装docker
```
apt-get install docker.io
service docker start
docker pull alpine
docker run -it alpine
```

## 用debootstap构建docker镜像
```
mkdir -p /mnt/ubuntu
debootstrap --arch amd64 trusty /mnt/ubuntu
```
以上两行命令就在/mnt/ubuntu目录里创建了一个ubuntu系统，通过,之后通过如下命令得到docker镜像
```
cd /mnt/ubuntu
tar --numeric-owner -cpf ubuntu.tar -C ubuntu .
cat ubuntu.tar|docker import - ubuntu-base
```
运行docker
```
docker run -i -t ubuntu-base /bin/bash
```

## 保存docker修改
```
docker run -i - t alpine
docker ps -a
```
通过docker ps -a 获得的TAG来commit
```
docker commit TAG baseos
```
