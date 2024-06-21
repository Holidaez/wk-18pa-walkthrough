from flask import Blueprint, redirect, render_template
from app.models import SimplePerson
from ..forms import SimpleForm
from ..models import db, SimplePerson

bp = Blueprint("simple", __name__, "")

@bp.route('/')
def main_page():
    return render_template('main_page.html')

@bp.route('/simple-form')
def simple_form():
    form = SimpleForm()
    return render_template("simple_form.html", form=form)

@bp.route('/simple-form', methods=['POST'])
def post_simple_form():
    form = SimpleForm()
    if form.validate_on_submit():
        data = SimplePerson(
            name= form.data['name'],
            age= form.data['age'],
            bio= form.data['bio']
        )
        db.session.add(data)
        db.session.commit()
        return redirect('/')
    if form.errors:
        return "Bad Data"

    return render_template("simple_form.html", form=form)


@bp.route('/simple-form-data')
def get_simple_form_data():
    results = SimplePerson.query.filter(SimplePerson.name.like("M%")).all()
    return render_template("simple_form_data.html", results=results )
