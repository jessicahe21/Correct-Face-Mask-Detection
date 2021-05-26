import os
import torch
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image
import urllib.parse
import numpy as np

model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'py_templates/simple_model_1.pth')
image_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

aug = transforms.Compose([        
        transforms.Resize((224,224)),
        #transforms.RandomHorizontalFlip(),
        #transforms.RandomAffine(degrees=0,translate=(0.2,0.2),scale=(0.8,1.2)),
        transforms.ToTensor()]
)

# load model
model = models.resnet18(pretrained=False)
model.fc = nn.Linear(model.fc.in_features, 2)
model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
model.eval()

# predict labels
def image_pred(url):
    new_url = image_path + url
    raw_url = urllib.parse.unquote(new_url)
    img = Image.open(raw_url)
    img = img.convert(mode='RGB')
    image = aug(img)
    image = image.unsqueeze(0)
    model.eval()
    out = model(image)
    out = out.detach().numpy()
    out = np.argmax(out)
    return out
