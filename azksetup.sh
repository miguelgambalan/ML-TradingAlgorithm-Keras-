#!/bin/bash

# Define the name of the virtual environment
VENV_NAME=AZK_1ENV

# Create a new virtual environment
python3 -m venv $VENV_NAME

# Activate the virtual environment
source $VENV_NAME/bin/activate

# Upgrade pip to the latest version
pip install --upgrade pip

# Install the required libraries
pip install numpy pandas requests matplotlib seaborn scikit-learn tensorflow keras

# Deactivate the virtual environment
deactivate

echo "Virtual environment '$VENV_NAME' has been created and required libraries have been installed."
