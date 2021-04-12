# -----------------------------------------
# Author: Leonardo Villalobos
# Date: 4/12/2021
# Instructor: Professor Avner Biblarz
# Course: CST-205
# Description: TODO: set description
# -----------------------------------------
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from PIL import Image
import image_info
import random as rand

app = Flask(__name__)
bootstrap = Bootstrap(app)
data = image_info.image_info


def get_image_attr(index: int) -> dict:
    """
    Returns the attributes of an image at the given 'index'.

    *index: int -- an image index, bound by 0 ≤ index ≤ 9.
    """
    return {
        'id': data[index]['id'], 'title': data[index]['title'],
        'credit': data[index]['flickr_user']
    }


def get_img_template_values(image, index: int, html_file: str) -> render_template:
    """
    Returns a 'render_template' object with the attribute parameters
    of the image at position 'index' within 'data'.

    *image -- the argument passed into the webpage function and decorator.
    *index: int -- an image index, bound by 0 ≤ index ≤ 9.
    *html_file: str -- the HTML file which the webpage function will open.
    """
    filename = get_image_attr(index)['id']
    with Image.open(f'static/images/{filename}.jpg') as this_im:
        return render_template(
            html_file,
            img=get_image_attr(index),
            image=image,
            format=this_im.format,
            mode=this_im.mode,
            width=this_im.size[0],
            height=this_im.size[1]
        )


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
        img1=get_image_attr(0),
        img2=get_image_attr(1),
        img3=get_image_attr(2)
    )


@app.route('/picture/<image>')
def first_image(image):
    return get_img_template_values(image, 0, 'first_image.html')
