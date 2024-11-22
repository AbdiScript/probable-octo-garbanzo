import pytesseract
from PIL import Image
import requests
from io import BytesIO
import re

def contains_english_letters(image_url):
    try:
        # Fetch the image from the URL
        response = requests.get(image_url)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content))
        
        # Perform OCR using pytesseract
        extracted_text = pytesseract.image_to_string(image)
        
        # Check for English letters in the extracted text
        contains_letters = bool(re.search(r'[A-Za-z]', extracted_text))
        
        print(contains_letters)  # Boolean result
        return contains_letters
    except Exception as e:
        print(f"Error: {e}")
        return False

# Example usage:
image_url = "https://dkstatics-public.digikala.com/digikala-products/319f22d08c9494efbc88a4756de3de3ded4d6f65_1731925489.jpg"
contains_english_letters(image_url)
