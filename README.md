# 🖼️ OpenCV Image Enhancer



![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)




![OpenCV](https://img.shields.io/badge/OpenCV-4.8-green)




![Gradio](https://img.shields.io/badge/Gradio-web--ui-orange)




![Status](https://img.shields.io/badge/status-active-brightgreen)




![License](https://img.shields.io/badge/license-MIT-lightgrey)



An advanced image enhancement tool built with **OpenCV** that improves photo quality through a multi-stage classical image-processing pipeline: noise reduction, adaptive contrast enhancement, sharpening, and 2x upscaling — all wrapped in a simple **Gradio** web interface.

---

## ✨ Features

| Feature | Technique | Purpose |
|---|---|---|
| **Noise Reduction** | Bilateral Filtering | Removes noise/grain while preserving edges |
| **Contrast Enhancement** | CLAHE (Contrast Limited Adaptive Histogram Equalization) | Improves local contrast without over-amplifying noise |
| **Sharpening** | Custom convolution kernel | Enhances fine details and edges |
| **Upscaling** | Cubic interpolation | Enlarges the image 2x while keeping edges smooth |
| **Final Sharpening** | Unsharp Masking | Adds a final crisp, high-detail finish |

---

## 📊 Processing Pipeline

The image passes through the following stages, in order:

1. **Bilateral Filter** → reduces noise while keeping edges sharp
2. **CLAHE** → enhances local contrast adaptively (usually applied on the L-channel in LAB color space)
3. **Sharpening Kernel** → convolves the image with a sharpening kernel to bring out detail
4. **2x Upscaling** → enlarges the image using `cv2.INTER_CUBIC` interpolation
5. **Unsharp Mask** → subtracts a blurred copy from the image to boost perceived sharpness

Input Image → Bilateral Filter → CLAHE → Sharpen → 2x Upscale → Unsharp Mask → Output Image

---

## 🚀 Quick Start

### Clone the repository

    git clone https://github.com/kamandNajari/Opencv-Image-Enhancer.git
    cd Opencv-Image-Enhancer

### Install dependencies

    pip install -r requirements.txt

### Run the app

    python app.py

Gradio will start a local web server (by default at `http://127.0.0.1:7860`) — open it in your browser to use the tool.

### Run on Google Colab

Alternatively, open `Opencv-Image_Enhancer.ipynb` in Google Colab and run all cells — no local installation required.

---

## 📋 Requirements

- Python 3.8+
- OpenCV (`opencv-python`)
- Gradio
- NumPy
- scikit-image

Full pinned versions are listed in `requirements.txt`.

---

## 📝 Usage

1. Upload your image (any common format: JPG, PNG, etc.)
2. Click **Submit**
3. Preview the enhanced result
4. Download the output image

**Works well with:**
- Low-resolution photos
- Blurry images
- Old or faded photos
- Both color and grayscale images

---

## ⚙️ Technical Details

| | |
|---|---|
| **Input** | Any standard image format (JPG, PNG, BMP, etc.) |
| **Output** | Enhanced image, 2x the original resolution |
| **Processing time** | ~2–5 seconds, depending on image size |
| **Interface** | Gradio web UI |
| **Core library** | OpenCV (classical image processing, no deep learning model required) |

---

## 📄 License

This project is licensed under the **MIT License** — see the LICENSE file for details.

---

## 👨‍💻 Author

**[kamandNajari](https://github.com/kamandNajari)**
