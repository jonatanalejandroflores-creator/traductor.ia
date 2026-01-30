sudo apt install ./libayatana-appindicator1_0.5.92-1_amd64.deb ./libayatana-indicator7_0.9.3-1_amd64.deb ./libdbusmenu-gtk4_18.10.20180917~bzr492+repack1-3_amd64.deb ./libgconf-2-4_3.2.6-8_amd64.deb ./gconf2-common_3.2.6-8_all.deb
# Cleanup
rm ./libgconf-2-4_3.2.6-8_amd64.deb ./gconf2-common_3.2.6-8_all.deb ./libayatana-appindicator1_0.5.92-1_amd64.deb ./libayatana-indicator7_0.9.3-1_amd64.deb ./libdbusmenu-gtk4_18.10.20180917~bzr492+repack1-3_amd64.deb
# Download missing libraries
wget http://ftp.debian.org/debian/pool/main/g/gconf/gconf2-common_3.2.6-8_all.deb
wget http://ftp.debian.org/debian/pool/main/g/gconf/libgconf-2-4_3.2.6-8_amd64.deb
wget http://ftp.debian.org/debian/pool/main/liba/libayatana-appindicator/libayatana-appindicator1_0.5.92-1_amd64.deb
wget http://ftp.debian.org/debian/pool/main/liba/libayatana-indicator/libayatana-indicator7_0.9.3-1_amd64.deb
wget http://ftp.debian.org/debian/pool/main/libd/libdbusmenu/libdbusmenu-gtk4_18.10.20180917~bzr492+repack1-3_amd64.deb
# Install
sudo apt install ./libayatana-appindicator1_0.5.92-1_amd64.deb ./libayatana-indicator7_0.9.3-1_amd64.deb ./libdbusmenu-gtk4_18.10.20180917~bzr492+repack1-3_amd64.deb ./libgconf-2-4_3.2.6-8_amd64.deb ./gconf2-common_3.2.6-8_all.deb
# Cleanup
rm ./libgconf-2-4_3.2.6-8_amd64.deb ./gconf2-common_3.2.6-8_all.deb ./libayatana-appindicator1_0.5.92-1_amd64.deb ./libayatana-indicator7_0.9.3-1_amd64.deb ./libdbusmenu-gtk4_18.10.20180917~bzr492+repack1-3_amd64.deb
# Update & install
sudo apt update
sudo apt install forticlient
wget -O - https://repo.fortinet.com/repo/forticlient/7.4/ubuntu22/DEB-GPG-KEY | gpg --dearmor | sudo tee /usr/share/keyrings/repo.fortinet.com.gpg
/etc/apt/sources.list.d/.
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/repo.fortinet.com.gpg] https://repo.fortinet.com/repo/forticlient/7.4/ubuntu22/ stable non-free" | sudo tee /etc/apt/sources.list.d/repo.fortinet.com.list
sudo apt-get update
sudo apt install forticlient
<support@fortinet.com>: 264E 114C 6911 D08D 3BA6 CE6C 18AC 2639 5E54 716D
sudo apt install forticlient
snap install spotify
curl -sS https://download.spotify.com/debian/pubkey_5384CE82BA52C83A.asc | sudo gpg --dearmor --yes -o /etc/apt/trusted.gpg.d/spotify.gpg
echo "deb https://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list
sudo apt update
sudo apt install spotify
curl -sS https://download.spotify.com/debian/pubkey_5384CE82BA52C83A.asc | sudo gpg --dearmor --yes -o /etc/apt/trusted.gpg.d/spotify.gpg
echo "deb https://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list
sudo apt-get update && sudo apt-get install spotify-client
sudo apt update
sudo snap install whatsapp.linux-app
sudo apt install watsapp
#include <Servo.h>
// Definición de pines
const int sensorPin = A0;
const int relayPin = 7;
// Umbral de humedad (ajustar según necesidad)
// 0 = muy húmedo, 1023 = muy seco
const int limiteHumedad = 600; 
void setup() {
  pinMode(relayPin, OUTPUT);
  digitalWrite(relayPin, HIGH); // El relé suele apagarse con HIGH (depende del modelo)
  Serial.begin(9600);
}
void loop() {
  int lectura = analogRead(sensorPin);
  
  Serial.print("Humedad detectada: ");
  Serial.println(lectura);
  if (lectura > limiteHumedad) {
    // Si la lectura es mayor al límite, la tierra está SECA
    Serial.println("Tierra seca - Regando...");
    digitalWrite(relayPin, LOW); // Activa la bomba
    delay(3000);                 // Riega por 3 segundos
    digitalWrite(relayPin, HIGH); // Apaga la bomba
    delay(1000);
  } else {
    // La tierra está HÚMEDA
    Serial.println("Tierra húmeda - No requiere riego");
    digitalWrite(relayPin, HIGH);
  }
  delay(2000); // Espera 2 segundos antes de la próxima lectura
}
sudo apt install package_name
sl
ls 
nano
nano mi_script.sh.riego
ls
chmod x
chmod
chmod nano mi_script.sh.riego
cd nano mi_script.sh.riego
cd
mi_script.sh.riego
cd mi_script.sh.riego
ls
ls
su
adduser penguin bird
nano script.sh
ls -l
echo
ls
df -h
bash
/
/etc/
/var/log/
/home/
/dev/
sudo apt install github
mount
sudo apt install mount
ls -l
-
d
cd/some/location
chmod
sticky bit
sudo apt install sticky bit
sudo adduser penguin bird
sudo virg
su
vim
ls
ls
cd script.sh--riego
ls
cd/script.sh..riego
cd script.sh...riego
ls -a
cd
ls
ls
su
root
top
htop
ls -la
cd
cd directorio
pwd
mkdir
su -l
bash
sudo apt install manpages
sudo apt install manpages-dev
sudo apt install contrib
sudo apt install non-free
sudo apt install posix
sudo apt update
sudo apt upgrade
sudo apt install posix
mashism
ls
sl
sudo apt install build-essential
sudo apt install git
sudo apt install c++
sudo apt install C++
sudo apt install x-terminal-emulador
sudo apt install gnome-terminal
sudo apt install fluxbox
ls
root
su
sudo sh -c "echo 'deb http://ppa.launchpad.net/papirus/papirus/ubuntu jammy main' > /etc/apt/sources.list.d/papirus-ppa.list"
sudo wget -qO /etc/apt/trusted.gpg.d/papirus-ppa.asc 'https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x9461999446FAF0DF770BFC9AE58A9D36647CAE7F'
sudo apt-get update
sudo apt-get install-icon-theme
sudo apt install papirus-icon-theme
nano prueba.sh
cd
ls
nano prueba.sh
chmod 777 prueba.sh
./prueba.sh
nano
nano pruba.sh
#!/bin/bash
echo // Definición de pines
const int sensorPin = A0;
const int relayPin = 7;
 // Umbral de humedad (ajustar según necesidad)
