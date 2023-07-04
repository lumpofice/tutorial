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
        gen_integer_input.integer_input_generator(form.integer.data, form.count.data)
        return redirect(url_for('main.integer_input'))
    return render_template('index.html', title='Tutorials', form=form)

@bp.route('/integer_input')
def integer_input():
    return render_template('integer_input.html', title='Tutorials')


@bp.route('/uptime')
def uptime():
    gen_uptime = Generator()
    gen_uptime.uptime_generator()
    return render_template('uptime.html', title='Tutorials')

@bp.route('/disk_space')
def disk_space():
    gen_disk_space = Generator()
    gen_disk_space.disk_space_generator()
    return render_template('disk_space.html', title='Tutorials')

@bp.route('/home_space')
def home_space():
    gen_home_space = Generator()
    gen_home_space.home_space_generator()
    return render_template('home_space.html', title='Tutorials')
