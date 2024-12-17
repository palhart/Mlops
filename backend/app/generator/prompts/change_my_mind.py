import datetime
from PIL import Image
from app.generator.design.image_manager import Image_Manager

import os


IMAGE_DIR =  "generated_images"

class Change_My_Mind():
    name = "Change_My_Mind"
    description = "This is the way it is in my opinion"

    def __init__(self):
        self.instruction = """
###
Message:Chocolate chip cookies are the best cookies. Try to change my mind.
Meme:{"opinion":" Chocolate chip cookies are the best cookies."}
###
Message:Learning to code is one of the most rewarding experiences. Change my mind.
Meme:{"opinion":"Learning to code is one of the most rewarding experiences."}
###
Message:Daft Punk is the greatest electronic band to ever exist and you can't convince me otherwise.
Meme:{"opinion":"Daft Punk is the greatest electronic band to ever exist. "}
###
Message:In my opinion, the best way to get a good grade in school is to study hard.
Meme:{"opinion":"The best way to get a good grade in school is to study hard. "}
###
"""

    def create(self, meme_text):

        with Image.open(f"app/static/meme_pics/{self.name.lower()}.jpg").convert(
            "RGBA"
        ) as base:

            overlay_image = Image_Manager.add_text(
                base=base,
                text=meme_text["opinion"],
                position=(500, 385),
                font_size=30,
                text_color="black",
                rotate_degrees=20,
                wrapped_width=22,
            )
            out = Image.alpha_composite(base, overlay_image)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                date = datetime.datetime.now()
                image_name = f"{date}.jpg"
                file_location = os.path.join(IMAGE_DIR, image_name)
                out.save(file_location)
                return image_name
