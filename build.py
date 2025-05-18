import os
import platform
import subprocess
import shutil

def build_executable():
    # Clean up previous builds
    if os.path.exists('dist'):
        shutil.rmtree('dist')
    if os.path.exists('build'):
        shutil.rmtree('build')
    
    # Get the platform-specific executable name
    system = platform.system().lower()
    exe_name = 'video-schedule-planner'
    if system == 'windows':
        exe_name += '.exe'
    
    # Build command
    cmd = [
        'pyinstaller',
        '--name', exe_name,
        '--onefile',  # Create a single executable
        '--windowed',  # Don't show console window
        '--add-data', f'README.md{os.pathsep}.',  # Include README
        '--icon', 'icon.ico' if system == 'windows' else 'icon.png',  # Platform-specific icon
        'main.py'
    ]
    
    # Run PyInstaller
    subprocess.run(cmd)
    
    print(f"\nBuild completed! Executable can be found in the 'dist' directory.")
    print(f"To run the application, simply double-click the executable in the 'dist' folder.")

if __name__ == '__main__':
    build_executable() 