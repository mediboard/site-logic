from flask import Blueprint

bp = Blueprint('drugs', __name__)

from app.drugs import models, routes 