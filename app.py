import cv2
import numpy as np
from flask import Flask, render_template, request, jsonify
import imutils
from flask import send_file

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/parking_lot.jpg')
def get_parking_lot_image():
    print("shubham")
    filename = 'parking_lot.jpg'
    return send_file(filename, mimetype='image/jpg')


# @app.route('/detect_parking', methods=['POST'])
# def detect_parking():
#     # Get the image file from the request
#     file = request.files['image']
#     # file = 'parking_lot.jpg'
#     print("shubham---++++", file)
#     # Read the image file and convert it to grayscale
#     image = cv2.imdecode(np.fromstring(
#         file.read(), np.uint8), cv2.IMREAD_COLOR)
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Apply thresholding to the grayscale image
#     thresh = cv2.threshold(
#         gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

#     # Find contours in the thresholded image
#     contours = cv2.findContours(
#         thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     contours = imutils.grab_contours(contours)

#     # Count the number of contours
#     num_contours = len(contours)

#     # Return the number of parking spots
#     return jsonify(num_parking_spots=num_contours)

@app.route('/detect_parking')
def detect_parking():
    # Read the image file and convert it to grayscale
    print("ohm namah shivay")
    image = cv2.imread('parking_lot.jpg')
    # print("@@", image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # print("@@", gray)

    # Apply thresholding to the grayscale image
    thresh = cv2.threshold(
        gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # print("@@", thresh)
    # Find contours in the thresholded image
    contours = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    # print("@@", contours)
    # Count the number of contours
    num_contours = len(contours)

    # print("@@", num_contours)
    # Return the number of parking spots
    return jsonify(num_parking_spots=num_contours)


if __name__ == '__main__':
    app.run(debug=True)
