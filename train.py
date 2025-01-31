from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments, TextDataset, DataCollatorForLanguageModeling

# Load model and tokenizer
model_name = "deepseek-ai/deepseek-llm-7b-base"  # Replace with your model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Load dataset
train_dataset = TextDataset(
    tokenizer=tokenizer,
    file_path="data/training_data.txt",
    block_size=128
)

# Set up training
training_args = TrainingArguments(
    output_dir="./models/my_finetuned_model",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    save_steps=500,
    logging_steps=100,
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=DataCollatorForLanguageModeling(tokenizer, mlm=False),
    train_dataset=train_dataset,
)

# Train and save the model
trainer.train()
trainer.save_model("./models/my_finetuned_model")
tokenizer.save_pretrained("./models/my_finetuned_model")

print("Fine-tuning complete. Model saved to models/my_finetuned_model.")
