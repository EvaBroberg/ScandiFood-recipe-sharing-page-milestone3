import os
from PIL import Image
from flask import url_for,current_app


def add_recipe_pic(recipe_pic_upload):
    recipe_filename = recipe_pic_upload.filename
    recipe_ext_type = recipe_filename.split('.')[-1]
    recipe_filepath = os.path.join(current_app.root_path,'static/recipe_pics',storage_filename)


    #setting file size
    recipe_output_size = (200,200)
    pic = Image.open(recipe_pic_upload)
    pic.thumbnail(recipe_output_size)
    pic.save(recipe_filepath)

    return recipe_storage_filename


    