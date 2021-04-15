# -----------------------------------------
# Author: Leonardo Villalobos
# Date: 4/14/2021
# Description: A webpage which displays
# three random images from a given image
# metadata structure using Flask, Bootstrap,
# and Pillow.
# -----------------------------------------
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from PIL import Image
import image_info
import random as rand

app = Flask(__name__)
bootstrap = Bootstrap(app)
data = image_info.image_info


def access_image_data(index: int) -> dict:
    """
    Returns the attributes of an image at the given 'index'.

    *index: int -- an image index, bound by 0 ≤ index ≤ 9.
    """
    return {
        'id': data[index]['id'], 'title': data[index]['title'],
        'credit': data[index]['flickr_user']
    }


def get_image_attributes(image, index: int, html_file: str) -> dict:
    """
    Returns a dictionary with the attributes of the image at position
    'index'.

    *image -- the argument passed into the webpage function and decorator.
    *index: int -- an image index, bound by 0 ≤ index ≤ 9.
    *html_file: str -- the HTML file which the webpage function will access.
    """
    filename = access_image_data(index)['id']
    with Image.open(f'static/images/{filename}.jpg') as this_im:
        return {
            'file': html_file,
            'attr': access_image_data(index),
            'image': image,
            'format': this_im.format,
            'mode': this_im.mode,
            'width': this_im.size[0],
            'height': this_im.size[1]
        }


@app.route('/')
def home_page() -> render_template:
    """
    Returns a 'render_template' object which will construct the
    main page on the website.
    """
    rand.shuffle(data)
    # The first three images in 'data' are used since the images
    # will shuffle each time the webpage reloads.
    return render_template(
        'index.html',
        img1=access_image_data(0),
        img2=access_image_data(1),
        img3=access_image_data(2),
    )


@app.route('/picture/<id>')
def display_images(id) -> render_template:
    image_1 = get_image_attributes(id, 0, 'first_image.html')
    image_2 = get_image_attributes(id, 1, 'second_image.html')
    image_3 = get_image_attributes(id, 2, 'third_image.html')
    if id == image_1['attr']['id']:
        return render_template(
            image_1['file'],
            attr=image_1['attr'],
            id=image_1['image'],
            format=image_1['format'],
            mode=image_1['mode'],
            width=image_1['width'],
            height=image_1['height']
        )
    elif id == image_2['attr']['id']:
        return render_template(
            image_2['file'],
            attr=image_2['attr'],
            id=image_2['image'],
            format=image_2['format'],
            mode=image_2['mode'],
            width=image_2['width'],
            height=image_2['height']
        )
    else:
        return render_template(
            image_3['file'],
            attr=image_3['attr'],
            id=image_3['image'],
            format=image_3['format'],
            mode=image_3['mode'],
            width=image_3['width'],
            height=image_3['height']
        )
