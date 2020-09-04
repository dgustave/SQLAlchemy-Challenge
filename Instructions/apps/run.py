# Only function is to run the app, that app has to exist within __init__.py. 
# App(whatever the name of the foldere) is essentially a package, __init__ will house app variable equal Flask(__name__)
from app import app
if __name__ == '__main__':
    app.run(debug = True)