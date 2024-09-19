import os
import subprocess

def download_url(url, download_dir):
    try:
        command = ["yt-dlp", url, "-o", os.path.join(download_dir, "%(title)s.%(ext)s")]
        subprocess.run(command, check=True)
        print(f"Successfully downloaded: {url}")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading {url}: {e}")

def main(download_text, download_dir):
    os.makedirs(download_dir, exist_ok=True)
    try:
        with open(download_text, "r") as file:
            urls = file.readlines()
            for url in urls:
                url = url.strip()  
                if url: 
                    download_url(url, download_dir)
    except FileNotFoundError:
        print(f"The {download_text} file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_dir = "cooking2"
    download_text = "ToDownloadFromYouTube.txt"
    for _ in range(3):
        main(download_text, download_dir)