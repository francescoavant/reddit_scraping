import subprocess
import requests
import re
import time

#extract the html from the url and save it to a file if it contains a video
def get_html_from_url(url, c):
    response = requests.get(url)
    filename = "html" + str(c) + ".txt"
    pattern = r'<source\s+src="(https://v.redd.it/[^"]+)"'
    match = re.search(pattern, response.text)
    if match:
        with open(filename, 'w', encoding='utf8') as f:
            f.write(response.text)
            return filename
    else:
        return None

#extract the source link from the html file if it contains a video
def extract_source_link_from_html_file(file_path):
    if file_path is not None:
        try:
            #delay before accessing the file
            time.sleep(6)
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
            # Use regex to find the source link contains the video
            pattern = r'<source\s+src="(https://v.redd.it/[^"]+)"'
            match = re.search(pattern, file_content)

            if match:
                source_link = match.group(1)
                return source_link
            else:
                return None
        except FileNotFoundError:
            return None

#download the video from the source link (HLS format) and merge it with the audio with ffmpeg commands
def download_video(url,c):
    try:
        command = f"youtube-dl -o video{c}.mp4 {url}"
        subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        print("Video downloaded successfully as 'video.mp4'.")
        merge_command = "ffmpeg -i video.mp4 -i audio.mp3 -c:v copy -c:a aac output.mp4"
        subprocess.run(merge_command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        pass


