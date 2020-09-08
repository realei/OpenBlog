sudo apt-install python3-opencv
sudo apt-get install -y pkg-config

pip3 install yolo34py-gpu

result:
yolov3_net.detectImage(image="examples/flight_attendant.jpg")
[{'object': b'person', 'conficence': 0.9796929955482483, 'box': (116.1363525390625, 102.11215209960938, 90.18379211425781, 122.39525604248047)}, {'object': b'person', 'conficence': 0.9430640339851379, 'box': (52.88164138793945, 84.03394317626953, 112.10961151123047, 171.35459899902344)}]

yolov3_net = Detector(bytes(self.network, encoding="utf-8"), bytes(self.weights, encoding="utf-8"), 0, bytes(self.data, encoding="utf-8"))
yolov3_net.detectImage(image="examples/flight_attendant.jpg")
