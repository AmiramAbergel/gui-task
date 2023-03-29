from flask import Flask, render_template, redirect, request, url_for

from forms import PageOneForm, PageTwoForm
from utils import read_yaml, write_yaml

app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/', methods=['GET', 'POST'])
def page_one():
  config_data = read_yaml()
  form = PageOneForm()
  if request.method == "POST" and form.validate_on_submit():
    write_yaml(config_data)
    return redirect(url_for('page_two'))

  return render_template('pageOne.html', form=form, config=config_data)


@app.route('/page-two', methods=['GET', 'POST'])
def page_two():
  config_data = read_yaml()
  form = PageTwoForm()
  if form.validate_on_submit():
    if request.method == "POST" and form.validate_on_submit():
      write_yaml(config_data)
      return redirect(url_for('page_one'))

  return render_template('pageTwo.html', form=form, config=config_data)


if __name__ == '__main__':
  app.run(debug=True)
