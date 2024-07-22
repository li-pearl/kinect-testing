# Libfreenect on the Raspberry Pi 4

```
sudo apt-get update

sudo apt-get install git-core cmake freeglu3-dev pkg-config build-essential libxmu-dev libxi-dev libusb-1.0-0-dev

sudo git clone https://github.com/OpenKinect/libfreenect.git

```

cd into the libfreenect directory

```

sudo mkdir build

cd build

sudo apt-get install cmake

sudo cmake -L ..u

sudo make

sudo make install

sudo ldconfig /usr/local/lib64

sudo adduser $USER plugdev

sudo apt-get install gedit

sudo gedit /etc/udev/rules.d/51-kinect.rules

```
