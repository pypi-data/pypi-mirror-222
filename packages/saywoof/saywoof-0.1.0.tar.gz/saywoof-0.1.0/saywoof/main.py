import time
import pyaudio
import numpy as np
import soundfile as sf
from transformers import AutoProcessor, AutoModel, AutoTokenizer
from saywoof import args
from colr import color
import argparse
import os
import sys

save_path = None, None

blue_1 = '#67D0A8'
red_1 = '#FF6B6B'

def pr(text: str, hex_color: str = None):

    if not hex_color:
        hex_color = blue_1

    print(color(text, fore=hex_color))


def load_model():
    save_path = "./Models/bark-small"
    os.environ["SUNO_OFFLOAD_CPU"] = "True"
    os.environ["SUNO_USE_SMALL_MODELS"] = "True"

    pr("\nLoading Processor...\n")
    processor = AutoProcessor.from_pretrained("suno/bark-small")

    pr("\nLoading Model...\n")
    model = AutoModel.from_pretrained("suno/bark-small")

    pr("\nLoading Tokenizer...\n")
    tokenizer = AutoTokenizer.from_pretrained("suno/bark-small")

    return processor, model, tokenizer, save_path


def load_large():
    save_path = "./Models/bark"

    pr("\nLoading Processor...\n")
    processor = AutoProcessor.from_pretrained("suno/bark")

    pr("\nLoading Model...\n")
    model = AutoModel.from_pretrained("suno/bark")

    pr("\nLoading Tokenizer...\n")
    tokenizer = AutoTokenizer.from_pretrained("suno/bark")

    return processor, model, tokenizer, save_path


def load_local():
    os.environ["SUNO_OFFLOAD_CPU"] = "True"
    os.environ["SUNO_USE_SMALL_MODELS"] = "True"

    if args.large:
        if not os.path.exists("./Models/bark"):
            pr("\nBark model not found, please download it first (run without '-l' flag)\n", red_1)
            sys.exit(1)
        else:
            pr("\nLoading Processor...\n")
            processor = AutoProcessor.from_pretrained("./Models/bark")

            pr("\nLoading Model...\n")
            model = AutoModel.from_pretrained("./Models/bark")

            pr("\nLoading Tokenizer...\n")
            tokenizer = AutoTokenizer.from_pretrained("./Models/bark")

    else:
        if not os.path.exists("./Models/bark-small"):
            pr("\nBark-small model not found, please download it first (run without '-l' flag)\n", red_1)
            sys.exit(1)
        else:
            pr("\nLoading Processor...\n")
            processor = AutoProcessor.from_pretrained("./Models/bark-small")

            pr("\nLoading Model...\n")
            model = AutoModel.from_pretrained("./Models/bark-small")

            pr("\nLoading Tokenizer...\n")
            tokenizer = AutoTokenizer.from_pretrained("./Models/bark-small")

    return processor, model, tokenizer


def save_model(processor, model, tokenizer, save_path):

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    pr("\nSaving Processor...\n")
    processor.save_pretrained(save_path)

    pr("\nSaving Model...\n")
    model.save_pretrained(save_path)

    pr("\nSaving Tokenizer...\n")
    tokenizer.save_pretrained(save_path)


def text_to_speech(processor, model, tokenizer, text):

    voice_preset = "v2/en_speaker_9"

    inputs = processor(
        text=[text],
        return_tensors="pt",
        voice_preset=voice_preset
    )

    # speech_values = model.generate(**inputs, do_sample=True)
    audio_array = model.generate(**inputs)
    audio_array = audio_array.cpu().numpy().squeeze()

    return audio_array


def write(filename, sample_rate, audio_array):
    sf.write(filename, audio_array, sample_rate)


def main():

    if args.rate:
        rate = int(args.rate)
    else:
        rate = 22050

    if args.local:
        processor, model, tokenizer = load_local()
    elif args.large:
        processor, model, tokenizer, save_path = load_large()
    else:
        processor, model, tokenizer, save_path = load_model()

    if args.save:
        if not args.local:
            save_model(processor, model, tokenizer, save_path)
        else:
            print("Local model is already saved, Its local...")
        sys.exit(0)

    if args.persistent:
        persistent(rate, processor, model, tokenizer)
        sys.exit(0)

    if not args.text and not args.file:
        print("No input text or file specified")
        sys.exit(1)
    elif args.text and args.file:
        print("Both text and file specified")
        sys.exit(1)

    elif args.text:
        speech = text_to_speech(processor, model, tokenizer, args.text)
        if args.output:
            output_file = args.output
        else:
            output_file = "output.wav"

        write(output_file, rate, speech)

    elif args.file:
        speech = text_to_speech(processor, model, tokenizer, args.file)
        if args.output:
            output_file = args.output
        else:
            output_file = "output.wav"

        write(output_file, 18000, speech)


def persistent(rate, processor, model, tokenizer):

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=rate, output=True)

    while True:
        text = input("Enter text: ")
        speech = text_to_speech(processor, model, tokenizer, text)
        stream.write(speech.astype(np.float32).tobytes())

    stream.stop_stream()
    stream.close()
    p.terminate()


if __name__ == "__main__":
    main()
