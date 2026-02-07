{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "41445fa0",
   "metadata": {},
   "source": [
    "# Introduction to Hugging Face and Using its Models\n",
    "Welcome to this session on using Hugging Face models! This is guide is designed to introduce you to the world of Hugging Face and empower you to leverage its powerful tools for various machine learning tasks.\n",
    "\n",
    "## What is Hugging Face?\n",
    "Hugging Face is an open-source platform that has revolutionized the field of Natural Language Processing (NLP) and is rapidly expanding into other domains like computer vision and audio. Its core mission is to democratize access to cutting-edge machine learning models and tools, making it easier for everyone to build and deploy AI applications.\n",
    "\n",
    "Think of Hugging Face as a central hub for the ML community, offering:\n",
    "\n",
    "*   **A vast Model Hub:** A repository of thousands of pre-trained models for various tasks, contributed by researchers and developers worldwide. You can find models for text classification, translation, summarization, image recognition, audio transcription, and much more.\n",
    "*   **Powerful Libraries:** Open-source libraries like `transformers`, `datasets`, and `tokenizers` that provide easy-to-use interfaces for working with models, datasets, and text processing.\n",
    "*   **A Collaborative Community:** A vibrant community of ML practitioners who share models, datasets, and expertise.\n",
    "\n",
    "Hugging Face significantly reduces the barrier to entry for using state-of-the-art ML models, allowing you to quickly experiment and build applications without having to train models from scratch.\n",
    "\n",
    "## Managing Hugging Face Tokens\n",
    "To access some models or features on the Hugging Face Hub, you might need to use an API token. This token helps authenticate your requests and can be used to interact with the Hub programmatically, including downloading gated models or uploading your own.\n",
    "\n",
    "Here's how you can manage and verify your Hugging Face token:\n",
    "1.  **Obtain a Token:** Go to your Hugging Face profile settings (https://huggingface.co/settings/tokens) and generate a new access token. You can choose different roles for the token (e.g., read, write).\n",
    "2.  **Store your Token Securely:** It's crucial to store your token securely. In Google Colab, you can use the \"Secrets\" feature (🔑 icon in the left panel) to store your token as an environment variable. Name your secret `HF_TOKEN`.\n",
    "3.  **Log in Programmatically:** You can use the `huggingface_hub` library to log in to the Hugging Face Hub using your token.\n",
    "\n",
    "Let's add a code block to install the necessary library and verify your token."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8f2b1d61",
   "metadata": {},
   "outputs": [],
   "source": [
    "%pip install huggingface_hub"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "93715270",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "from dotenv import load_dotenv\n",
    "from huggingface_hub import whoami\n",
    "\n",
    "# Get your Hugging Face token from the .env file\n",
    "load_dotenv()\n",
    "hf_token = os.getenv(\"HF_TOKEN_AA\")\n",
    "\n",
    "# Authenticate with Hugging Face using the token\n",
    "try:\n",
    "    user_info = whoami(token=hf_token)\n",
    "    print(f\"Logged in as: {user_info['name']}\")\n",
    "except Exception as e:\n",
    "    print(f\"Error authenticating with Hugging Face: \\n{e}\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "59ca882a",
   "metadata": {},
   "source": [
    "## Showcasing Different Model Types\n",
    "\n",
    "Hugging Face isn't just about text! Let's explore how to use models for other modalities like images and audio, and also how to work with datasets.\n",
    "\n",
    "### Image Classification\n",
    "\n",
    "#Image classification is the task of categorizing an image into one of several classes. We can use a pre-trained image classification model from the Hugging Face Hub."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9c11efd0",
   "metadata": {},
   "outputs": [],
   "source": [
    "%pip install transformers pillow torch torchvision"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "fa0b1784",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "No model was supplied, defaulted to google/vit-base-patch16-224 and revision 3f49326.\n",
      "Using a pipeline without specifying a model name and revision in production is not recommended.\n",
      "Loading weights: 100%|██████████| 200/200 [00:00<00:00, 1164.57it/s, Materializing param=vit.layernorm.weight]                                \n",
      "Fast image processor class <class 'transformers.models.vit.image_processing_vit_fast.ViTImageProcessorFast'> is available for this model. Using slow image processor class. To use the fast image processor class set `use_fast=True`.\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Image classification results:\n",
      "- Egyptian cat: 0.86\n",
      "- tabby, tabby cat: 0.08\n",
      "- tiger cat: 0.06\n",
      "- lynx, catamount: 0.00\n",
      "- leopard, Panthera pardus: 0.00\n"
     ]
    }
   ],
   "source": [
    "import torch\n",
    "from transformers import pipeline\n",
    "from PIL import Image\n",
    "import requests\n",
    "from io import BytesIO\n",
    "\n",
    "# Determine device (use CPU for compatibility)\n",
    "device = 0 if torch.cuda.is_available() else -1\n",
    "\n",
    "# Load image classification pipeline with explicit device\n",
    "classifier = pipeline(\"image-classification\", device=device)\n",
    "\n",
    "# Get an image from a URL using a public image (cat photo)\n",
    "url = \"https://images.unsplash.com/photo-1574158622682-e40e69881006?w=400\"\n",
    "headers = {'User-Agent': 'Mozilla/5.0'}\n",
    "try:\n",
    "    response = requests.get(url, headers=headers, stream=True, timeout=10)\n",
    "    response.raise_for_status()\n",
    "    image = Image.open(BytesIO(response.content))\n",
    "    \n",
    "    # Classify the image\n",
    "    predictions = classifier(image)\n",
    "    \n",
    "    print(\"Image classification results:\")\n",
    "    for prediction in predictions:\n",
    "        print(f\"- {prediction['label']}: {prediction['score']:.2f}\")\n",
    "except Exception as e:\n",
    "    print(f\"Error: {e}\")\n",
    "    #print(\"\\nUsing a sample image instead...\")\n",
    "    \n",
    "    # Create a simple test image if URL fails\n",
    "    #test_image = Image.new('RGB', (224, 224), color='red')\n",
    "    #predictions = classifier(test_image)\n",
    "    #print(\"Image classification results:\")\n",
    "    #for prediction in predictions:\n",
    "        #print(f\"- {prediction['label']}: {prediction['score']:.2f}\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
