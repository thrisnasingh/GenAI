import requests
import os
import base64
from PIL import Image
from io import BytesIO

def generate_image_from_model(prompt):
    model_id = "03yd9kk3"
    baseten_api_key = "9ITFpBSs.txHgts35PvWcJ6N3Zasx0OVunF3pYmNe"

    data = {
        "prompt": prompt,
        "negative_prompt": "blurry, low quality",
        "steps": 30
    }

    # Call model endpoint
    res = requests.post(
        f"https://model-{model_id}.api.baseten.co/production/predict",
        headers={"Authorization": f"Api-Key {baseten_api_key}"},
        json=data
    )

    # Get output image
    res = res.json()
    output = res.get("output")

    # Convert the base64 model output to an image
    img_bytes = base64.b64decode(output)
    img = Image.open(BytesIO(img_bytes))

    return img
