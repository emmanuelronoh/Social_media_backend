from flask import Blueprint, request, jsonify
from models import db, User, Post, Comment, Like, Follow
from flask_jwt_extended import create_access_token, jwt_required, JWTManager, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

api = Blueprint('api', __name__)
jwt = JWTManager()

# User Registration
@api.route('/register', methods=['POST'])
def register():
    data = request.json
    if User.query.filter_by(username=data['username']).first():
        return jsonify(message='Username already exists!'), 400
    new_user = User(username=data['username'])
    new_user.set_password(data['password'])  # Hash password
    db.session.add(new_user)
    db.session.commit()
    return jsonify(message='User registered!'), 201

# User Login
@api.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    return jsonify(message='Bad username or password'), 401

# Create a Post
@api.route('/posts', methods=['POST'])
@jwt_required()
def create_post():
    data = request.json
    current_user = get_jwt_identity()
    new_post = Post(content=data['content'], user_id=current_user)
    db.session.add(new_post)
    db.session.commit()
    return jsonify(message='Post created!'), 201

# Get All Posts
@api.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([{'id': post.id, 'content': post.content, 'author': post.author.username} for post in posts]), 200

# Add a Comment to a Post
@api.route('/posts/<int:post_id>/comments', methods=['POST'])
@jwt_required()
def add_comment(post_id):
    data = request.json
    current_user = get_jwt_identity()
    new_comment = Comment(content=data['content'], user_id=current_user, post_id=post_id)
    db.session.add(new_comment)
    db.session.commit()
    return jsonify(message='Comment added!'), 201

# Get Comments for a Post
@api.route('/posts/<int:post_id>/comments', methods=['GET'])
def get_comments(post_id):
    comments = Comment.query.filter_by(post_id=post_id).all()
    return jsonify([{'id': comment.id, 'content': comment.content, 'author': comment.author.username} for comment in comments]), 200

# Like a Post
@api.route('/posts/<int:post_id>/like', methods=['POST'])
@jwt_required()
def like_post(post_id):
    current_user = get_jwt_identity()
    existing_like = Like.query.filter_by(user_id=current_user, post_id=post_id).first()
    if existing_like:
        db.session.delete(existing_like)
        message = 'Post unliked!'
    else:
        new_like = Like(user_id=current_user, post_id=post_id)
        db.session.add(new_like)
        message = 'Post liked!'
    db.session.commit()
    return jsonify(message=message), 200

# Follow a User
@api.route('/follow/<int:user_id>', methods=['POST'])
@jwt_required()
def follow_user(user_id):
    current_user = get_jwt_identity()
    existing_follow = Follow.query.filter_by(follower_id=current_user, followed_id=user_id).first()
    if existing_follow:
        return jsonify(message='You are already following this user.'), 400
    new_follow = Follow(follower_id=current_user, followed_id=user_id)
    db.session.add(new_follow)
    db.session.commit()
    return jsonify(message='Now following user!'), 201

# Unfollow a User
@api.route('/unfollow/<int:user_id>', methods=['POST'])
@jwt_required()
def unfollow_user(user_id):
    current_user = get_jwt_identity()
    existing_follow = Follow.query.filter_by(follower_id=current_user, followed_id=user_id).first()
    if not existing_follow:
        return jsonify(message='You are not following this user.'), 400
    db.session.delete(existing_follow)
    db.session.commit()
    return jsonify(message='Unfollowed user!'), 200
