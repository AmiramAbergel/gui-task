from flask import Flask, render_template, redirect, url_for, flash, request

from forms import PageOneForm, PageTwoForm
from utils import read_yaml, write_yaml, log_message

app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/', methods=['GET', 'POST'])
def page_one():
  config_data = read_yaml()
  form = PageOneForm(data=config_data)
  if request.method == 'POST':
    write_yaml(form.data)
    log_message("Saved configuration for Page 1.")
    flash('Configuration saved.')
    return redirect(url_for('page_two'))
  else:
    return render_template('pageOne.html', form=form, config=config_data)


@app.route('/page-two', methods=['GET', 'POST'])
def page_two():
  config_data = read_yaml()
  form = PageTwoForm()
  if request.method == 'POST':
    write_yaml(form.data)
    log_message("Saved configuration for Page 2.")
    flash('Configuration saved.')
    return redirect(url_for('page_one'))
  else:
    return render_template('pageTwo.html', form=form, config=config_data)


if __name__ == '__main__':
  app.run(debug=True)
