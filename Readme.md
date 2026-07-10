# 📷 Photo Editor using OpenCV and Streamlit

## Project Overview

Photo Editor is an interactive web application built using OpenCV and Streamlit that allows users to perform real-time image editing directly from their browser. Users can upload an image, apply various image processing operations, preview the results instantly, and download the edited image.

The project demonstrates practical applications of Computer Vision and Image Processing techniques using Python.

---

## Features

### Basic Editing Features

* Upload images (JPG, JPEG, PNG)
* Resize images
* Adjust brightness
* Adjust contrast
* Convert image to grayscale
* Apply blur effect
* Apply sharpen effect
* Apply warm filter
* Portrait-style background blur
* Download edited image

### Additional Features

* Edge Detection
* Sketch Effect
* Image Rotation

---

## Technologies Used

* Python
* OpenCV
* Streamlit
* NumPy
* Pillow

---

## Project Structure

```text
Photo-Editor-OpenCV-Streamlit/
│
├── app.py
├── requirements.txt
├── README.md
├── sample_images/
└── output/
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Photo-Editor-OpenCV-Streamlit.git
```

### 2. Navigate to Project Folder

```bash
cd Photo-Editor-OpenCV-Streamlit
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

After running the command, Streamlit will automatically open the application in your default browser.

---

## Application Workflow

```text
Upload Image
      ↓
Resize Image
      ↓
Adjust Brightness & Contrast
      ↓
Apply Filters & Effects
      ↓
Preview Edited Image
      ↓
Download Edited Image
```

---

## Image Processing Features Explained

### Brightness Adjustment

Controls the intensity of image pixels to make the image brighter or darker.

### Contrast Adjustment

Enhances the difference between light and dark areas of the image.

### Grayscale Conversion

Converts a color image into a black-and-white representation.

### Blur Effect

Applies Gaussian Blur to reduce image details and smooth the image.

### Warm Filter

Enhances red tones to create a warmer appearance.

### Portrait Blur

Simulates a portrait photography effect by blurring the background while keeping the center region clearer.

### Sharpen Filter

Enhances image edges and details using a sharpening kernel.

### Edge Detection

Detects object boundaries using the Canny Edge Detection algorithm.

### Sketch Effect

Transforms an image into a pencil sketch appearance.

### Rotation

Rotates the image by a user-selected angle.

---

## Learning Outcomes

Through this project, I learned:

* Fundamentals of OpenCV image processing
* Building interactive web applications using Streamlit
* Image enhancement and filtering techniques
* Real-time image manipulation using Python
* Deploying and sharing machine learning/computer vision projects

---

## Future Enhancements

* Cartoon Effect
* Face Detection
* Background Replacement
* Image Cropping Tool
* HDR Effect
* Real-time Webcam Filters

---

## Screenshots

Add screenshots of:

* Home Page
* Image Upload
* Filter Application
* Final Edited Image

---

## Author

Siva Kumar Katari

## License

This project is open-source and available under the MIT License.
