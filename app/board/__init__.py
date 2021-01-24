from flask import Blueprint

bp = Blueprint('board', __name__)

from app.board import routes
