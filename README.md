# 🪖 BattleEye  

## Deep learning–powered object detection framework using YOLOv8 for defense and surveillance applications.  

**BattleEye** is a web-based intelligent vision system built with **Flask** and **YOLOv8**.  
It allows users to upload images and automatically detect and classify various **military** and **civilian** vehicles and aircraft.  
The model is trained on a **custom defense dataset** featuring six distinct object classes.  
*_(Video inference functionality coming soon!)_*

---

## 🚀 Features

- 📸 Upload an image through an intuitive web interface  
- 🤖 Object detection powered by **YOLOv8 (Ultralytics)**  
- 🧩 Detects both **civilian** and **military** vehicles/aircraft  
- 💾 Automatically processes and displays detection results  
- 🧠 Modular design separating model logic and Flask routes  
- ⚡ Real-time inference with bounding boxes and confidence scores  

---

## 🧠 Model Information

- **Model Architecture:** YOLOv8 (PyTorch, Ultralytics)
- **Trained Weights:** `best.pt`  
- **Classes:**  
  - Civilian Aircraft ✈️  
  - Civilian Car 🚗  
  - Military Aircraft 🛩️  
  - Military Helicopter 🚁  
  - Military Tank 🪖  
  - Military Truck 🚚
- **Framework:** PyTorch  
- **Backend Integration:** Flask  

---

## 🔄 Application Flow

1. **User Uploads Image**  
   The image is sent from the HTML form to the Flask backend (`app.py`).

2. **Flask Handles Request**  
   The app saves the image to the `uploads/` directory and passes its path to `yolo_model.py`.

3. **YOLO Inference**  
   The `run_yolo_inference(image_path)` function loads the trained YOLOv8 model (`best.pt`) and performs detection.

4. **Result Generation**  
   The processed image with bounding boxes and class labels is saved to the `runs/detect/predict/` folder.

5. **Result Display**  
   Flask dynamically loads and renders the processed image on the webpage using the result path.

---

## 🧰 Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend** | HTML, CSS (Jinja2 Templates) |
| **Backend** | Flask (Python) |
| **Model** | YOLOv8 (Ultralytics) |
| **Framework** | PyTorch |
| **Inference** | Custom YOLO model integrated with Flask |

---

## 🧩 File Overview

### `app.py`
- Initializes the Flask application  
- Handles image upload and result rendering  
- Connects the user interface with YOLO inference logic  

### `yolo_model.py`
- Contains all YOLOv8 inference code  
- Loads model weights (`best.pt`) and performs detection  
- Returns the path to the output image for display  

### `requirements.txt`
- Lists all Python dependencies (Flask, Ultralytics, Torch, OpenCV, etc.)

---

## 📦 Requirements
- ultralytics
- pandas
- numpy
- fastapi
- jinja2
- python-multipart



