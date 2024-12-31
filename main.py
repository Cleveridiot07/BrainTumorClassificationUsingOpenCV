
import os
import logging
from fastapi import FastAPI, UploadFile, File
from keras.models import load_model
from PIL import Image
import numpy as np
from mangum import Mangum

# Suppress TensorFlow logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Configure logging for FastAPI
logging.basicConfig(level=logging.ERROR)

app = FastAPI()
handler = Mangum(app)

# Load the pre-trained model and compile
model = load_model('model/BrainTumor10EpochsCategorical.h5')
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Brain Tumor Detection API!"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        image = Image.open(file.file).convert('RGB')
        image = image.resize((64, 64))
        image_array = np.array(image)
        input_img = np.expand_dims(image_array, axis=0)

        result = model.predict(input_img)
        result_final = np.argmax(result, axis=1)

        if result_final[0] == 0:
            return {"prediction": "No Brain Tumor Detected"}
        else:
            return {"prediction": "Brain Tumor Detected"}
    except Exception as e:
        return {"error": str(e)}
