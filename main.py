from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'some',
    'location': 'new york',
    'salary': 'Rs. 1200000'
  },
  {
    'id': 1,
    'title': 'some',
    'location': 'new york',
    'salary': 'Rs. 1200000'
  },
  {
    'id': 1,
    'title': 'some',
    'location': 'new york',
    'salary': 'Rs. 1200000'
  },
  {
    'id': 1,
    'title': 'some',
    'location': 'new york',
    'salary': 'Rs. 1200000'
  },
  {
    'id': 1,
    'title': 'some',
    'location': 'new york',
    'salary': 'Rs. 1200000'
  },
]


@app.route('/')
def helloWorld():
  return render_template('home.html', jobs=JOBS)


@app.route('/api/jobs')
def apiresponse():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
