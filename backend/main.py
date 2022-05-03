from flask import request, Flask, render_template, send_from_directory
from flask_cors import CORS
from sql.sql import sqlDAO

app = Flask(__name__,template_folder='./dist',static_folder='./dist/static/')
CORS(app)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
def index():
    return render_template('index.html', name='index')


@app.route('/v1/sql/user', methods=['GET', 'POST'])
def user():
    requestdata = request.get_json()
    sql = sqlDAO()
    username = requestdata['username']
    password = requestdata['password']
    msg = sql.login(username, password)
    del sql
    return msg


@app.route('/v1/sql/register', methods=['GET', 'POST'])
def register():
    requestdata = request.get_json()
    sql = sqlDAO()
    name = requestdata['name']
    username = requestdata['username']
    password = requestdata['password']
    msg = sql.register(name, username, password)
    del sql
    return {'status': msg}


@app.route('/v1/sql/comment')
def comment():
    sql = sqlDAO()
    data = sql.comment()
    del sql
    return data


@app.route('/v1/sql/insert', methods=['GET', 'POST'])
def insertcomment():
    sql = sqlDAO()
    requestdata = request.get_json()
    name = requestdata['name']
    comment = requestdata['comment']
    time = requestdata['time']
    msg = sql.insert_comment(name, comment, time)
    del sql
    return {"status": msg}


@app.route('/v1/sql/delete', methods=['GET', 'POST'])
def delete():
    sql = sqlDAO()
    requestdata = request.get_json()
    name = requestdata['name']
    id = requestdata['id']
    msg = sql.delete_comment(id, name)
    del sql
    return {"status": msg}


@app.route('/v1/sql/article')
def article():
    sql = sqlDAO()
    limit = request.values.get("limit")
    if limit:
        return sql.getarticle(limit)
    else:
        return sql.getarticle()


@app.route('/v1/sql/order', methods=['GET', 'POST'])
def order():
    sql = sqlDAO()
    requestdata = request.get_json()
    name = requestdata['name']
    activename=requestdata['activename']
    region = requestdata['region']
    date = requestdata['date']
    time = requestdata['time']
    type = requestdata['type']
    resource = requestdata['resource']
    miaoshu = requestdata['miaoshu']
    status = sql.addorder(name=name, resource=resource, miaoshu=miaoshu, region=region, date=date, time=time, type=type,activename=activename)
    del sql
    return {"status": status}
@app.route('/v1/sql/getorder',methods=['GET', 'POST'])
def getorder():
    sql=sqlDAO()
    name = request.values.get("name")
    app.logger.info(name)
    return sql.get_order(name)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=81, debug=True)
