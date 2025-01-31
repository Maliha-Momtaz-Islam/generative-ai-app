import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load fine-tuned model and tokenizer
model = AutoModelForCausalLM.from_pretrained("./models/my_finetuned_model")
tokenizer = AutoTokenizer.from_pretrained("./models/my_finetuned_model")

# Function to generate text
def generate_summary(radius_mean, texture_mean, perimeter_mean):
    prompt = (
        f"This sample has a radius mean of {radius_mean}, "
        f"texture mean of {texture_mean}, "
        f"and perimeter mean of {perimeter_mean}. "
        "The diagnosis is:"
    )
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=100)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Gradio interface
gr.Interface(
    fn=generate_summary,
    inputs=[
        gr.Slider(0, 30, label="Radius Mean"),
        gr.Slider(0, 50, label="Texture Mean"),
        gr.Slider(0, 200, label="Perimeter Mean"),
    ],
    outputs="textbox",
    title="Breast Cancer Data Summarizer",
    description="Enter feature values to generate a descriptive summary."
).launch()
