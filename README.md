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
  - Civilian Aircraft
  - Civilian Car
  - Military Aircraft 
  - Military Helicopter
  - Military Tank
  - Military Truck
- **Framework:** PyTorch  
- **Backend Integration:** Flask  

---

## 🔄 Application Flow

1. **User Uploads Image**  
   - The image is sent from the HTML form to the Flask backend (`app.py`).
   - On form submission, a POST request is sent to the Flask backend (`/predict` route).
   - The uploaded image is accessed in Flask and saved to `/uploads` folder.

2. **Flask Handles Request**  
   - After the image is saved the flask calls the YOLO inference function `yolo_model.predict`.
   - The annotated image path is returned and stored in the variable `processed_image_path`.

4. **YOLO Inference**  
   - The `predict(image_path)` function in `yolo_model.py` is called and it performs detection.
   - Then after this a full output path is generated for locating the annotated image.
   - This full output image path is stored in `processed_image_path` as mentioned earlier.
   
5. **Result Generation**  
   - The processed image with bounding boxes and class labels is saved to the `runs/detect/predict/` folder.

6. **Result Display**  
   - Flask dynamically loads and renders the processed image on the webpage using the `result.html` page.

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

### `index.html`
- Contains the code for landing page and image uploading.

### `result.html`
- Contains the code for displaying the annotated image.

---

## 📦 Requirements
- ultralytics
- pandas
- numpy
- fastapi
- jinja2
- python-multipart

## Running the model
The repository include the frontend code (`index.html` & `result.html`), backend code(`app.py`), Yolo training and inferencing code(`yolo_model.py`) as well as trained model weights i.e `best.pt`.
Since the trained model weights (`best.pt`) are already included, users can directly run inference without retraining the model.

1. Clone the repository.
2. Then replace the `model_path` with the appropriate directory path.
3. Create a seperate `uploads` folder to save the uploaded images. In case you haven't, the `app.py` will generate the folder if it doesn't exist.
4. By default, the annotated image is stored in /runs/detect/predict due to `save=True` in `yolo_model.py`.

