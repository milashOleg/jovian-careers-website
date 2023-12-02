from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analist',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,000'
  },
  {
    'id': 2,
    'title': 'Data Sceintist',
    'location': 'Dehli, India',
    'salary': 'Rs. 15,000'
  },
  {
    'id': 3,
    'title': 'Frontend Ingener',
    'location': 'Remote',
    'salary': 'Rs. 12,000'
  },
  {
    'id': 4,
    'title': 'Backend Ingener',
    'location': 'San Francisco, USA',
    'salary': '$120,000'
  }
]

@app.route('/')
def hello_world():
  return render_template('home.html',
                         jobs=JOBS,
                        company_name='Jovian')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
