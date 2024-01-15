from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/cloth/')
def cloth():
    data = {
        'title': 'Одежда',
        'content': {
        }
    }
    return render_template('cloth.html', data=data)

@app.route('/shoes/')
def shoes():
    data = {
        'title': 'Обувь',
        'content': {
        }
    }
    return render_template('shoes.html', data=data)

@app.route('/accessories/')
def accessories():
    data = {
        'title': 'Аксессуары',
        'content': {
        }
    }
    return render_template('accessories.html', data=data)


if __name__ == '__main__':
    app.run()
