from tools import *


@app.route('/')
def page0():
    return jsonify(0)


@app.route('/1', methods=['GET'])
def pagedata():
    try:
        data = request.args
        user = data["user"]
        password = data["password"]
        gmail = data["gmail"]
        contact = data["contact"]
        conn = sqlite3.connect(path)

        sql = ''' INSERT INTO box1(user,password,gmail,contact)
              VALUES(?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, (user,password,gmail,contact))
        conn.commit()

        return jsonify("2")

    except Exception as e:
        print("!!!!Error :", e)

@app.route('/find')
def find():
    try:
        conn = sqlite3.connect(path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM " + table)
        rows = cur.fetchall()
        rr = []
        for row in rows:
            data = {}
            data["id"] = row[0]
            data["user"] = row[1]
            data["password"] = row[2]
            data["gmail"] = row[3]
            data["contact"] = row[4]
            rr.append(data)
        return jsonify(rr)
    except Exception as e:
        print("Error :",e)

if __name__ == '__main__':
    app.run(host, port)
