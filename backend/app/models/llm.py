from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

def load_model():
    model_name = "gpt2"  # Replace with e.g. "mistralai/Mistral-7B-Instruct" for better performance
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return model

model = load_model()
tokenizer = AutoTokenizer.from_pretrained("gpt2")