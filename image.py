import os
import warnings

# Must be set BEFORE importing transformers/huggingface_hub
os.environ["HF_HUB_DISABLE_IMPLICIT_TOKEN"] = "1"
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["TRANSFORMERS_VERBOSITY"] = "error"
os.environ["HF_HUB_VERBOSITY"] = "error"

import warnings
warnings.filterwarnings("ignore")

# Suppress huggingface_hub warnings specifically
import logging
logging.getLogger("huggingface_hub").setLevel(logging.ERROR)
logging.getLogger("transformers").setLevel(logging.ERROR)

from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Load model
processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

# Open image
image = Image.open("tree.jpg")

# Process image
inputs = processor(image, return_tensors="pt")

# Generate caption
output = model.generate(**inputs, max_new_tokens=20)

# Decode caption
caption = processor.decode(output[0], skip_special_tokens=True)

print("\nCaptioning Image:")
print(caption)