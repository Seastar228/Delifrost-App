from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Supermarket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_code = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(150), nullable=False)
    targets = db.relationship('MonthlyTarget', backref='supermarket', lazy=True)
    orders = db.relationship('Order', backref='supermarket', lazy=True)
    returns = db.relationship('Return', backref='supermarket', lazy=True)

class MonthlyTarget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supermarket_id = db.Column(db.Integer, db.ForeignKey('supermarket.id'), nullable=False)
    month = db.Column(db.String(20), nullable=False)
    target_amount = db.Column(db.Float, nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supermarket_id = db.Column(db.Integer, db.ForeignKey('supermarket.id'), nullable=False)
    date = db.Column(db.Date, default=datetime.date.today, nullable=False)
    items = db.relationship('OrderItem', backref='order', lazy=True)

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)

class Return(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supermarket_id = db.Column(db.Integer, db.ForeignKey('supermarket.id'), nullable=False)
    date = db.Column(db.Date, default=datetime.date.today, nullable=False)
    product_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    reason = db.Column(db.String(200))

