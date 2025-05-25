# Image Forgery Detection Flask Application

This project is a Flask web application for detecting image forgery using a pre-trained Keras model. Users can upload images, and the application will process them to determine if they are real or fake.

## Project Structure

```
image-forgery-flask-app
├── app.py                     # Main entry point of the Flask application
├── model                      # Directory containing the trained model
│   └── image_forgery_detection_casia2.h5
├── static                     # Directory for static files
│   └── uploads                # Directory for temporarily storing uploaded images
├── templates                  # Directory for HTML templates
│   ├── index.html            # HTML form for uploading images
│   └── result.html           # HTML page for displaying prediction results
├── requirements.txt           # List of dependencies for the project
└── README.md                  # Documentation for the project
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone https://github.com/Shubham-741/Image-Forgery-Identification-System
   Run the image-forgery-detection.ipynb code. This will create a image_forgery_detection_casia2.h5 model.
   Dataset Used : https://www.kaggle.com/datasets/divg07/casia-20-image-tampering-detection-dataset/code
   cd image-forgery-flask-app
   ```

2. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the Flask application**:
   ```
   python app.py
   ```

5. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

- Navigate to the home page where you can upload an image.
- After uploading, the application will process the image and display the prediction results, indicating whether the image is real or fake along with the confidence level.

## Example

Below is an example image used in the application:

![HomePage](static/images/HomePage.jpg)
![SampleResult](static/images/SampleResult.jpg)

## Dependencies

- Flask
- Keras
- Pillow
- NumPy