from TApp import appv
from flask import render_template, request, redirect
from TApp.jsonopener import get_json_file, FIELDS, FILE


@appv.route('/', methods=["GET", "POST"])
@appv.route('/index', methods=["GET", "POST"])
def start_page():
    if request.method == "POST":
        return redirect('/table')
    return render_template('start_only.html', title=FILE)


@appv.route('/table')
def table_page():
    tabfl = get_json_file(FILE)
    return render_template('table.html',
                           fields=FIELDS,
                           arrayofdict=tabfl)
