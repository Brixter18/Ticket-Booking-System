import subprocess
import sys

def install_requirements(file_path='requirements.txt'):
    try:
        with open(file_path, 'r') as f:
            packages = f.read().splitlines()
        
        for package in packages:
            if package.strip() and not package.startswith('#'):
                print(f"Installing {package}...")
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        print("All packages installed successfully!")
    except FileNotFoundError:
        print(f"{file_path} not found.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install package: {e}")

if __name__ == "__main__":
    install_requirements()
