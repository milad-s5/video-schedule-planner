#!/bin/bash

# Check if running from the correct directory
if [ ! -f "main.py" ]; then
    echo "Error: Please run this script from the project root directory"
    exit 1
fi

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python 3 using your package manager:"
    echo "  Ubuntu/Debian: sudo apt-get install python3"
    echo "  Fedora: sudo dnf install python3"
    echo "  Arch Linux: sudo pacman -S python"
    exit 1
fi

# Check if Python development package is installed
if [ ! -f "/usr/lib/python3.8/config-3.8-x86_64-linux-gnu/libpython3.8.so" ] && \
   [ ! -f "/usr/lib/x86_64-linux-gnu/libpython3.8.so" ]; then
    echo "Error: Python development package is not installed"
    echo "Please install it using your package manager:"
    echo "  Ubuntu/Debian: sudo apt-get install python3.8-dev"
    echo "  Fedora: sudo dnf install python3-devel"
    echo "  Arch Linux: sudo pacman -S python-pip"
    exit 1
fi

# Check if MediaInfo is installed
if ! command -v mediainfo &> /dev/null; then
    echo "Error: MediaInfo is not installed"
    echo "Please install MediaInfo using your package manager:"
    echo "  Ubuntu/Debian: sudo apt-get install mediainfo"
    echo "  Fedora: sudo dnf install mediainfo"
    echo "  Arch Linux: sudo pacman -S mediainfo"
    exit 1
fi

# Check if tkinter is installed
if ! python3 -c "import tkinter" &> /dev/null; then
    echo "Error: tkinter is not installed"
    echo "Please install tkinter using your package manager:"
    echo "  Ubuntu/Debian: sudo apt-get install python3-tk"
    echo "  Fedora: sudo dnf install python3-tkinter"
    echo "  Arch Linux: sudo pacman -S tk"
    exit 1
fi

# Install Python dependencies if needed
if [ ! -d "venv" ]; then
    echo "Setting up Python virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
else
    source venv/bin/activate
fi

# Function to build the executable
build_executable() {
    echo "Building executable..."
    python build.py
    if [ $? -eq 0 ]; then
        echo "Build successful! Executable created in the 'dist' directory."
        chmod +x dist/video-schedule-planner
        echo "You can now run the application using: ./dist/video-schedule-planner"
    else
        echo "Build failed. Please check the error messages above."
        exit 1
    fi
}

# Check if we're being asked to build
if [ "$1" = "build" ]; then
    build_executable
    exit 0
fi

# Run the application
python3 main.py 