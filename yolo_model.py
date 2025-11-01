'''
#Training code.

import torch
print(torch.__version__)
print(torch.cuda.is_available())
from ultralytics import YOLO
from multiprocessing import freeze_support
import time

def run_yolo_model():
    start = time.time()
    model = YOLO("yolov8n.pt")
    model.train(data="path_to_yaml", epochs=50, workers=4)
    print("Training time: ", time.time() - start)


if __name__ == '__main__':
    freeze_support()
    run_yolo_model()
'''

#Inference code.
from ultralytics import YOLO
import os

class YOLOModel:
    def __init__(self, model_path="/best.pt"):
        self.model = YOLO(model_path)
    
    def predict(self, image_path):
        # Run inference
        results = self.model.predict(source=image_path, save=True, save_txt=False)
        
        result_dir = results[0].save_dir
        saved_image_path = os.path.join(result_dir, os.path.basename(image_path))
        
        return saved_image_path

