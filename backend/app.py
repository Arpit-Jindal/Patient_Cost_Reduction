from flask import Flask, render_template, redirect, request
import final
import json
import numpy as np
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app, support_credentials=True)
class NpEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, np.integer):
        return int(obj)
    elif isinstance(obj, np.floating):
        return float(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    else:
        return super(NpEncoder, self).default(obj)

@app.route('/')
def hello():
  return render_template('index.html')

@app.route('/patient/<p_id>')
@cross_origin(supports_credentials=True)
def getPatientData(p_id):
  output = json.dumps(final.final_output(p_id),cls=NpEncoder)
  return output

@app.route('/', methods=['POST'])
def submitID():
  p_id = request.form['patientID']
  # p_id='5b891358-1bb3-4bbf-b8a6-a73fbe58efe7'
  output = final.final_output(p_id)
  return render_template('index.html', output = output)


if __name__=='__main__':
  app.run(debug=True)