# Object Detection with YOLO v8 & PyTorch
*A beginner‑friendly project for detecting objects using YOLOv8 in PyTorch*

## ✅ What this repository is
This repo provides:
- A working implementation of object detection using YOLOv8 and PyTorch.
- A guide to follow along with the accompanying video tutorial.
- Sample scripts, dataset structure, and instructions so you can get up and running quickly.

## 🔍 Key Highlights
- **Simple setup**: Minimal dependencies, clear instructions.
- **Fully worked‑example**: Scripts to train and test on a small face‑detection dataset (or your custom dataset).
- **Beginner‑friendly**: No previous deep‑learning experience required — you’ll follow the tutorial step‑by‑step.

## 🛠️ What’s inside
```
├── train.py             # Script to train the YOLOv8 model
├── test.py              # Script to test/detect objects on images or video
├── data.yaml            # Data configuration file (classes, paths)
├── classes.txt          # Text file listing class names
├── requirements.txt     # Python dependencies
└── runs/                 # Folder where training/detection outputs are saved
    ├── detect/          # Outputs from detection runs
    └── train/           # Training logs, weights, etc
```

## 🚀 Getting Started

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Prepare your dataset
- Update `data.yaml` with your dataset paths and class names.
- Ensure `classes.txt` lists each class name, one per line.

### 3. Train the model
```bash
python train.py --data data.yaml --img 640 --epochs 50 --batch 16
```
_You can adjust `--img`, `--epochs`, and `--batch` based on your machine._

### 4. Run detection / inference
```bash
python test.py --weights runs/train/weights/best.pt --source path/to/images_or_video
```
Output will be saved under `runs/detect/`.

## 🎥 Video Tutorial
Check out the accompanying tutorial video (link below) for a full walkthrough, step‑by‑step:  
[Video Link Here] (insert your video link)

## 🧑‍💻 Why this approach?
YOLOv8 is a state‑of‑the‑art, efficient object detector that is easy to use and high performing. PyTorch provides a flexible foundation for customising and extending detection workflows. This combination is ideal for beginners who want to build real‑world detection systems.

## 📋 License & Contributions
Feel free to use, modify, and experiment. Pull requests are welcome.  
If you find improvements or refinements – create an issue or submit a PR.

---

⭐ If this project helps you — please give it a star!
