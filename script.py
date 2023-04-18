from gui_app import app

if __name__ == "__main__":
  yaml_data = app.main(debug=False)
  print("Received YAML data:")
  print(yaml_data)
