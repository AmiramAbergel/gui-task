from gui_app.app import main

if __name__ == "__main__":
  yaml_data = main(debug=False)
  print("Received YAML data:")
  print(yaml_data)
