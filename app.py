from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

EXCEL_FILE = 'static/data/seats.xlsx'

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        fullname = request.form.get('fullname').strip()
        df = pd.read_excel(EXCEL_FILE)
        row = df[df['Name'].str.lower() == fullname.lower()]

        if not row.empty:
            seat_number = int(row['Seat'].values[0])
            return redirect(url_for('seat', seat=seat_number))
        else:
            error = "Name not found. Please check spelling."

    return render_template('index.html', error=error)

@app.route('/seat/<int:seat>')
def seat(seat):
    return render_template('seats.html', seat=seat)

if __name__ == '__main__':
    app.run(debug=True)
