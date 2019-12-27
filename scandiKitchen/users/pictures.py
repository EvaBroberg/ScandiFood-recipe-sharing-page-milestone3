import os
from PIL import Image
from flask import url_for,current_app


def add_profile_pic(pic_upload,username):
    filename = pic_upload.filename
    #taking the text after . to check that extention is jpg or png
    ext_type = filename.split('.')[-1]
    #changing user's picture name to username and adding existing extention in order not to have repeating file names
    storage_filename = str(username)+'.'+ext_type
    #finding path to a folder where profile pictures will be stored 
    filepath = os.path.join(current_app.root_path,'static/profile_pictures',storage_filename)


    #setting file size
    output_size = (200,200)
    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)

    return storage_filename
