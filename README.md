# 🖋️ Handwritten Persian Digit Recognizer

### Deep Learning Model for Recognizing Handwritten Persian Numbers (۰–۹)

A deep learning project using **TensorFlow / Keras** and **OpenCV**, trained on a **custom handwritten Persian digit dataset**.  
Each participant wrote Persian digits (۰–۹) by hand. The images were scanned, processed, segmented, and used to train a CNN model capable of recognizing Persian handwritten digits.

---

## 🚀 Project Overview

This repository implements a **Convolutional Neural Network (CNN)** to classify Persian handwritten digits.  
Unlike the standard MNIST dataset (English numerals), this dataset contains **real Persian numerals** collected and labeled manually.

### Main Steps

**1. Data Collection**  
- Handwritten Persian digits (۰–۹) collected from multiple individuals.  
- Each page was scanned and cropped into labeled samples.

**2. Preprocessing & Segmentation**  
- Used **OpenCV contour detection** to extract digits automatically.  
- All images resized to **28×28 pixels** and normalized to **[0, 1]**.  

**3. Model Architecture (CNN)**
```python
model = Sequential([
Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
MaxPooling2D((2,2)),
Dropout(0.25),
Flatten(),
Dense(128, activation='relu'),
Dropout(0.5),
Dense(10, activation='softmax')
])
```
Loss: Categorical Crossentropy
Optimizer: Adam
Metric: Accuracy
4. Training & Validation

Train/validation split: 80 % / 20 %
Data augmentation used (ImageDataGenerator):
rotation_range=10
width_shift_range=0.1
height_shift_range=0.1
zoom_range=0.1
✅ Training Accuracy: 93 – 99 %

✅ Validation Accuracy: 70 – 90 %

🧠 Technical Stack
Language: Python 3.9
Frameworks: TensorFlow, Keras
Image Processing: OpenCV
Visualization: Matplotlib
Dataset Tools: tf.data, ImageDataGenerator
📂 Dataset Structure

Handwritten_dataset/
│
├── 0/
├── 1/
├── 2/
├── 3/
├── 4/
├── 5/
├── 6/
├── 7/
├── 8/
└── 9/
Each folder contains grayscale images of Persian digits belonging to that label.

📊 Results
The CNN successfully recognizes Persian handwritten digits similarly to MNIST-level models.

Training accuracy: ~0.97 – 0.99
Validation accuracy: ~0.75 – 0.90
It can also detect multi-digit Persian numbers from segmentations generated via OpenCV.

Performance visualization (accuracy & loss curves) can be found inside the repository under /plots.

🔮 Future Improvements
Add more samples and handwriting variations.
Improve image preprocessing (denoising and thresholding).
Convert the trained model to TensorFlow Lite for mobile deployment.

