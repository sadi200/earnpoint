#!/bin/bash

# ANSI color codes for red and yellow
RED="\033[91m"
YELLOW="\033[93m"
RESET="\033[0m"

# Banner function
print_banner() {
    echo -e "${RED}███████╗ █████╗ ██████╗ ███╗   ██╗${RESET}"
    echo -e "${YELLOW}██╔════╝██╔══██╗██╔══██╗████╗  ██║${RESET}"
    echo -e "${RED}███████╗███████║██████╔╝██╔██╗ ██║${RESET}"
    echo -e "${YELLOW}╚════██║██╔══██║██╔═══╝ ██║╚██╗██║${RESET}"
    echo -e "${RED}███████║██║  ██║██║     ██║ ╚████║${RESET}"
    echo -e "${YELLOW}╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═══╝${RESET}"
    echo -e "${RED}      💰 EARN${RESET} & ${YELLOW}POINTS 💎${RESET}\n"
}

# Run the banner
print_banner

# Update and install necessary packages
sudo apt update && sudo apt upgrade -y
sudo apt install git screen python3 python3-pip python3-venv -y

# Clone the earnpoint repository
git clone https://github.com/sadi200/earnpoint.git
cd earnpoint || exit

# Set up Python virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required Python package
pip install requests

# Start a screen session
screen -S hyperbolic
