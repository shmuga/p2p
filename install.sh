#! /bin/sh
apt-get -y install python-daemon

DST_DIR_PATH=/opt/p2p

echo "Копирование файлов..."
if ! [ -d $DST_DIR_PATH ] 
then
mkdir -p $DST_DIR_PATH
fi
cp -r ./ $DST_DIR_PATH
echo "OK"

# chmod +x /opt/e2p/e2p.py
chmod +x /opt/p2p/start.sh

rm /var/mail/info

sh /opt/p2p/start.sh