import gradio as gr
import joblib
import numpy as np

model = joblib.load("model.pkl")

def predict(gender, age, salary):
    gender = 1 if gender == "Male" else 0
    data = np.array([[gender, age, salary]])
    prediction = model.predict(data)[0]

    if prediction == 1:
        return "✅ User is likely to purchase the ad"
    else:
        return "❌ User is unlikely to purchase the ad"

interface = gr.Interface(
    fn=predict,
    inputs=[
        gr.Radio(["Male", "Female"], label="Gender"),
        gr.Number(label="Age"),
        gr.Number(label="Estimated Salary")
    ],
    outputs="text",
    title="Social Network Ads Click Prediction",
    description="Predict whether a user will click on an advertisement"
)

interface.launch()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                