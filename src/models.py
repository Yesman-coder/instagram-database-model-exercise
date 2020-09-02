import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_name = Column(String, primary_key=True)
    name = Column(String(80))
    last_name = Column(String(80))
    email = Column(String(250), nullable=False)
    password = Column(String(250))
    profile_pic = Column(String(250))
    followers = Column(Integer())
    followed = Column(Integer())
    notifications = Column(Integer())
    posts = relationship("Post", backref="user")
    inbox = relationship("Inbox")

    # def like() 
    # def comment()
    # def save()
    # def follow_unfollow()

class Post(Base):
    __tablename__= 'post'
    post_id = Column(Integer, primary_key=True)
    user_name = Column(String, ForeignKey('users.user_name'), nullable=False)
    user = User
    content = Column(String(250))
    date = Column(DateTime())
    likes = Column(Integer())
    comments = Column(String(250))
    saved = Column(Boolean())


class Saved(Base):
    __tablename__ = 'saved'
    saved_id = Column(Integer, primary_key=True)
    user_name = Column(String, ForeignKey('users.user_name'))
    post_id = Column(String, ForeignKey('post.post_id'))
    posts = relationship("Post")

class Feed(Base):
    __tablename__ = 'feed'
    feed_id = Column(Integer, primary_key=True)
    user_name = Column(String, ForeignKey('users.user_name'))
    post_id = Column(String, ForeignKey('post.post_id'))
    date = Column(DateTime())
    posts = relationship("Post")

class Stories(Base):
    __tablename__ = 'stories'
    stories_id = Column(Integer, primary_key=True)
    user_name = Column(String, ForeignKey('users.user_name'))
    post_id = Column(String, ForeignKey('post.post_id'))
    posts = relationship("Post")

class Inbox(Base):
    __tablename__ = 'inbox'
    inbox_id = Column(Integer, primary_key=True)
    user_name = Column(Integer, ForeignKey('users.user_name'), nullable=False)
    new_messages = Column(String(200))
    old_messages = Column(String(200))
    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')