import datetime
from PIL import Image
from app.generator.design.image_manager import Image_Manager
import os
import shortuuid

IMAGE_GEN =  "Mlops/backend/generated_images"
IMAGE_STATIC = "Mlops/backend/app/static/meme_pics"

class Missing_Something():
    name = "Missing_Something"
    description = "something is missing and I wish it was still here"

    def __init__(self):
        self.instruction = """
###
Message:I miss going for long by the beach
Meme:{"missing": "long runs by the beach"}
###
Message:I wish there was a new season of The Office
Meme:{"missing": "a new season of The Office"}
###
Message:I love the smell of a new car
Meme:{"missing": "The smell of a brand new car"}
###
"""

    def create(self, meme_text):
        with Image.open(f"{IMAGE_STATIC}/{self.name.lower()}.jpg").convert(
            "RGBA"
        ) as base:

            overlay_image = Image_Manager.add_text(
                base=base,
                text=meme_text["missing"],
                position=(1150, 550),
                font_size=50,
                wrapped_width=12,
            )
            out = Image.alpha_composite(base, overlay_image)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")

                date = shortuuid.uuid()
                image_name = f"{date}.jpg"
                file_location = os.path.join(IMAGE_GEN, image_name)
                out.save(file_location)
                return image_name
