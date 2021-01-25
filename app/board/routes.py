from app.board import bp
from app import db
from app.models import Post, Comment, Tag
from app.drugs.routes import get_condition_if_exists, get_drug_if_exists

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


def create_posts_response(posts):
    posts_response = []
    for post in posts:
        comments = Comment.query.filter_by(post_id=post.id).all()
        tags = Tag.query.filter_by(post_id=post.id).all()
        print(post.__dict__)

        post_dict = post.to_dict()
        post_dict['tags'].append((tag.to_dict() for tag in tags))
        post_dict['comments'].append((comment.to_dict() for comment in comments))
        posts_response.append(post_dict)

    return posts_response


@bp.route('/posts/trending', methods=['GET'])
def get_trending_posts():
    posts = Post.query.all()

    return success_response({'posts': create_posts_response(posts)})


@bp.route('/posts', methods=['GET'])
def get_posts():
    user = request.args.get('user_id')
    category = request.args.get('category')
    timestamp = request.args.get('timestamp')
    tags = request.args.get('tags')

    #  First filter by the first three
    filter_args = {}
    if user:
        filter_args['user'] = user
    if category:
        filter_args['category'] = category
    if timestamp:
        filter_args['timestamp'] = timestamp

    base = Post.query.filter_by(**filter_args)
    posts = base.all() if not tags else base.join(Tag).filter_by(Tag.name.in_(tags)).all()

    return success_response({'posts': create_posts_response(posts)})


@bp.route('/posts', methods=['POST'])
def create_post():
    data = request.json or {}

    tags = data.get('tags', [])
    new_post = Post(**data['post'])
    db.session.add(new_post)
    db.session.commit()

    for tag in tags:
        new_tag = Tag(**tag)
        condition_lookup = get_condition_if_exists(new_tag.name)
        drug_lookup = get_drug_if_exists(new_tag.name)

        if condition_lookup:
            new_tag.condition_id = condition_lookup.id
        if drug_lookup:
            new_tag.drug_id = drug_lookup.id

        new_tag.post_id = new_post.id
        db.session.add(new_tag)

    db.session.commit()
    return success_response({'post': create_posts_response([new_post])})
