* How to format in vscode
  > right-click and choose `format document`
  > ctrl-shift-p 

* How to choose default python interpreter
  > ctrl-shift-p
  > input `select interpreter`

* sqlite flask how-to
  ```
  # Go to the app.py directory
  python
  from app import db
  db.create_all()
  ```

* diff class and id in CSS
  > A class name can be used by multiple HTML elements, while an id name must only be used by one HTML element within the page  
  > In the CSS, a class selector is a name preceded by a full stop (“.”) and an ID selector is a name preceded by a hash character (“#”)


* [flask url_for in javascript](https://stackoverflow.com/questions/50670010/flask-url-for-with-dynamic-file-name)
  ```
  # In your app.py file:
  app.jinja_env.globals['js_bundle_file'] = 'bundle-1.1.js'

  # In your template:
  <script src="{{url_for('static', filename=js_bundle_file)}}"></script>

  # Instead of hardcoding your bundle file, you could also look for it using a slightly hacky list comprehension:
  app.jinja_env.globals['js_bundle_file'] = [f for f in os.listdir('static') if f.endswith('.js') and f.startswith('bundle')][0]

  # or this cleaner looking glob:
  import glob
  app.jinja_env.globals['js_bundle_file'] = glob.glob('static/bundle*.js')[0]

  ```

* [turn your web site into async with aiohttp](https://flask-aiohttp.readthedocs.io/en/latest/firstofall.html)
