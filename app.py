from flask import Flask, abort, request, render_template_string
import jinja2, re, hashlib

app = Flask(__name__)
app.secret_key = b'SECRET_KEY'


@app.route('/filter', methods=['GET'])
def filter():

        payload = request.args.get('payload')
        bad_chars = "'_#&;"
        if any(char in bad_chars for char in payload):
                abort(403)
        
        template = '''
        <!DOCTYPE html>
        <html>
          <head>
            <title>No Filter</title>
          </head>
          <body>
            <p>''' + payload + '''</p>
          </body>
        </html>'''

        return render_template_string(template)

@app.route('/no_filter', methods=['GET'])
def no_filter():
        
        payload = request.args.get('payload')

        template = '''
        <!DOCTYPE html>
        <html>
          <head>
            <title>No Filter</title>
          </head>
          <body>
            <p>''' + payload + '''</p>
          </body>
        </html>'''

        return render_template_string(template)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=80, debug=False)
