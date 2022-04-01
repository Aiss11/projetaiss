 
 #!/bin/bash

echo "installation de mysql-server"
sudo  apt-get install  mysql-server


echo "installation de iredmail"

echo "telecharger la derniere version de iredmail"
 wget https://github.com/iredmail/iRedMail/archive/refs/tags/1.5.2.tar.gz

echo " extraction du fichier archive"
sudo tar xvf 1.5.2.tar.gz

echo "entrer dans le repertoire iremail-1.2.3"
 
echo "droit dexecution"
sudo chmod +x /home/faby/iRedMail-1.5.2/iRedMail.sh
sudo bash  /home/faby/iRedMail-1.5.2/iRedMail.sh



