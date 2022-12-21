import torch
import pandas as pd
import gradio as gr

def predict(img):
    # Convert the image to a tensor
    img_tensor = torch.from_numpy(img).float()

    # Add a batch dimension
    img_tensor = img_tensor.unsqueeze(0)

    # Get the model's prediction
    # prediction = model(img_tensor)

    # Get the index corresponding to the highest score
    # pred_idx = torch.argmax(prediction, dim=1)

    # Convert the index to a class name
    # pred_class = classes[pred_idx]

    return img_tensor


# Read classes from the classes.csv file
classes = pd.read_csv("classes.csv", encoding="utf-8")

# Convert the dataframe to a list
classes = classes["style"].tolist()

# Load the saved torch model
model = torch.load("artcnn.pth")

# Create a gradio interface
demo = gr.Interface(predict, "image", "textbox")
demo.launch(show_error=True)
