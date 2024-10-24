#!/bin/bash

# Config git hub
name="$1"
email="$2"
if [ -z "$name" ] || [ -z "$email" ]; then
    echo "Usage: ./initialize.sh <your_name> <your_email>"
    exit 1
fi

git config --global user.name "$name"
git config --global user.email "$email"

# Use conda to create environment and automatically activate it
conda env create -f environment.yml
conda activate myenv