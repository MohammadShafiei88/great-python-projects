import os
import requests

def get_extensions(image_url: str) -> str:
    extensions: list[str] = [".png", ".jpg", ".jpeg", ".gif", ".svg"]
    for ext in extensions:
        if ext in image_url:
            return ext


def download_image(image_url: str, image_name: str, folder: str = None):
    if ext:= get_extensions(image_url):
        if folder:
            image_name: str=f'{folder}/{image_name}{ext}'
        else:
            image_name: str=f'{image_name}{ext}'

    else:
        raise Exception('Image extension could not be located...')

    if os.path.isfile(image_name):
        raise Exception('File name already exists...')

    try:
        image_content: bytes = requests.get(image_url).content
        with open(image_name, 'wb') as handler:
            handler.write(image_content)
            print(f'Downloaded: "{image_name}" successfully!')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    input_url: str = input('Enter a url: ')
    input_name: str = input('What would you like to name it?: ')
    print('Downloading...')
    download_image(input_url, input_name, folder='images')





