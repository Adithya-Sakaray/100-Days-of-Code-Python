import shutil
from flask import Flask, render_template, request, url_for, redirect
from color_handler import extract_dominant_colors
import os

app = Flask(__name__)


@app.route('/')
def home():
    folder_path = "static/images"  # Adjust the path as needed

    # Check if the folder exists
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        # List all files in the folder
        files = os.listdir(folder_path)

        # Loop through the files and delete them
        for file in files:
            file_path = os.path.join(folder_path, file)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    # If the file is a directory, you can use shutil.rmtree for recursive deletion
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

        print(f"All files in '{folder_path}' have been deleted.")
    else:
        print(f"'{folder_path}' does not exist or is not a directory.")

    return render_template("home.html")


@app.route("/result", methods=["POST", "GET"])
def result():
    uploaded_file = request.files['file']

    if uploaded_file:
        path = f"static/images/{uploaded_file.filename}"
        uploaded_file.save(path)
        hex_color_list = extract_dominant_colors(image_path_local=path)

        # os.remove(uploaded_file.filename)

        return render_template("result.html", color_list=hex_color_list, image_path=path)

    return redirect(url_for("error"))


@app.route("/error")
def error():
    return render_template("error.html")


if __name__ == '__main__':
    app.run()
