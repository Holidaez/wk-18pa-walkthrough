from flask import Flask
from .routes import simple
from flask_migrate import Migrate
from .config import Configuration
from .models import db

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(simple.bp)
db.init_app(app)
Migrate(app, db)
