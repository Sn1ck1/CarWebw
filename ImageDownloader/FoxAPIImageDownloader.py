import os
import json
import requests

# The url of the API endpoint
url = "https://randomfox.ca/floof/"

# The directory where you want to save the images
save_directory = "images"

# Create the save directory if it doesn't exist
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# Number of images you want to download
num_images = 20

for i in range(num_images):
    # Make a GET request to the API
    response = requests.get(url)
    # Parse the JSON response
    data = json.loads(response.text)
    # Get the image URL
    image_url = data['image']

    try:
        # Get image data
        image_data = requests.get(image_url, stream=True)
        image_data.raise_for_status()

        # Get image file name from URL
        file_name = image_url.split("/")[-1]
        # if the filename not contain any extension, then you should give the extension,
        # otherwise the image will be corrupted
        if '.' not in file_name:
            file_name = file_name + '.jpg'

        # Save image to directory
        with open(os.path.join(save_directory, file_name), "wb") as f:
            for chunk in image_data.iter_content(1024):
                f.write(chunk)
        print(f"Image {file_name} downloaded and saved to {save_directory}")
    except requests.exceptions.HTTPError as errh:
        print ("HTTP Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("Something went wrong: ",err)


'''Here's a Python program that automatically downloads multiple images from the API at https://randomfox.ca/floof/ 
and saves them to a directory. It should be compatible with all image types.'''