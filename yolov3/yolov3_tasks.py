import os
from celery import Celery

from objdetect import Darknet


app = Celery('yolov3_tasks', broker='amqp://guest@localhost//')

CUR_PATH = os.getcwd()
CFG = os.path.join(CUR_PATH, "darknet/cfg/yolov3.cfg")
WEIGHTS = os.path.join(CUR_PATH, "weights/yolov3.weights")  
DATA = os.path.join(CUR_PATH, "darknet/cfg/coco.data")
EXAMPLE = os.path.join(CUR_PATH, "examples/flight_attendant.jpg")
yolov3_net = Darknet(network=CFG, weights=WEIGHTS, data=DATA)

@app.task
def yolo_identify(image=EXAMPLE):
    return yolov3_net.detectImage(image=image)


