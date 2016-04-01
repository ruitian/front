# -*- coding: utf-8 -*-
from app import db


class CommodityModel(db.Model):

    __tablename__ = 'commodity'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=True)
    link = db.Column(db.Text, nullable=True)
    description = db.Column(db.Text, nullable=True)
    imglink = db.Column(db.Text, nullable=True)
    price = db.Column(db.String(64), nullable=True)
