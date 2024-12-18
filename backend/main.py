from fastapi.responses import FileResponse

from app.generator.generate_meme import generate_meme
from fastapi import Depends, FastAPI, HTTPException, Header
from pydantic import BaseModel
from dotenv import load_dotenv
import os


app = FastAPI()

load_dotenv()

project_root = os.path.abspath(os.path.dirname(__file__))


IMAGE_DIR =  os.path.join(project_root, "generated_images")

API_TOKEN = os.getenv("API_TOKEN")

class MemeRequest(BaseModel):
    user_input: str

# Dependency to validate token
def validate_token(x_token: str = Header(...)):
    if x_token.strip() != API_TOKEN.strip():
        raise HTTPException(status_code=401, detail="Invalid or missing token")


@app.get("/")
@app.get("/home")
def read_root():
    image_name = "default2.jpg"

    file_path = os.path.join(IMAGE_DIR, image_name)
    print(file_path)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    raise HTTPException(status_code=404, detail="Image non trouvée")



@app.get("/generated_images/{image_name}")
def get_image(image_name: str):
    file_path = os.path.join(IMAGE_DIR, image_name)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    raise HTTPException(status_code=404, detail="Image non trouvée")

@app.post("/generate_meme")
def generate_meme_endpoint(meme_request: MemeRequest, x_token: str = Depends(validate_token)):
    try:
        print(meme_request)
        user_input = meme_request.user_input
        meme = generate_meme(user_input=user_input)
        return meme
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Failed to generate meme")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=27010)




    



            