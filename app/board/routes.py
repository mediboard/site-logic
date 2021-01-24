from app.board import bp
from app import db
from app.models import Post, Comment, Tag

from flask import jsonify, request
from flask_login import login_user
from werkzeug.http import HTTP_STATUS_CODES


def success_response(message):
    payload = {'status': HTTP_STATUS_CODES.get(200, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = 200
    return response


@bp.route('/posts/trending', methods=['GET'])
def get_trending_posts():
    posts = Post.query.all()

    posts_response = []
    for post in posts:
        comments = Comment.query.filter_by(post_id=post.id).all()
        tags = Tag.query.filter_by(post_id=post.id).all()
        print(post.__dict__)

        post_dict = post.to_dict()
        post_dict['tags'].append((tag.to_dict() for tag in tags))
        post_dict['comments'].append((comment.to_dict() for comment in comments))
        posts_response.append(post_dict)

    return success_response({'posts': posts_response})


# @bp.route('/posts', methods=['GET'])
# def get_posts():
