import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# -----------------------------------
# Load Model
# -----------------------------------
@st.cache_resource
def load_model():
    model_path = "model/arecanut_resnet_final.keras"
    model = tf.keras.models.load_model(model_path)
    return model

model = load_model()

# -----------------------------------
# Class Labels
# -----------------------------------
CLASS_NAMES = [
    "Healthy_Leaf",
    "Healthy_Nut",
    "Healthy_Trunk",
    "Mahali_Koleroga",
    "Stem_bleeding",
    "bud borer",
    "healthy_foot",
    "stem cracking",
    "yellow leaf disease"
]

# -----------------------------------
# Preprocessing
# -----------------------------------
def preprocess_image(img):
    img = img.resize((224, 224))   # ResNet expected size
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    return img

# -----------------------------------
# Prediction
# -----------------------------------
def predict(img):
    img_array = preprocess_image(img)
    preds = model.predict(img_array)
    class_id = np.argmax(preds)
    confidence = np.max(preds)
    return CLASS_NAMES[class_id], confidence

# -----------------------------------
# Streamlit UI
# -----------------------------------
st.title("🌴 Arecanut Disease Detection")
st.write("Upload an arecanut leaf/nut/trunk image to detect the disease.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Image", use_column_width=True)

    if st.button("Predict"):
        with st.spinner("Analyzing image..."):
            label, confidence = predict(img)
        
        st.success(f"**Prediction:** {label}")
        st.info(f"**Confidence:** {confidence*100:.2f}%")
