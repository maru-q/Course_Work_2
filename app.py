from flask import Flask, send_from_directory
from views import main_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)


app.run()

