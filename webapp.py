from contextlib import _RedirectStream, redirect_stderr
from flask import Flask, render_template, request
from image_processing import preprocess_image
from object_detection import detect_objects
from database import get_spaces, get_booked_spaces, book_space, unbook_space

app = Flask(__name__)

@app.route('/')
def index():
    # Preprocess the image and detect occupied spaces
    img, parking_spaces = preprocess_image('parking_lot.jpg')
    occupied_spaces = detect_objects(img, parking_spaces)

    # Get the total and booked spaces from the database
    total_spaces = get_spaces()
    booked_spaces = get_booked_spaces()

    # Render the template with the parking lot image and the number of spaces
    return render_template('index.html', img=img, parking_spaces=parking_spaces,
        occupied_spaces=occupied_spaces, total_spaces=total_spaces,
        booked_spaces=booked_spaces)

@app.route('/book', methods=['POST'])
def book():
    # Get the space ID and user ID from the form submission
    space_id = int(request.form['space_id'])
    user_id = int(request.form['user_id'])

    # Book the space in the database
    book_space(space_id, user_id)

    # Redirect back to the main page
    return _RedirectStream('/')

@app.route('/unbook', methods=['POST'])
def unbook():
    # Get the space ID from the form submission
    space_id = int(request.form['space_id'])

    # Unbook the space in the database
    unbook_space(space_id)

    # Redirect back to the main page
    return redirect_stderr('/')

if __name__ == '__main__':
    app.run(debug=True)
