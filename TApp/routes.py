from TApp import appv
from flask import render_template
from TApp.jsonopener import get_json_file
from TApp.forms import FileDetailForm


@appv.route('/', methods=["GET", "POST"])
@appv.route('/index', methods=["GET", "POST"])
def start_page():
    form = FileDetailForm()
    if form.validate_on_submit():
        tabfl = get_json_file(form.file_.data)
        return render_template('table.html', fields=form.fields.data,
                               arrayofdict=tabfl)
    return render_template('start_detail.html', form=form)
