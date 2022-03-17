from yolov5 import train1, detect

if _name_ == '_main_':
    train1.run(imgsz=416, data='scratch.yaml', weight='yolov5s.pt',epochs=400, worker= 4)
