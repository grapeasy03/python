from app import app

@app.route('/product/add')
def add_product():
    return "hi from add product"