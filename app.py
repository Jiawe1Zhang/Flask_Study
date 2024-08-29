from flask import Flask, render_template
from flask import request

app = Flask(__name__)


# form 表单 & request 请求
@app.route('/index', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('test.html')
        
    elif request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('onlypassword')
        print(name, password)
        return 'this is post'

from flask import redirect, url_for
# 重定向，redirect & url_for
@app.route('/sb')
def naocan():
    '''在 Flask 中, url_for 函数用于生成特定路由的 URL。
    url_for 函数的参数是视图函数的名称，!!!而不是视图函数本身!!!
    因此，你需要将!!!视图函数名称作为字符串!!!传递给 url_for 函数。'''

    return redirect(url_for('hello'))

from flask import json, make_response
# 重定向的目的地 & 返回json 数据给前端
@app.route('/name')
def hello():
    data = {
        'name':'你的名字'
    }
    return make_response(json.dumps(data,ensure_ascii=False)) 


from flask import abort
# abort() 报错 类似 raise， 来点简单的登陆界面实现  
@app.route('/baocuo', methods = ['GET', 'POST'])
def nima():
    if request.method == 'GET':
        return render_template('try.html')
    if request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('onlypassword')
        if name =='zjw' and password == '123':
            return 'login successfully'
        else:
            abort(404)  
            return None  


# 自定义错误处理方法
@app.errorhandler(404)
def handle_404_error(err):
    # return '出现404错误 错误信息是%s'%err
    return render_template('a404.html')


if __name__== "__main__":
    app.run()

