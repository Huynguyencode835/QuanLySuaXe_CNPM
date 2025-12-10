from flask import session
from app.routes.index import route
from app._init_ import create_app,login_manager
from app.models.model import User

from app.utils.cart_util import count_cart

app = create_app()
route(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.context_processor
def common_response():
    cart = session.get('cart', {})
    return {
        'cart_stats': count_cart(cart)
    }

if __name__ == "__main__":
    app.run(debug=True)