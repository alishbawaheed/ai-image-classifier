# AI Image Classifier

A Python-based desktop application that allows users to classify images using a pre-trained MobileNet model. Users can upload an image, see the image displayed in the interface, get multiple predictions, and choose to classify additional images interactively.

👩‍💻 **Developed By**  
Alishba Waheed

---

## ✨ Features

- **Upload Image Button:** User-friendly button to upload an image for classification.
- **Image Display:** Shows the uploaded image directly in the interface.
- **Multiple Predictions:** Displays at least 3 class predictions with probabilities.
- **Interactive Workflow:** After classification, asks the user if they want to classify another image.
- **User Guidance:** If the user chooses not to continue, a thank-you message is displayed.

---

## 🖼️ Screenshots

1. **GUI / Upload Interface**  
![GUI](screenshots/gui.png)

2. **Image Display & Predictions**  
![Output](screenshots/output.png)



---

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or newer
- TensorFlow 2.20.0 (CPU version recommended for compatibility)
- Tkinter (usually comes with Python)
- PIL (Python Imaging Library)  

Install required libraries:

```bash
pip install tensorflow-cpu pillow

