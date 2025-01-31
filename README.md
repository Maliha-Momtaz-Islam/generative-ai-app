# generative-ai-app
This project fine-tunes a generative AI model (DeepSeek LLM) to create a text generation app.
# Generative AI App with Breast Cancer Wisconsin Dataset

This project fine-tunes a generative AI model (DeepSeek LLM) to create a text generation app using the Breast Cancer Wisconsin Dataset. The app generates descriptive summaries of breast cancer data based on user input.

## Features

- **Dataset**: Uses the Breast Cancer Wisconsin Dataset from Kaggle.
- **Fine-Tuning**: Fine-tunes a generative AI model to generate text summaries.
- **Web App**: Includes a Gradio interface for interacting with the model.

## Setup

1. **Clone this repository**:
   ```bash git clone https://github.com/yourusername/generative-ai-app.git```

2. **Install dependencies**:

```bash pip install -r requirements.txt```

3. **Download the dataset**:

Go to your Kaggle account settings and download your API token (kaggle.json).

Place the kaggle.json file in ~/.kaggle/ (on Linux/Mac) or C:\Users\<YourUsername>\.kaggle\ (on Windows).

Run the download script:

```bash
python download_data.py```

4. **Preprocess the data**:

```bash
python preprocess.py```

5. **Train the model**:

```bash
python train.py```

6. **Run the app**:

```bash
python app.py```

**Project Structure**

generative-ai-app/
│
├── data/
│   ├── data.csv            # Original dataset from Kaggle
│   └── training_data.txt   # Preprocessed text data
│
├── models/
│   └── my_finetuned_model/ # Fine-tuned model and tokenizer (generated after training)
│
├── app.py                  # Gradio app
├── train.py                # Training script
├── preprocess.py           # Script to generate training_data.txt
├── download_data.py        # Script to download the dataset from Kaggle
├── requirements.txt        # List of Python dependencies
├── README.md               # Project documentation
└── outputs/                # Sample outputs (optional)
    └── example_summary.txt

**Sample Outputs**
Here’s an example of output:

Input:

Radius Mean: 15

Texture Mean: 25

Perimeter Mean: 100

Output:

This sample has a radius mean of 15, texture mean of 25, and perimeter mean of 100. The diagnosis is likely benign, as the feature values fall within the normal range for healthy tissue.

**License**
This project is licensed under the MIT License. See LICENSE for details.
