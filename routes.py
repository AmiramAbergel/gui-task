from flask import render_template, redirect, url_for, request

# Import the app instance from the main file
from forms import PageOneForm
from utils import read_yaml, write_yaml, file_upload, classesShuffle

page_one_classes, page_two_classes = classesShuffle()


def router(app):
  
  @app.route('/', methods=['GET', 'POST'])
  def page_one():
    config_data = read_yaml()
    form = PageOneForm()
    if request.method == 'POST':
      file = request.files.get('report_background_image')
      if file:
        file_upload(file, form, app)
        return redirect(url_for('page_two'))
      else:
        write_yaml(form.data)
        return redirect(url_for('page_two'))
    else:
      return render_template('pageOne.html', form=form, config=config_data, page_one_classes=page_one_classes,
                             page_two_classes=page_two_classes)

  @app.route('/page-two', methods=['GET', 'POST'])
  def page_two():
    config_data = read_yaml()
    form = PageOneForm()
    if request.method == 'POST':
      file = request.files.get('report_background_image')
      if file:
        file_upload(file, form, app)
        return redirect(url_for('page_two'))
      else:
        write_yaml(form.data)
        return redirect(url_for('page_two'))
    else:
      return render_template('pageTwo.html', form=form, config=config_data, page_two_classes=page_two_classes)

  @app.route('/check-all', methods=['GET', 'POST'])
  def check_all():
    config_data = read_yaml()
    for test in config_data['tests']:
      test['value'] = True
    write_yaml(config_data)

    return ('', 204)

  @app.route('/uncheck-all', methods=['GET', 'POST'])
  def uncheck_all():
    config_data = read_yaml()
    for test in config_data['tests']:
      test['value'] = False
    write_yaml(config_data)

    return ('', 204)

  @app.route('/remove-row/<int:index>', methods=['GET', 'POST'])
  def remove_row(index):
    config_data = read_yaml()
    if 1 <= index < len(config_data['users']):
      config_data['users'].pop(index)
      write_yaml(config_data)

    return ('', 204)

  @app.route('/add-row', methods=['GET', 'POST'])
  def add_row():
    empty_cell = False
    if request.method == 'POST':
      config_data = read_yaml()
      for user in config_data['users']:
        if user['email'] == '' or user['password'] == '':
          empty_cell = True
          break
      if not empty_cell:
        config_data['users'].append({'user_type': 'Standard', 'email': '', 'password': ''})
        write_yaml(config_data)

    return ('', 204)
