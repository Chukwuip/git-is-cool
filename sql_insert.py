from flask import request
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        
        conn = pyodbc.connect(
            "Driver={ODBC Driver 17 for SQL Server};"
            "Server=tcplida-dat-cms-test.windows.net,1433;"
            "Database=lida_dat_cms_test;"
            "Uid=medich;"
            "Pwd=Password321;"
            "Encrypt=yes;"
            "TrustServerCertificate=no;"
            "Connection Timeout=30;"
        )
        
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tblDoctest (fname, lname) VALUES (?, ?)", fname, lname)
        conn.commit()

        return 'Success!'
