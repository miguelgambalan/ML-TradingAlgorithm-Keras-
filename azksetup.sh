#!/bin/bash

VENV_NAME=AZK_1ENV

# Create a virtual environment using Python 3.9
python3.9.6 -m venv $VENV_NAME

# Activate the virtual environment
source $VENV_NAME/bin/activate

# Upgrade pip to the latest version
pip install --upgrade pip setuptools wheel

# Install specific versions of the libraries for Python 3.9 compatibility
pip install numpy==1.21 pandas==1.3.3 requests matplotlib==3.4.3 seaborn scikit-learn==1.0.2 tensorflow==2.10.0

# Deactivate the virtual environment
deactivate

echo "Virtual environment '$VENV_NAME' has been created and required libraries have been installed."
