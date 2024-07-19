from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO("yolov8m.pt")
    model.train(data="data.yaml", batch=8, imgsz=640, epochs=100, workers=1)
