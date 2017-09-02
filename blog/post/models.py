# -*- coding: utf-8 -*-

from blog import db
from model_fields import TimeStamp


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    #create_at = db.Column(db.DateTime)
    #update_at = db.Column(TimeStamp)

    def __repr__(self):
        return '<Post %r>' % self.title

    def __init__(self, title, body):
        self.title = title
        self.body = body


class PostV2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    #create_at = db.Column(db.DateTime)
    #update_at = db.Column(TimeStamp)

    def __repr__(self):
        return '<Post %r>' % self.title

    def __init__(self, title, body):
        self.title = title
        self.body = body


class PostV3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    #create_at = db.Column(db.DateTime)
    #update_at = db.Column(TimeStamp)

    def __repr__(self):
        return '<Post %r>' % self.title

    def __init__(self, title, body):
        self.title = title
        self.body = body


class PostV4(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    #create_at = db.Column(db.DateTime)
    update_at = db.Column(TimeStamp)

    def __repr__(self):
        return '<Post %r>' % self.title

    def __init__(self, title, body, update_at):
        self.title = title
        self.body = body
        self.update_at = update_at