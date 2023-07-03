from flask import redirect, render_template, url_for, request
from app.main import bp
from app.main.forms import IntegerInputForm
from app.main.generator import Generator


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():

    gen_index = Generator()
    gen_index.index_generator()

    form = IntegerInputForm()
    if form.validate_on_submit():
        gen_integer_input = Generator()
        gen_integer_input.integer_input_generator(form.integer.data)
        return redirect(url_for('main.integer_input'))
    return render_template('index.html', title='Tutorials', form=form)

@bp.route('/integer_input')
def integer_input():
    return render_template('integer_input.html', title='Tutorials')


@bp.route('/uptime')
def uptime():
    pass

@bp.route('/diskspace')
def diskspace():
    pass

@bp.route('/homespace')
def homespace():
    pass
