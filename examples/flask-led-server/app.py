from flask import Flask, request, jsonify, render_template

colors = {'red': '255', 'green': '255', 'blue': '255'}
#red = 255
#green = 125
#blue = 102

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')
 
'''
<form method ="POST" action = "/process">
              <input type = "range" name = "red" max=255><br>
              <input type = "range" name = "green" max=255><br>
              <input type = "range" name = "blue" max =255><br>
              <input type = "submit" value = "Laheta">
            </form>
'''

@app.route('/process', methods=['POST'])
def process():
  colors['red']  = request.form['red']
  colors['green'] = request.form['green']
  colors['blue'] = request.form['blue']
  return  '<h1> Values are saved!<h1>'

@app.route('/processjson', methods = ['POST', 'GET'])
def processjson():
  ##red, green, blue  = process()
  #data = request.get_json()
  #red = data['red']
  return jsonify({"red" : colors['red'], "green": colors['green'], "blue": colors['blue']})

if __name__ == '__main__':
  app.run(debug = True, host='0.0.0.0')
