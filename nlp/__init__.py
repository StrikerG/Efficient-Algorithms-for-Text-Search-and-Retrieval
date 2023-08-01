# # Load model directly
# from transformers import AutoTokenizer, AutoModelForCausalLM
#
# tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-70b-chat-hf")
# model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-70b-chat-hf")

import torch

def check_gpu():
    if torch.cuda.is_available():
        gpu_count = torch.cuda.device_count()
        gpu_name = torch.cuda.get_device_name(0)
        print(f"GPU is available. Number of GPUs: {gpu_count}. GPU Name: {gpu_name}")
    else:
        print("GPU is not available. Using CPU.")

if __name__ == "__main__":
    check_gpu()
