from ultralytics import YOLO

model = YOLO("best.pt")

# Use the camera as the source (0 for the default camera)
model.predict(source=0, show=True, save=False, conf=0.5)
