import gradio as gr
import pandas as pd
import torch
import torchvision
from PIL import Image
from resnet import ResNet9, get_default_device, to_device

# Read classes from the classes.csv file
classes = pd.read_csv("classes.csv", encoding="utf-8")

# Convert the dataframe to a list
classes = classes["style"].tolist()


def predict(img):
    # Check sizes
    width, height = Image.fromarray(img).size

    # Resize if necessary
    if width != 32 or height != 32:
        img = Image.fromarray(img).resize((32, 32))

    # Convert to a torchvision tensor
    img = torchvision.transforms.ToTensor()(img)

    # Create the model
    device = get_default_device()
    model = to_device(ResNet9(3, 19), device)

    # Load the model's weights
    model.load_state_dict(torch.load('artcnn.pth', map_location=device))

    # Get predictions from model
    yb = model(to_device(img.unsqueeze(0), device))

    # Pick index with highest probability
    _, preds = torch.max(yb, dim=1)

    # Retrieve the class label
    label = classes[preds[0].item()]

    return f'The predicted style for this image is: {label}'


# Create a gradio interface
demo = gr.Interface(predict, "image", "textbox")
demo.launch()
