#make sure ur in cmd not powershell
#cd C:\Users\aleks\dev\python_projects\SKORPZ\skorpzbot
#-m venv SkorpzEnv
#SkorpzEnv\Scripts\Activate


import os
import requests

def download_image(url, folder):
    try:
        response = requests.get(url)
        response.raise_for_status()
        filename = os.path.join(folder, url.split("/")[-1])
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {url} to {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")

def main():
    folder = "downloaded_images"
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    while True:
        url = input("Enter image URL (or 'exit' to quit): ")
        if url.lower() == 'exit':
            break
        download_image(url, folder)

if __name__ == "__main__":
    main()
