from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    #email = request.form.get('email')
    #passsword = request.form.get('password')
    #remember = True if request.form.get('remember') else False

    #user = User.query.filter_by(email=email).first()

    #if not user or not check_password_hash(user.password, passsword):
    #    flash('El usuario y/o la contraseña son incorrectos')
    #    return redirect(url_for('auth.login'))

    #login_user(user, remember=remember)
    #return redirect(url_for('reloj.relojes'))
    return 0


@auth.route('/signup', methods=['GET'])
def signup_get():
    return render_template('/signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    # email = request.form.get('email')
    # name = request.form.get('name')
    # password = request.form.get('password')

    # user = User.query.filter_by(email=email).first()

    #if user:
    #    flash('Ese correo electrónico ya existe')
    #    return redirect(url_for('auth.signup'))
#
    #userDataStore.create_user(name=name, email=email,
    #                          password=generate_password_hash(password, method='sha256'))
    #db.session.commit()
#
    #return redirect(url_for('auth.login'))
    return 0

@auth.route('/logout')
# @login_required
def logout():
    #logout_user()
    #return redirect(url_for('main.index'))
    return 0
