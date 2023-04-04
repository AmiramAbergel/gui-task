from flask import render_template, request, redirect, url_for

from forms import PageForm
from utils import read_yaml, write_yaml, file_upload, classesShuffle, tests_convert_to_dict

page_one_classes, page_two_classes = classesShuffle()


def router(app):
  @app.route('/', methods=['GET', 'POST'])
  def page_one():
    config_data = read_yaml()
    form = PageForm(allowed_classes=page_one_classes)
    if request.method == 'POST' or form.validate_on_submit():
      form.process(request.form)
      file = request.files.get('report_background_image')
      if file:
        return file_upload(file, form, app, config_data, 'page_two')
      else:
        form_data = form.data
        updated_form = tests_convert_to_dict(form_data)
        write_yaml(updated_form)
        return redirect(url_for('page_two'))
    else:
      return render_template('pageOne.html', form=form, config=config_data, page_one_classes=page_one_classes,
                             page_two_classes=page_two_classes)

  @app.route('/page-two', methods=['GET', 'POST'])
  def page_two():
    config_data = read_yaml()
    form = PageForm(allowed_classes=page_two_classes)
    if request.method == 'POST' or form.validate_on_submit():
      form.process(request.form)
      file = request.files.get('report_background_image')
      if file:
        return file_upload(file, form, app, config_data, 'page_two')
      else:
        form_data = form.data
        updated_form = tests_convert_to_dict(form_data)
        write_yaml(updated_form)
        return redirect(url_for('page_one'))
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
