from flask import redirect, render_template, flash, url_for, request
from app.main import bp
import subprocess
from app.main.forms import IntegerInputForm


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    my_cmd = ['app/templates/index']
    with open('app/templates/index.html', 'w') as outfile:
        subprocess.run(my_cmd, stdout=outfile)
    form = IntegerInputForm()
    if form.validate_on_submit():
        flash ('Integer was {}'.format(form.integer.data))
        return redirect(url_for('main.index'))
    return render_template('index.html', title='Tutorials', form=form)

