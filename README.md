📄 README.md 
# 🌴 Arecanut Disease Detection (Deep Learning + Streamlit)

This project uses a deep learning model (ResNet-based classifier) to detect **arecanut plant diseases** from images of leaves, nuts, trunks, and other plant parts.  
The model is deployed using **Streamlit** for easy web access.

---

## 🚀 Live Demo  
(Once deployed on Streamlit Cloud, paste your link here)

---

## 📦 Features

- ✔ Detects 9 classes of arecanut plant conditions  
- ✔ Trained on an 8.2GB dataset  
- ✔ Real-time image upload and prediction  
- ✔ Lightweight Streamlit web app  
- ✔ Supports `.jpg`, `.jpeg`, `.png` images  

---

## 🧠 Model Information

The model used for deployment is:



arecanut_resnet_final.keras


This model was trained using TensorFlow/Keras and exported in the recommended `.keras` format.

### Class Labels



Healthy_Leaf

Healthy_Nut

Healthy_Trunk

Mahali_Koleroga

Stem_bleeding

bud borer

healthy_foot

stem cracking

yellow leaf disease


---

## 📁 Project Structure



arecanut-disease/
├── app.py
├── requirements.txt
├── model/
│ └── arecanut_resnet_final.keras
├── README.md


---

## ▶️ Running Locally

Install dependencies:

```bash
pip install -r requirements.txt


Run the app:

streamlit run app.py

☁️ Deployment (Streamlit Cloud)

Push repo to GitHub

Go to https://streamlit.io/cloud

Create a new app

Select this repository

Set main file to:

app.py


Deploy 🎉

📬 Contact

If you want help improving the model or app, feel free to open an issue or message me.


---

# ✅ Next Step for You
Now:

### 👉 Go to GitHub → Click *Add README* → Paste the above content → Save.

If you want, I can also help you:

- Fix deploy errors  
- Add loading animation  
- Add confidence bars  
- Add sample images  
- Add mobile-friendly UI  

Just tell me **what you want improved**.
