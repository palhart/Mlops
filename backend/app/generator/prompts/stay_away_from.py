import datetime
from PIL import Image
from app.generator.design.image_manager import Image_Manager
import os
import shortuuid

IMAGE_GEN =  "Mlops/backend/generated_images"
IMAGE_STATIC = "Mlops/backend/app/static/meme_pics"

class Stay_Away_From():
    name = "Stay_Away_From"
    description = "stay away from"

    def __init__(self):
        self.instruction = """
###
Message:I typically prefer to stay away from people who are not my friends.
Meme:{"subject":"who are not my friends."}
###
Message:I don't hang out with Tiktokers
Meme:{"subject":"Tiktokers"}
###
"""

    def create(self, meme_text):
        with Image.open(f"{IMAGE_STATIC}/{self.name.lower()}.jpg").convert(
            "RGBA"
        ) as base:

            overlay_image = Image_Manager.add_text(
                base=base,
                text=meme_text["subject"],
                position=(115, 300),
                font_size=30,
                wrapped_width=15,
            )
            out = Image.alpha_composite(base, overlay_image)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                date = shortuuid.uuid()
                image_name = f"{date}.jpg"
                file_location = os.path.join(IMAGE_GEN, image_name)
                out.save(file_location)
                return image_name
