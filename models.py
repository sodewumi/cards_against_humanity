from flask_sqlalchemy import SQLAlchemy
from flask import Flask

import os

db = SQLAlchemy()

game_player = db.Table('game_player',
                       db.Column('game_id', db.Integer, db.ForeignKey('game.id')),
                       db.Column('player_id', db.Integer, db.ForeignKey('player.id'))
                       )

round_player = db.Table('round_player',
                        db.Column('round_id', db.Integer, db.ForeignKey('round.id')),
                        db.Column('player_id', db.Integer, db.ForeignKey('player.id'))
                        )

player_hand = db.Table('player_hand',
                       db.Column('round_id', db.Integer, db.ForeignKey('card.id')),
                       db.Column('player_id', db.Integer, db.ForeignKey('player.id'))
                       )


class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    password = db.Column(db.String(20))


class Room(db.Model):
    __tablename__ = "rooms"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))


class Game(db.Model):
    __tablename__ = "games"

    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))


class Round(db.Model):
    __tablename__ = "rounds"

    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    round_number = db.Column(db.Integer)
    black_card_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    judge_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    winner_id = db.Column(db.Integer, db.ForeignKey('player.id'))


class Player(db.Model):
    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(20))
    game_id = db.Column(db.Integer, db.ForeignKey('room.id'))


class Hand(db.Model):
    __tablename__ = "hands"

    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))


class BlackMasterDeck(db.Model):
    __tablename__ = "black_master_deck"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    pick_number = db.Column(db.Integer)


class BlackGameDeck(db.Model):
    __tablename__ = "black_game_deck"

    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    card_id = db.Column(db.Integer, db.ForeignKey('black_master_deck.id'))


class WhiteMasterDeck(db.Model):
    __tablename__ = "white_master_deck"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))


class WhiteGameDeck(db.Model):
    __tablename__ = "white_game_deck"

    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    card_id = db.Column(db.Integer, db.ForeignKey('black_master_deck.id'))


def connect_to_db(app):
    """Connect the database to our Flask app."""
    if os.environ.get('DATABSE_URL') is None:
        SQLALCHEMY_DATABASE_URI = os.environ['LOCAL_DATABASE_URI']
    else:
        SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)
    db.create_all()
