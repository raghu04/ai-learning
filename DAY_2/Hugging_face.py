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
   "execution_count": 2,
   "id": "93715270",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/raghus/Projects/outskill/ai-accelerator/.venv/lib/python3.14/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user_install.html\n",
      "  from .autonotebook import tqdm as notebook_tqdm\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Logged in as: raghujs\n"
     ]
    }
   ],
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
      "Loading weights: 100%|██████████| 200/200 [00:00<00:00, 920.49it/s, Materializing param=vit.layernorm.weight]                                 \n",
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
  },
  {
   "cell_type": "markdown",
   "id": "3f6b166c",
   "metadata": {},
   "source": [
    "### Audio Classification\n",
    "\n",
    "Audio classification is the task of categorizing audio data into different classes, such as identifying the type of sound or the speaker's emotion."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b5288646",
   "metadata": {},
   "outputs": [],
   "source": [
    "%pip install soundfile"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ded394b7",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Loading weights: 100%|██████████| 216/216 [00:00<00:00, 1595.23it/s, Materializing param=wav2vec2.masked_spec_embed]                                            \n",
      "Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Audio classification results:\n",
      "- _silence_: 1.00\n",
      "- right: 0.00\n",
      "- _unknown_: 0.00\n",
      "- left: 0.00\n",
      "- yes: 0.00\n",
      "- down: 0.00\n",
      "- stop: 0.00\n",
      "- off: 0.00\n",
      "- no: 0.00\n",
      "- up: 0.00\n",
      "- go: 0.00\n",
      "- on: 0.00\n"
     ]
    }
   ],
   "source": [
    "from transformers import pipeline\n",
    "import torch\n",
    "import soundfile as sf\n",
    "\n",
    "# Load an audio classification pipeline\n",
    "classifier = pipeline(\"audio-classification\", model=\"superb/wav2vec2-base-superb-ks\")\n",
    "\n",
    "# A simple sine wave, you would load your actual audio data\n",
    "dummy_audio = torch.randn(16000)  # 1 second of random noise at 16kHz\n",
    "sf.write(\"dummy_audio.wav\", dummy_audio.numpy(), 16000)\n",
    "\n",
    "# Classify the audio\n",
    "audio_file = \"dummy_audio.wav\"\n",
    "predictions = classifier(audio_file)\n",
    "\n",
    "print(\"Audio classification results:\")\n",
    "for prediction in predictions:\n",
    "    print(f\"- {prediction['label']}: {prediction['score']:.2f}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2c9f88df",
   "metadata": {},
   "source": [
    "### Working with Datasets\n",
    "\n",
    "Hugging Face provides the `datasets` library, which makes it easy to access and work with a wide variety of datasets for various ML tasks."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0469fe4f",
   "metadata": {},
   "outputs": [],
   "source": [
    "%pip install datasets"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e15bbf88",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "DatasetDict({\n",
      "    train: Dataset({\n",
      "        features: ['id', 'title', 'context', 'question', 'answers'],\n",
      "        num_rows: 87599\n",
      "    })\n",
      "    validation: Dataset({\n",
      "        features: ['id', 'title', 'context', 'question', 'answers'],\n",
      "        num_rows: 10570\n",
      "    })\n",
      "})\n",
      "\n",
      "Example from the training set:\n",
      "{'id': '5733be284776f41900661182', 'title': 'University_of_Notre_Dame', 'context': 'Architecturally, the school has a Catholic character. Atop the Main Building\\'s gold dome is a golden statue of the Virgin Mary. Immediately in front of the Main Building and facing it, is a copper statue of Christ with arms upraised with the legend \"Venite Ad Me Omnes\". Next to the Main Building is the Basilica of the Sacred Heart. Immediately behind the basilica is the Grotto, a Marian place of prayer and reflection. It is a replica of the grotto at Lourdes, France where the Virgin Mary reputedly appeared to Saint Bernadette Soubirous in 1858. At the end of the main drive (and in a direct line that connects through 3 statues and the Gold Dome), is a simple, modern stone statue of Mary.', 'question': 'To whom did the Virgin Mary allegedly appear in 1858 in Lourdes France?', 'answers': {'text': ['Saint Bernadette Soubirous'], 'answer_start': [515]}}\n"
     ]
    }
   ],
   "source": [
    "from datasets import load_dataset\n",
    "\n",
    "# Load a dataset (e.g., the SQuAD dataset for question answering)\n",
    "dataset = load_dataset(\"squad\")\n",
    "\n",
    "# Print information about the dataset\n",
    "print(dataset)\n",
    "\n",
    "# Access the first example in the training set\n",
    "print(\"\\nExample from the training set:\")\n",
    "print(dataset[\"train\"][0])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "72c83718",
   "metadata": {},
   "source": [
    "## Transcription with Hugging Face\n",
    "\n",
    "Audio transcription is the task of converting spoken language into text. Hugging Face also offers models for this task.\n",
    "\n",
    "Here's how you can use a pre-trained model for audio transcription:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "09fd8bd3",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Loading weights: 100%|██████████| 212/212 [00:00<00:00, 1101.77it/s, Materializing param=wav2vec2.feature_projection.projection.weight]                        \n",
      "\u001b[1mWav2Vec2ForCTC LOAD REPORT\u001b[0m from: facebook/wav2vec2-base-960h\n",
      "Key                        | Status  | \n",
      "---------------------------+---------+-\n",
      "wav2vec2.masked_spec_embed | MISSING | \n",
      "\n",
      "\u001b[3mNotes:\n",
      "- MISSING\u001b[3m\t:those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.\u001b[0m\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Transcription result:\n",
      "THE STALE SMELL OF OLD BEER LINGERS IT TAKES HEAT TO BRING OUT THE ODOR A COLD DIP RESTORES HEALTH AND ZEST A SALT PICKLE TASTES FINE WITH HAM TAKOS AL PASTORE ARE MY FAVORITE A ZESTFUL FOOD IS THE HOT CROSS BUN\n"
     ]
    }
   ],
   "source": [
    "from transformers import pipeline\n",
    "import soundfile as sf\n",
    "import torch\n",
    "\n",
    "# Load the automatic speech recognition pipeline\n",
    "transcriber = pipeline(\"automatic-speech-recognition\", model=\"facebook/wav2vec2-base-960h\")\n",
    "\n",
    "# Transcribe the audio file\n",
    "audio_file = \"harvard.wav\"\n",
    "try:\n",
    "    transcription = transcriber(audio_file)\n",
    "    print(\"Transcription result:\")\n",
    "    print(transcription['text'])\n",
    "except Exception as e:\n",
    "    print(f\"Error transcribing audio: \\n{e}\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8c6f0c10",
   "metadata": {},
   "source": [
    "## Summarization with Hugging Face\n",
    "\n",
    "Text summarization is the task of creating a shorter version of a text while preserving its main ideas. Hugging Face provides several models that can be used for this purpose.\n",
    "\n",
    "Here's how you can use a pre-trained model from Hugging Face for summarization:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "06cae513",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "No model was supplied, defaulted to distilbert/distilbert-base-uncased-finetuned-sst-2-english and revision 714eb0f.\n",
      "Using a pipeline without specifying a model name and revision in production is not recommended.\n",
      "Loading weights: 100%|██████████| 104/104 [00:00<00:00, 1285.06it/s, Materializing param=pre_classifier.weight]                                  \n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Original Text:\n",
      "\n",
      "Based on coalescence of Mitochondrial DNA and Y Chromosome data, it is thought that the earliest extant lineages of anatomically modern humans or Homo sapiens on the Indian subcontinent had reached there from Africa between 80,000 and 50,000 years ago\n",
      "\n",
      "\n",
      "Summary:\n",
      "NEGATIVE\n"
     ]
    }
   ],
   "source": [
    "from transformers import pipeline\n",
    "\n",
    "# Load the summarization pipeline\n",
    "summarizer = pipeline(\"text-classification\")\n",
    "\n",
    "# Text to summarize\n",
    "text = \"\"\"\n",
    "Based on coalescence of Mitochondrial DNA and Y Chromosome data, it is thought that the earliest extant lineages of anatomically modern humans or Homo sapiens on the Indian subcontinent had reached there from Africa between 80,000 and 50,000 years ago\n",
    "\"\"\"\n",
    "\n",
    "# Summarize the text\n",
    "summary = summarizer(text, max_length=100, min_length=30, do_sample=False)\n",
    "\n",
    "print(\"\\nOriginal Text:\")\n",
    "print(text)\n",
    "print(\"\\nSummary:\")\n",
    "print(summary[0]['label'])"
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
