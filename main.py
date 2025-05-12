from transformers import pipeline
from datasets import load_dataset
import soundfile as sf
import torch
import os

os.makedirs('output', exist_ok=True)

device = "cuda" if torch.cuda.is_available() else "cpu"

synthesiser = pipeline("text-to-speech", "microsoft/speecht5_tts", device=device)

embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
speaker_embedding = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

speech = synthesiser("What's your favorite coffee?", forward_params={"speaker_embeddings": speaker_embedding})

sf.write("data/favorite_coffee.wav", speech["audio"], samplerate=speech["sampling_rate"])

print("Done!")
