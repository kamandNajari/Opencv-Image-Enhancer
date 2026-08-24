import cv2
import numpy as np
from PIL import Image
import gradio as gr

def enhance_image(input_image):
    img = np.array(input_image)
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    denoised = cv2.bilateralFilter(img_bgr, 9, 75, 75)
    
    lab = cv2.cvtColor(denoised, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    l_clahe = clahe.apply(l)
    
    lab_enhanced = cv2.merge([l_clahe, a, b])
    enhanced = cv2.cvtColor(lab_enhanced, cv2.COLOR_LAB2BGR)
    
    kernel = np.array([[-1,-1,-1],
                       [-1, 9,-1],
                       [-1,-1,-1]])
    sharpened = cv2.filter2D(enhanced, -1, kernel)
    
    h, w = sharpened.shape[:2]
    upscaled = cv2.resize(sharpened, (w*2, h*2), interpolation=cv2.INTER_CUBIC)
    
    blurred = cv2.GaussianBlur(upscaled, (0, 0), 1.0)
    unsharp = cv2.addWeighted(upscaled, 1.5, blurred, -0.5, 0)
    
    result = cv2.cvtColor(unsharp, cv2.COLOR_BGR2RGB)
    
    return Image.fromarray(result.astype('uint8'))

demo = gr.Interface(
    fn=enhance_image,
    inputs=gr.Image(type="pil", label="Upload photo"),
    outputs=gr.Image(label="Enhanced Result"),
    title="Image Enhancer",
    description="Enhance photo quality with OpenCV"
)
if __name__=="__main__":
    demo.launch()


