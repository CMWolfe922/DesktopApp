import os
import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")

def complete_text(
    model:str = "text-davinci-003", 
    prompt:str = "", 
    max_tokens:int = 256,
    top_p:int = 1,
    frequency_penalty:int = 0,
    presence_penalty:int = 0
    )
    
    """The prompt is the most important input."""

    response = openai.Completion.create(
      model="text-davinci-003",
      prompt="",
      temperature=0.7,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    print(response)
    return response


def generate_image(prompt:str, size:str = "500x500", num:int = 1):

    response = openai.Image.create(
      prompt=prompt,
      n=num,
      size=size
    )
    image_url = response['data'][0]['url']
    print(image_url)
    return image_url
