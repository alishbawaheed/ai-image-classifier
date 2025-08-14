# AI Image Classifier

A Python-based desktop application that allows users to classify images using a pre-trained MobileNet model. Users can upload an image, see it displayed in the interface, get multiple predictions, and choose to classify additional images interactively.

## 👩‍💻 Developed By
Alishba Waheed

## ✨ Features

Upload Image Button: User-friendly button to upload an image for classification.

Image Display: Shows the uploaded image directly in the interface.

Multiple Predictions: Displays at least 3 class predictions with probabilities.

Interactive Workflow: After classification, asks the user if they want to classify another image.

User Guidance: If the user chooses not to continue, a thank-you message is displayed.

## 🖼️ Screenshots

GUI / Upload Interface


Image Display & Predictions


## 🚀 Getting Started
### Prerequisites

Python 3.11 or newer

TensorFlow 2.20.0 (CPU version recommended)

Tkinter (usually comes with Python)

PIL (Python Imaging Library)

### Install required libraries:

pip install tensorflow-cpu pillow

### How to Run

1. Clone this repository:

git clone https://github.com/<your-username>/AI-Image-Classifier.git


2. Open in VS Code:

Go to File > Open and select the AI-Image-Classifier folder.

Activate your virtual environment (if using one):

.\.venv_py311\Scripts\Activate.ps1


3. Run the App:

python image_classifier.py

## 🗂️ Project Structure

AI-Image-Classifier/

├── .venv_py311/           
├── image_classifier.py     
├── gui.png                 
├── output.png              
├── README.md              
└── .gitignore              


## 💡 Usage

Open the app.

Click Upload Image.

Select an image from your computer.

See the uploaded image displayed in the window.

Get the top 3 predictions with their probabilities.

When prompted, choose Yes to classify another image or No to end.

If No, the app displays:

Thank you! Hope it helped.

## 🛠️ Technologies Used

Python 3.11

TensorFlow 2.20.0 (CPU)

Tkinter

PIL (Python Imaging Library)

VS Code
