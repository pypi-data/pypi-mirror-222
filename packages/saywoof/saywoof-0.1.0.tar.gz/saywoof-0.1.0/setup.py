from setuptools import setup, find_packages

setup(
    name='saywoof',
    version='0.1.0',
    description='An easy to use wrapper for the BARK text-to-speech engine',
    author='Connor Etherington',
    author_email='connor@concise.cc',
    packages=find_packages(),
    install_requires=[
        "pyaudio",
        "numpy",
        "soundfile",
        "transformers",
        "saywoof",
        "colr",
        "argparse"
    ],
    entry_points={
        'console_scripts': [
            'saywoof=saywoof.main:main'
        ]
    }
)