// 0 = muy húmedo, 1023 = muy seco
const int limiteHumedad = 600; 
void setup() {
  pinMode(relayPin, OUTPUT);
  digitalWrite(relayPin, HIGH); // El relé suele apagarse con HIGH (depende del modelo)
  Serial.begin(9600);
}
void loop() {
  int lectura = analogRead(sensorPin);
  
  Serial.print("Humedad detectada: ");
  Serial.println(lectura);
  if (lectura > limiteHumedad) {
    // Si la lectura es mayor al límite, la tierra está SECA
    Serial.println("Tierra seca - Regando...");
    digitalWrite(relayPin, LOW); // Activa la bomba
    delay(3000);                 // Riega por 3 segundos
    digitalWrite(relayPin, HIGH); // Apaga la bomba
    delay(1000);
  } else {
    // La tierra está HÚMEDA
    Serial.println("Tierra húmeda - No requiere riego");
    digitalWrite(relayPin, HIGH);
  }
  delay(2000); // Espera 2 segundos antes de la próxima lectura
}
ls
nano prueba.sh
dhmod 777 prueba.sh
clear
./prueba.sh
sudo apt install forticlient
[200~# Maintainer: Adrian Piotrowicz <nexces+chakraos@nxstudio.pl>
pkgname=forticlient-deb
pkgver=4.4.2331
pkgrel=1
pkgdesc="FortiClient SSL VPN from hadler.me packages"
arch=(x86_64)
url="https://hadler.me/linux/forticlient-sslvpn-deb-packages/"
license=('MIT')
depends=()
makedepends=('binutils')
provides=('forticlient')
conflicts=('forticlient')
replaces=('forticlient')
source=(https://hadler.me/files/forticlient-sslvpn_${pkgver}-${pkgrel}_amd64.deb)
sha256sums=('d76f2ad93968cbce333d813ab6c6fbe6bd3bd1966f7caa08c4983da89d579871')
prepare() { cd "$srcdir"; ar p forticlient-sslvpn_${pkgver}-${pkgrel}_amd64.deb control.tar.gz | tar xzf -; ar p forticlient-sslvpn_${pkgver}-${pkgrel}_amd64.deb data.tar.xz | tar xJf -; }
check() { cd "$srcdir"; md5sum -c md5sums || return 1; }
package() { cd "$srcdir"; mv opt "$pkgdir/"; mv usr "$pkgdir/"; 
sudo apt-cache search fortinet grep vpn
sudo apt-cache search fortinet | grep vpn
sudo apt install openfortivpn
time
18:40
timedatectl
timedatectl list-timezones
sudo timedatectl set-time
sudo timedatectl set-time "18:56:35


nano scrpt.sh
python.py
python
python.py
pithon
sudo apt install python
sudo apt install python-is-python3
python.py
python
ls
pwd
cd
progam.cpp
cd progam.cpp
cd progam.cpp
nano progam.cpp
sudp apt install libasio-dev
libasio-dev
sudo apt update
sudo apt install bouild-essential
sudo apt install build-essential
nano mi_programa.cpp
ls
ls
ls
bash ls
nano progam.cpp
chmod x nano program.cpp
chmod nano program.cpp
chmod program.cpp
chmod help
chmod --help
lis
ls
chmod 775 program.cpp
chmod u+x program.cpp
ls
cd program.cpp
cd
program.cpp
./program.cppp
./progam.cpp
cd progam.cpp
bash
ls
cd script.sh.save
cat progam.cpp
./progam.cpp
ls -l
cd mi_programa.cpp
mkdir
cat pi_programa.cpp
cat publico
pwd
ls
ls
ls -l
cd
cd
pwd
cd-
cd /
cd Doc
cd doc
cd documentos/
ls
ls
cd
l
ls
cd..
cd ..
ls
cd -
ls
pwd
sudo apt uptade
sudo apt update
sudo apt install build-essential git
sudo apt install nodejs npm
sudo apt install qt5-dev qt5-qmake
sudo apt install qtbase5-dev
sudo apt install qt5-qmake
sudo apt install rustc cargo
sudo apt install VS Code
sudo apt install visual studio code
apt
pip
sudo apt install pip
sudo apt install npm
pip install pandas
pip install numpy
sudo apt install .deb
.deb
nano mi-app.sh
nano progam.cpp
nano mi_programa.cpp
nano prueba.sh
ls
nano prueba.sh
chmod x prueba.sh
nano prueba.sh
ls
ls -l
chmod +x prueba.sh
ls
ls -l
nano prueba.sh
chmod +x progam.cpp
ls -l
nano progam.cpp
ls -l
chmod +x mi_programa.cpp
ls -l
nano mi_programa.cpp
ls
nano publico
nano videos
nano script.sh.save
mi-app.sh.save
nano mi-app.sh.save
ls
bash
sudo apt install netflix
netflix
sudo apt install max
sudo apt install HBO Max
sudo apr install HBO
sudo apt install hbo
enable
configuracion terminal
interface vlan1
interface vlan 1
ip addres 192.168.1.200 255.255.255.0
username admin privilege 15 password Ruijie12345
vlan 10
sudo apt install minicom
sudo minicom -D /dev/ttyUSB0 -d 9600
admin/admin
sudo apt install screen
sudo screen /dev/ttyUSB0 9600
enable
configure terminal
exit 
interface vlan 1
vlan 10
CONFIGURACION SWTICH RUIJIE:
sudo minicom -D /dev/ttyUSB0 -b 9600
MODO DE ACCESO:
enable 
configure terminal 
exit o end
enable
hostname
bash 
 /dev/ttyUSB0 -b 9600
/dev/ttyUSB -b 9600
/dev/ttyUSB0 -d 9600
display stack
sudo apt install pipicom
sudo apt install minicom
enable
enable confugure terminal
dmesg | grep ttyUSB
sudo apt install minicom
sudo minico -s
sudo minicom -s
sudo apt install vlan
sudo modprobe 8021q
sudo nano /etc/network/interfaces
/dev/ttyUSB0 -b 9600
sudo minicom -s
sudo minicom -s
sudo apt install screen
sudo minicom -s
sudo apt install code
sudo apt install .deb
nano hola.cpp
g++ hola.cpp -o mi_programa
./hola.cpp
chmod +x hola.cpp
./hola.cpp
ls -l
./hola.cpp
nano hola.cpp
sudo apt install code
sudo apt install.deb
nano hola.cpp
ls -l
nano hola.cpp
chomd +x hola.cpp
chmod +x hola.cpp
./hola.cpp
nano hola.cpp
./hola.cpp
nano hola.cpp
ls -l
nano prueba.sh
./prueba.sh
cd
nano prueba.sh
ls
cd
ls
cd..
cd...
cd
sudo apt install vivaldi
sudo apt install LibreWolf
sudo atp update
sudo apt update
sudo apt install extrepo -y
sudo apt update
sudo apt install librewolf -y
su apt install librewolf
sudo apt install librewolf
sudo apt install librewolf -y
sudo apt install librewolf -y
pyinstaller --onefile
pip install pyinstaller --onefile
pip install pyinstaller
./traductor.py
python3 -m pip install googletrans==4.0.0-rc1 --break-system-packages
ls -l
./traductor.py
sudo apt uptade
sudo apt update
sudo apt upgrade
chmod +x traductor.py
./traductor.py
nano traductor.py
pip install googletrans==4.0.0-rc1
sudo apt install python3
pip install googletrans==4.0.0-rc1
ls -l
sudo apt update
sudo apt install python3-venv
sudo apt install python3-full
mkdir mi_proyecto.py
ls -l
cd mi_proyecto.py
ls
python3 -m venv .venv
soure .venv/bin/activate
pip install googletrans==4.0.0-rc1
ipconfig
ipcofig
netstart
ls /
ls -l
nano mi_rpograma.cpp
nano hola.cpp
g++ --version
nano hola.cpp
ls
nano progam.cpp
nano hola_mundo.sh.save
suno apt install googletrans
[200~pip install googletrans==4.0.0-rc1~
pip install googletrans==4.0.0-rc1
nano traductor.py
ls
ls -l
chmod +x traductor.py
./traductor.py
nano traductor.py
ls -l
./traductor.py
python.py
pip install pyinstaller
pyinstaller --oneofile traductor.py
bash 
