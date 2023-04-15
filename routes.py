from flask import render_template, request, redirect, url_for, flash

from forms import PageForm
from utils import read_yaml, write_yaml, file_upload, classes_shuffle, tests_convert_to_dict

page_one_classes, page_two_classes = classes_shuffle()


def router(app):
  @app.route('/', methods=['GET', 'POST'])
  def page_one():
    flash('App is running.')
    config_data = read_yaml()
    form = PageForm(allowed_classes=page_one_classes)

    if form.validate_on_submit():
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
    flash('Configuration saved.')
    if request.method == 'POST' and form.validate_on_submit():
      form.process(request.form)
      file = request.files.get('report_background_image')
      if file:

        return file_upload(file, form, app, config_data, 'finish_page')
      else:
        form_data = form.data
        updated_form = tests_convert_to_dict(form_data)
        write_yaml(updated_form)

        return redirect(url_for('finish_page'))
    else:

      return render_template('pageTwo.html', form=form, config=config_data, page_two_classes=page_two_classes)

  @app.route('/finish-page', methods=['GET'])
  def finish_page():
    flash('Finished successfully.')

    return render_template('finishPage.html')

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
    if len(config_data['users']) > 1 or index > 1:
      config_data['users'].pop(index - 1)
      write_yaml(config_data)
      return ('', 204)
    else:
      return ('', 400)

  @app.route('/add-row/<int:index>', methods=['GET', 'POST'])
  def add_row(index):
    config_data = read_yaml()
    new_user = {'user_type': 'admin', 'email': '', 'password': ''}
    config_data['users'].insert(index, new_user)
    write_yaml(config_data)

    return ('', 204)
