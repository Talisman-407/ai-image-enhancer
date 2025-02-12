import os
from huggingface_hub import InferenceClient

HUGGING_FACE_TOKEN = os.getenv("HUGGING_FACE_TOKEN")

client = InferenceClient(
    provider="hf-inference",
    token=HUGGING_FACE_TOKEN,
    model="prompthero/openjourney-v4",
)
