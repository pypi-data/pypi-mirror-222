import argparse
import sys

parser = argparse.ArgumentParser(description='A wrapper for the BARK text-to-speech engine')
parser.add_argument("-l", "--local", help="Load local model", action="store_true")
parser.add_argument("-L", "--large", help="Load large model (Uses more vram)", action="store_true")
parser.add_argument("-s", "--save", help="Save model", action="store_true")
parser.add_argument("-t", "--text", help="Text to convert to speech")
parser.add_argument("-f", "--file", help="File to convert to speech")
parser.add_argument("-o", "--output", help="Output file name (default: output.wav)")
parser.add_argument("-r", "--rate", help="Sample rate of output file (default: 22050)", type=int)
parser.add_argument("-p", "--persistent", help="Persistent mode (Keep running after conversions to save time)", action="store_true")

args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)
