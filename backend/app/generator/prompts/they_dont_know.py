import datetime
from PIL import Image
from app.generator.design.image_manager import Image_Manager
import os

IMAGE_DIR =  "generated_images"


class They_Dont_Know():
    name = "They_Dont_Know"
    description = "they don't know"

    def __init__(self):
        self.instruction = """
###
Message:I am so proud of my new website that sells dog treats
Meme:{"details":"They don't know I have a new website that sells dog treats"} 
###
Message:They don't know I started a company
Meme:{"details":"They don't know I started a company"} 
###
Message:Everyone would be impressed that I can run a marathon
Meme:{"details":"They don't know I can run a marathon"} 
###
Message:No one cares that I am getting married this month
Meme:{"details":"They don't know that I am getting married this month"} 
###
Message:They don't know that I have a lot of followers on Twitter
Meme:{"details":"They don't know that I have a lot of followers on Twitter"} 
###
Message:We don't care that you have a masters in computer science
Meme:{"details":"They don't know that I have a masters in computer science"} 
###
Message:People think it's so important that they can do social media marketing
Meme:{"details":"They don't know that I can do social media marketing"} 
###
Message:I don't know if you guys realized I can an write an App in ReactJS while also using the Django framework on the backend
Meme:{"details":"They don't know that I can an write an App in ReactJS while also using the Django framework on the backend"}
###
"""

    def create(self, meme_text):
        with Image.open(f"app/static/meme_pics/{self.name.lower()}.jpg").convert(
            "RGBA"
        ) as base:

            overlay_image = Image_Manager.add_text(
                base=base,
                text=meme_text["details"],
                position=(400, 100),
                font_size=40,
                wrapped_width=15,
            )
            out = Image.alpha_composite(base, overlay_image)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                date = datetime.datetime.now()
                image_name = f"{date}.jpg"
                file_location = os.path.join(IMAGE_DIR, image_name)
                out.save(file_location)
                return image_name
