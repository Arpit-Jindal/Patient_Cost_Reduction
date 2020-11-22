from flask import Flask, render_template, redirect, request
import final
app = Flask(__name__)

@app.route('/')
def hello():
  return render_template('index.html')


@app.route('/', methods=['POST'])
def get_data():
  p_id = request.form['patientID']
  # p_id='5b891358-1bb3-4bbf-b8a6-a73fbe58efe7'
  output = final.final_output(p_id)
  return render_template('index.html', output = output)


if __name__=='__main__':
  app.run(debug=True)