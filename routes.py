from flask import render_template, request, flash

from forms import PageForm
from utils import read_yaml, write_yaml, classes_shuffle, process_form, shutdown_server

page_one_classes, page_two_classes = classes_shuffle()


def router(app, gui_app, callback=None):
  @app.route('/', methods=['GET', 'POST'])
  def page_one():
    flash('App is running.')
    config_data = read_yaml()
    form = PageForm(allowed_classes=page_one_classes)
    if form.validate_on_submit():
      return process_form(form, app, config_data, 'page_two')

    return render_template('pageOne.html', form=form, config=config_data, page_one_classes=page_one_classes,
                           page_two_classes=page_two_classes)

  @app.route('/page-two', methods=['GET', 'POST'])
  def page_two():
    config_data = read_yaml()
    form = PageForm(allowed_classes=page_two_classes)
    flash('Configuration saved.')
    if request.method == 'POST' and form.validate_on_submit():
      return process_form(form, app, config_data, 'finish_page')

    return render_template('pageTwo.html', form=form, config=config_data, page_two_classes=page_two_classes)

  @app.route('/finish-page', methods=['GET'])
  def finish_page():
    config_data = read_yaml()
    flash('Finished successfully.')

    return render_template('finishPage.html', config=config_data)

  @app.route('/shutdown', methods=['GET'])
  def shutdown():
    shutdown_server(gui_app,callback)

    return 'Server shutting down...'

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
