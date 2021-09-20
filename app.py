from flask import Flask
from views import views
from config import Config

## Initializes the application
app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(views, url_prefix="/views")

if (__name__) == '__main__':
    app.run(debug=True, port=8000)
