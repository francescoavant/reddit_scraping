import json
import requests
import os
import shutil
from pathlib import Path
from video import *

class Media:
    def media_down():
        with open('posts.json', 'r', encoding='utf8') as f:
            data = json.load(f)
            dir_photo_path="photo_dir"
            dir_video_path="video_dir"
            dir_html_path="html_dir"
            Path(dir_photo_path).mkdir(parents=True, exist_ok=True)
            Path(dir_video_path).mkdir(parents=True, exist_ok=True)
            Path(dir_html_path).mkdir(parents=True, exist_ok=True)
            
            for item in data:
                url = item["url"]
                if url.startswith("https://i"):
                    response = requests.get(url)
                    if response.status_code == 200:
                        filename = f"{item['id']}.jpg"
                        with open(filename, "wb") as f:
                            f.write(response.content)
                    else:
                        print(f"Failed to download image {item['id']}.jpg. Status code: {response.status_code}")
            c=0
            for item in data:
                    url = item["url"]
                    file_path= get_html_from_url(url,c)
                    source_link = extract_source_link_from_html_file(file_path)
                    #if source_link:
                        #print(source_link)
                    download_video(source_link,c)
                    #nomefile="video"+str(c)+".mp4"
                    #wait for download before moving
                    # if not os.path.exists(os.path.join(dir_video_path,nomefile)):
                    #     shutil.move(nomefile, dir_video_path)    
                    #     print(f"Video downloaded and moved successfully."
                    c+=1
                    
    #forall jpg files, move them to photo_dir
        for filename in os.listdir():
            if filename.endswith(".jpg"):
                if not os.path.exists(os.path.join(dir_photo_path,filename)):
                    shutil.move(filename, dir_photo_path)    
                    print(f"Image {filename} moved successfully.")
                else:
                    print(f"Image {filename} already exists in {dir_photo_path}")

    #forall html.txt files, move them to html_dir
        for filename in os.listdir():
            if filename.endswith(".txt"):
                if not os.path.exists(os.path.join(dir_html_path,filename)):
                    shutil.move(filename, dir_html_path)    
                    print(f"HTML file {filename} moved successfully.")
                else:
                    print(f"HTML file {filename} already exists in {dir_html_path}")

    #forall video.mp4 files, move them to video_dir
        for filename in os.listdir():
            if filename.endswith(".mp4"):
                if not os.path.exists(os.path.join(dir_video_path,filename)):
                    shutil.move(filename, dir_video_path)    
                    print(f"Video {filename} moved successfully.")
                else:
                    print(f"Video {filename} already exists in {dir_video_path}")
    

#Media.image_down()
