from app import app

if __name__ == '__main__':
    # debug will show errors in the webpage in addition to the terminal
    app.run(debug=True, host='0.0.0.0')