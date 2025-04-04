#!/usr/bin/env python3
import os
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from faster_whisper import WhisperModel

def download_whisper_model():
    print("Downloading Whisper model...")
    model_size = "medium"
    # This will download and cache the model
    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    print(f"Whisper {model_size} model downloaded successfully!")
    return model

def download_translation_model():
    print("Downloading translation model (English to Chinese)...")
    model_name = "Helsinki-NLP/opus-mt-en-zh"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    print("Translation model downloaded successfully!")
    return model, tokenizer

if __name__ == "__main__":
    print("Starting to download required models...")
    
    # Check for CUDA availability
    if torch.cuda.is_available():
        print("CUDA is available! Models will use GPU acceleration when running.")
    else:
        print("CUDA is not available. Models will run on CPU (slower).")
    
    # Download models
    whisper_model = download_whisper_model()
    translation_model, tokenizer = download_translation_model()
    
    print("\nAll models downloaded and ready to use!")
    print("You can now run main.py to generate subtitles for your videos.")

