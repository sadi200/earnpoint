#!/bin/bash

# Update and install necessary packages
sudo apt update && sudo apt upgrade -y
sudo apt install git screen python3 python3-pip python3-venv -y

# Clone the earnpoint repository
git clone https://github.com/sadi200/earnpoint.git
cd earnpoint

# Set up Python virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required Python package
pip install requests

# Start a screen session
screen -S hyperbolic
