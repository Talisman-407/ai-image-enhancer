from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import Response, JSONResponse
from rembg import remove
from PIL import Image
import io
import logging

logging.basicConfig(level=logging.INFO)

router = APIRouter()

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

@router.post("/background/remove")
async def remove_background(image: UploadFile = File(...), mode: str = Form("rembg")):
    try:
        image_data = await image.read()
        output_data = remove(image_data)
        # if mode == "ai":
        #     Use custom AI model (placeholder logic)
        #     output_data = custom_ai_background_removal(image_data)
        return Response(content=output_data, media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image: {e}")

@router.post("/background/generate")
async def generate_background(image: UploadFile = File(...), color: str = Form("#FFFFFF")):
    logging.info(f"Received color: {color}")
    try:
        rgb_color = hex_to_rgb(color)
        image_data = await image.read()
        image = Image.open(io.BytesIO(image_data))
        output_data = remove(image_data)
        foreground = Image.open(io.BytesIO(output_data)).convert("RGBA")

        # Create a new image with the specified background color
        background = Image.new("RGBA", foreground.size, rgb_color + (255,))

        # Composite the foreground onto the background
        composite = Image.alpha_composite(background, foreground)

        # Save the result to a byte stream
        byte_arr = io.BytesIO()
        composite.save(byte_arr, format="PNG")

        # Return the image directly
        return Response(content=byte_arr.getvalue(), media_type="image/png")
        #     content={
        #         "message": "Background generated successfully",
        #         "image": byte_arr.decode("latin1"),
        #     }
        # )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
