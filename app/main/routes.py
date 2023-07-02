from flask import redirect, render_template, flash, url_for, request
from app.main import bp
import subprocess
from app.main.forms import IntegerInputForm


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():

    index_view = ['app/templates/index']
    with open('app/templates/index.html', 'w') as outfile:
        subprocess.run(index_view, stdout=outfile)

    form = IntegerInputForm()
    if form.validate_on_submit():

        integer = form.integer.data
        
        integer_input_view = open("app/templates/integer_input.html", "w")
        subprocess.call(['bash', \
                './app/templates/./integer_input', \
                str(integer)], stdout=integer_input_view)

        return redirect(url_for('main.integer_input'))
    return render_template('index.html', title='Tutorials', form=form)

@bp.route('/result', methods=['GET', 'POST'])
def integer_input():

    return render_template('integer_input.html', title='Tutorials')
