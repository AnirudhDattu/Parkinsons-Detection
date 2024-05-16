import os
import requests
from flask import Flask, request, redirect, render_template, url_for
from werkzeug.utils import secure_filename
from process_image import process_image
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.config["IMAGE_UPLOADS"] = r"D:\SEM - 4\ML\project-final\Hand written\static\img"

@app.route("/", methods=["GET", "POST"])
def upload_image():
   if request.method == "POST":
      if request.files:
         image = request.files["image"]

         image_url = os.path.join(app.config["IMAGE_UPLOADS"], image.filename)

         image.save(image_url)

         print("Image saved")

         result = process_image(image_url)

         print(result)

         image_path = "static/img/" + image.filename
         return render_template("result.html", result=result, image_path=image_path)
   
   return render_template("index.html")


DOWNLOAD_DIRECTORY = r"D:\SEM - 4\ML\project-final\Hand written\static\uploaded images"




if __name__ == '__main__':
    app.run(debug=True)


