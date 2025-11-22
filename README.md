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
