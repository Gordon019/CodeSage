from flask import Flask, request, render_template
from app.logic import analyzer, fixer, tester

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        code = request.form['code']
        parsed = analyzer.analyze(code)
        fixed = fixer.repair(code)
        test_code = tester.generate_tests(code)
        return render_template('index.html', original=code, fixed=fixed, tests=test_code)
    return render_template('index.html')
