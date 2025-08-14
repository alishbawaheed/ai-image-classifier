import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import tensorflow as tf
from tensorflow.keras.applications.mobilenet import MobileNet, preprocess_input, decode_predictions
import numpy as np

# Load MobileNet model
model = MobileNet(weights='imagenet')

# Function to classify image
def classify_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if not file_path:
        return
    
    # Load and show the image
    img = Image.open(file_path)
    img_display = img.resize((250, 250))
    img_tk = ImageTk.PhotoImage(img_display)
    image_label.config(image=img_tk)
    image_label.image = img_tk
    
    # Preprocess for MobileNet
    img_resized = img.resize((224, 224))
    x = np.array(img_resized)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    
    # Prediction
    preds = model.predict(x)
    top_preds = decode_predictions(preds, top=3)[0]
    result_text = "Top 3 Predictions:\n"
    for i, (imagenet_id, name, score) in enumerate(top_preds, start=1):
        result_text += f"{i}. {name} ({score*100:.2f}%)\n"
    
    result_label.config(text=result_text + "\nDo you want to classify another image?")
    
    # Show Yes/No buttons
    upload_button.pack_forget()
    button_frame.pack(pady=10)

# Function to classify another image
def classify_another():
    result_label.config(text="")
    image_label.config(image="")
    button_frame.pack_forget()
    upload_button.pack(pady=20)

# Function for No option
def no_more():
    result_label.config(text="Thank you! Hope it helped you.")
    image_label.config(image="")
    button_frame.pack_forget()

# GUI setup
root = tk.Tk()
root.title("Image Classifier")
root.geometry("400x550")

# Welcome message
welcome_label = tk.Label(root, text="Hi! Please upload a picture to classify.", font=("Arial", 14))
welcome_label.pack(pady=20)

# Upload button
upload_button = tk.Button(root, text="Upload Image", command=classify_image, width=20, height=2)
upload_button.pack(pady=20)

# Image and result labels
image_label = tk.Label(root)
image_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Yes/No buttons
button_frame = tk.Frame(root)
yes_button = tk.Button(button_frame, text="Yes", command=classify_another, width=10)
no_button = tk.Button(button_frame, text="No", command=no_more, width=10)
yes_button.pack(side="left", padx=5)
no_button.pack(side="right", padx=5)

root.mainloop()




