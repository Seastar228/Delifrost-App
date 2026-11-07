import os
from flask import Flask, render_template, request, redirect, url_for
from models import db, Supermarket, MonthlyTarget, Order, OrderItem, Return

app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'delifrost.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    supermarkets = Supermarket.query.all()
    return render_template('index.html', supermarkets=supermarkets)

@app.route('/add_order', methods=['POST'])
def add_order():
    supermarket_id = request.form.get('supermarket_id')
    product_name = request.form.get('product_name')
    quantity = int(request.form.get('quantity'))
    unit_price = float(request.form.get('unit_price'))

    order = Order(supermarket_id=supermarket_id)
    db.session.add(order)
    db.session.commit()

    item = OrderItem(order_id=order.id, product_name=product_name, quantity=quantity, unit_price=unit_price)
    db.session.add(item)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/add_return', methods=['POST'])
def add_return():
    supermarket_id = request.form.get('supermarket_id')
    product_name = request.form.get('product_name')
    quantity = int(request.form.get('quantity'))
    reason = request.form.get('reason')

    ret = Return(supermarket_id=supermarket_id, product_name=product_name, quantity=quantity, reason=reason)
    db.session.add(ret)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


