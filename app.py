from flask import Flask, request, render_template, send_from_directory
import os
from yolo_model import YOLOModel

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

yolo_model = YOLOModel()  # Load model once at startup


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'image_file' not in request.files:
            return "No file part"
        
        file = request.files['image_file']
        if file.filename == '':
            return "No selected file"
        
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            
            # Run YOLO prediction
            processed_image_path = yolo_model.predict(filepath)
            
            # Render result page
            return render_template('result.html', result_image=processed_image_path)
    
    return render_template('index.html')


@app.route('/runs/<path:filename>')
def serve_detected_image(filename):
    return send_from_directory('runs', filename)


if __name__ == '__main__':
    app.run(debug=True)
