import time
import errno
import os

import cv2
from pydarknet import Detector, Image

class Darknet():
    """
    Wrap Darknet for video processing
    detail reference pleae:
    https://pjreddie.com/darknet
    Example:
        yolov3_net = Darknet(network="darknet/cfg/yolov3.cfg", 
                             weights="weights/yolov3.weights", 
                             data="darknet/cfg/coco.data")
    Attributes:
        network: Deep Learning Network configuration file based on Darknet
        weights: The trained weights file for Deep Learning Network 
        data: The objects type name file according to the tained weigits
    """
    def __init__(self, network=None, weights=None, data=None):
        self.network = network if self.__isExists__(network) else "./darknet/cfg/yolov3.cfg"
        self.weights = weights if self.__isExists__(weights) else "./weights/yolov3.weights"
        self.data = data if self.__isExists__(data) else "./darknet/cfg/coco.data"
        self.yolov3_net = Detector(bytes(self.network, encoding="utf-8"), 
                                   bytes(self.weights, encoding="utf-8"), 
                                   0,
                                   bytes(self.data, encoding="utf-8"))

    def __isExists__(self, file=None):
        """
        Check file's existence
        """
        if not os.path.isfile(file):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file)
        else:
            return True

    def detectImage(self, image=None):
        """
        Object detection for images
        Input:
            image (string): Target image files
        Output:
            (Dict): Detected objects in Dict data type
        """

        self.__isExists__(image)

        results = []
        bgr_img = cv2.imread(image)
        dark_frame = Image(bgr_img)
        obj_info = self.yolov3_net.detect(dark_frame)
        del dark_frame

        for data in obj_info:
            results.append({
                "object": data[0],
                "conficence":data[1],
                "box": data[2]
                })


        return results

    def detectVideos(self, video=None, count=1):
        """
        Object detection for videos
        
        Input:
            video (string): Target video files
            count (int): Interval of frames of procxessing videos
        Output:
            (List): Detected objects in List data type
        """

        self.__isExists__(video)

        cap = cv2.VideoCapture(video)
        frame_number = 0
        average_time = 0
        videoResults = []

        while True:
            success, frame = cap.read()
            if not success:
                print("video is all read")
                break

            frame_number += 1
            if (frame_number % count == 0):
                start_time = time.time()
                dark_frame = Image(frame)
                results = self.yolov3_net.detect(dark_frame)
                del dark_frame

                videoResults.append({
                    "frameIndex": frame_number,
                    "objectsInfo": results
                    })

                end_time = time.time()
                average_time = average_time * 0.8 + (end_time-start_time) * 0.2

                # Frames per second can be calculated as 1 frame 
                # divided by time required to process 1 frame
                fps = 1 / (end_time - start_time)
                print("FPS: ", fps)
                print("Total Time:", end_time-start_time, ":", average_time)

        return videoResults
