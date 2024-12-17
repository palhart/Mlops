import os, sys
from PIL import Image, ImageDraw, ImageFont
from app.generator.design.helper import Helper
import os




class Image_Manager:
    def __init__(self):
        print("Image manager create")

    @staticmethod
    def add_text(
        base,
        text,
        position,
        font_size,
        text_color="black",
        wrapped_width=None,
        rotate_degrees=None,
    ):

        try:
            overlay_image = Image.new("RGBA", base.size, (0, 0, 0, 0))
            if wrapped_width is not None:
                text = Helper.wrap(text, wrapped_width)
            font_path = os.getenv("FONT_PATH")
            font = ImageFont.truetype(font_path, font_size)
            draw = ImageDraw.Draw(overlay_image)
            fill = (0, 0, 0, 255)
            if text_color == "white":
                fill = (255, 255, 255, 255)
            draw.text(position, text, font=font, fill=fill)
            if rotate_degrees is not None:
                overlay_image = overlay_image.rotate(rotate_degrees)

            return overlay_image
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"error: {e}")
            print(f"line: {exc_tb.tb_lineno}")
            print(f"file: {fname}")
            return "error"
