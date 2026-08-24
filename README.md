# 🖼️ OpenCV Image Enhancer

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8-green)
![Gradio](https://img.shields.io/badge/Gradio-web--ui-orange)
![Status](https://img.shields.io/badge/status-active-brightgreen)

**Image Enhancer** is a powerful desktop/web application built with OpenCV that enhances image quality through advanced algorithms. It reduces noise, improves contrast, sharpens details, and upscales images — all in one click.

---

## ✨ Features

- **Noise Reduction** — Bilateral filtering removes noise while preserving edges
- **Contrast Enhancement** — CLAHE for adaptive histogram equalization
- **Sharpening** — Custom kernel-based detail enhancement
- **Upscaling** — 2x image enlargement with cubic interpolation
- **Unsharp Mask** — Final enhancement for crisp results

---

## 📊 Processing Pipeline

1. **Bilateral Filter** → Reduce noise
2. **CLAHE** → Enhance contrast
3. **Sharpening Kernel** → Add details
4. **2x Upscaling** → Enlarge image
5. **Unsharp Mask** → Final sharpening

---

## 🚀 Quick Start

### On Google Colab
Open `Opencv-Image_Enhancer.ipynb` in Colab and run all cells

### Locally
```bash
pip install -r requirements.txt
python app.py
## 📋 Requirements

- Python 3.8+
- OpenCV
- Gradio
- NumPy
- scikit-image

See `requirements.txt` for full list.

---

## 📝 Usage

1. Upload your image (any format)
2. Click "Submit"
3. Download enhanced result

Works with:
- Low-resolution photos
- Blurry images
- Old/faded photos
- Color and grayscale images

---

## ⚙️ Technical Details

**Input:** Any image format (JPG, PNG, etc.)
**Output:** Enhanced 2x larger image
**Processing Time:** Depends on image size (typically 2-5 seconds)

---

## 📄 License

MIT License — See LICENSE file

---

## 👨‍💻 Author

[kamandNajari](https://github.com/kamandNajari)

---

### 🚀 Clone this project

```bash
git clone https://github.com/kamandNajari/opencv-image-enhancer.git
