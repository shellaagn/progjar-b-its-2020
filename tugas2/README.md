# Tugas 2
05111740000107 - Shella Agustio Nainggolan <br>
Progjar B
<br>
1. Capture hasil keluaran dari program udpfileclient.py ke alamat 127.0.0.1 ke port 5006
	- Pada file udpfileclient.py, ubah **TARGET_IP = "127.0.0.1"** dan **TARGET_PORT = 5006**
	- Buka Wireshark, gunakan filter **"ip.src == 127.0.0.1 && ip.dst ==127.0.0.1 && udp.port==5006"**
	- Hasil:<br>
	![enter image description here](https://github.com/shellaagn/progjar-b-its-2020/blob/master/tugas2/udpfileclient-wireshark.JPG)

2. Capture hasil keluaran dari program udp_simple.py ke alamat 127.0.0.1 ke port 5006
	- 	Pada file udp_simple.py, ubah **TARGET_IP = "127.0.0.1"** dan **TARGET_PORT = 5006**
	- Buka Wireshark, gunakan filter **"ip.src == 127.0.0.1 && ip.dst ==127.0.0.1 && udp.port==5006"**
	- Hasil:<br>
	![enter image description here](https://github.com/shellaagn/progjar-b-its-2020/blob/master/tugas2/udp_simple-wireshark.JPG)
