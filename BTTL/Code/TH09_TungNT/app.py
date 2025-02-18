
from models import db, User, Category, Product, Cart, Order, nhanVien
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask import flash

app = Flask(__name__)

# Cấu hình kết nối CSDL MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/TH09_TungNT'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Secret key cho session

db.init_app(app)

#kiểm tra đăng nhập
# Kiểm tra nếu người dùng đã đăng nhập
def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:  # Kiểm tra session
            flash('Vui lòng đăng nhập để tiếp tục.', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Đăng xuất
@app.route('/logout')
@login_required
def logout():
    # Xóa dữ liệu session và chuyển hướng về trang chủ hoặc trang đăng nhập
    session.pop('user_id', None)  # Xóa session của user_id
    session.pop('username', None)  # Xóa session của username
    flash('Đăng xuất thành công!', 'success')  # Hiển thị thông báo
    return redirect(url_for('login'))  # Chuyển hướng đến trang đăng nhập

# Route trang chính
@app.route('/')
def index():
    products = Product.query.all()
    categories = Category.query.all()
    return render_template('index.html', products=products, categories=categories)
@app.route('/admin')
@login_required
def adindex():
    products = Product.query.all()
    categories = Category.query.all()
    return render_template('index2.html', products=products, categories=categories)
# Route đăng nhập
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        # if user and check_password_hash(user.password, password):
        if user and user.password ==  password:
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Đăng nhập thành công!', 'success')
            return redirect(url_for('index'))  # Chuyển hướng về trang chủ
        else:
            flash('Tên đăng nhập hoặc mật khẩu không đúng.', 'danger')

    return render_template('login.html')

# Route hiển thị danh mục 
@app.route('/categories')
def categories():
    categories = Category.query.all()
    products = Product.query.all()
    return render_template('categories.html', categories=categories, products=products)

# Route hiển thị danh sách sản phẩm
@app.route('/products')
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)

@app.route('/addProducts', methods=['GET', 'POST'])
@login_required
def addprd():
    if request.method == 'POST':
        # Lấy dữ liệu từ form
        name = request.form['name']
        price = float(request.form['price'])
        description = request.form['description']
        image = request.form['image']
        category_id = int(request.form['category_id'])
        
        # Thêm sản phẩm mới vào cơ sở dữ liệu
        new_product = Product(name=name, price=price, description=description, image=image, category_id=category_id)
        db.session.add(new_product)
        db.session.commit()
        
        # Sau khi thêm sản phẩm, chuyển hướng về trang sản phẩm
        return redirect(url_for('addprd'))  # Hoặc trang khác nếu muốn
        
    categories = Category.query.all()  # Lấy tất cả các thể loại
    return render_template('add_product.html', categories=categories)

from flask import request, redirect, url_for

@app.route('/editProduct/<int:product_id>', methods=['GET', 'POST'])
@login_required
def editProduct(product_id):
    # Lấy thông tin sản phẩm từ cơ sở    dữ liệu
    product = Product.query.get_or_404(product_id)
    categories = Category.query.all()

    if request.method == 'POST':
        # Lấy thông tin từ form
        product.name = request.form['name']
        product.price = request.form['price']
        product.description = request.form['description']
        product.image = request.form['image']
        product.category_id = request.form['category_id']

        # Lưu lại thay đổi vào cơ sở dữ liệu
        db.session.commit()
        
        # Chuyển hướng đến trang danh sách sản phẩm (hoặc trang bất kỳ)
        return redirect(url_for('adindex'))

    return render_template('edit_product.html', product=product, categories=categories)

@app.route('/deleteProduct/<int:product_id>', methods=['POST'])
@login_required
def deleteProduct(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('adindex'))  # Quay lại trang danh sách sản phẩm


# Route giỏ hàng
@app.route('/cart')
def cart():
    cart_items = Cart.query.all()
    return render_template('cart.html', cart_items=cart_items)

# Route đơn hàng
@app.route('/orders')
@login_required
def orders():
    orders = Order.query.all()
    return render_template('orders.html', orders=orders)

@app.route('/product_detail/<int:product_id>')
@login_required
def product_detail(product_id):
    # Lấy sản phẩm từ cơ sở dữ liệu dựa trên ID
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)

@app.route('/nhanvien')
def nhanvien():
    nhanvienn = nhanVien.query.all()
    return render_template('nhanvien.html', nhanvienn = nhanvienn)

@app.route('/addNhanVien', methods=['GET', 'POST'])
def addNV():
    if request.method == 'POST':
        # Lấy dữ liệu từ form
        name = request.form['name']
        id = request.form['id']
        # Thêm sản phẩm mới vào cơ sở dữ liệu
        new_nhanvien = nhanVien(id=id, name=name)
        db.session.add(new_nhanvien)
        db.session.commit()
        
        # Sau khi thêm sản phẩm, chuyển hướng về trang sản phẩm
        return redirect(url_for('nhanvien'))  # Hoặc trang khác nếu muốn
    return render_template('add_nhanvien.html')

# Route xử lý thanh toán
@app.route('/checkout/<int:product_id>', methods=['GET', 'POST'])
@login_required
def checkout(product_id):
    product = Product.query.get(product_id)

    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        phone = request.form['phone']
        
        # Xử lý logic đặt hàng (Lưu vào CSDL nếu cần)
        return render_template('success.html', name=name, product=product)

    return render_template('checkout.html', product=product)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Tạo bảng nếu chưa có
    app.run(debug=True)
