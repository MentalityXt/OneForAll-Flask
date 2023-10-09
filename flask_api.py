import threading
from flask import Flask, request, render_template, jsonify, send_from_directory, make_response, redirect, send_file
import os
import test

app = Flask(__name__)

path_token = "abcdefghijklmn"
cookie_token = "abcdefghijklmn"

def validate_token(func):
    def decorated_func(*args, **kwargs):
        token = request.cookies.get('token')  
        if token == cookie_token:  
            print(token)
            return func(*args, **kwargs)  
        else:
            return '', 404
    decorated_func.__name__ = f"decorated_{func.__name__}"  
    return decorated_func


@app.errorhandler(404)
def page_not_found(e):
    return '', 404

@app.route('/index', methods=['GET'])
@validate_token
def index():
    return render_template('index.html')



@app.route(f'/{path_token}', methods=['GET'])
def path_token():
    return render_template('token.html')


@app.route('/set_cookie', methods=['POST'])
def set_cookie():
    data = request.json
    token = data.get('token')
    print(token)
    if token == cookie_token:
        response = make_response(jsonify({"success": True}))
        # response = make_response(redirect('/index'))
        response.set_cookie('token', token)
        return response
    else:
        return 'token error'




@app.route('/getFile', methods=['GET'])
@validate_token
def getFile():
    return render_template('test.html')

@app.route('/getSubdomain', methods=['GET'])
@validate_token
def getSubdomain():
    url = request.args.get('domain')

    # 创建线程来处理耗时的任务
    print(url)
    task_thread = threading.Thread(target=test.oneforall, args=(url,))
    task_thread.start()

    return make_response(jsonify({"success": True}))

def save_txt(str_url):
    print('save urls success')
    open('test.txt', 'w',encoding='utf-8').write(str_url)
    test.oneforalls('test.txt')

@app.route('/uploadSubdomain', methods=['POST'])
@validate_token
def uploadSubdomain():
    if 'file' not in request.files:
        return jsonify(message='No file uploaded', status=400)

    file = request.files['file']
    if file.filename == '':
        return jsonify(message='Empty filename', status=401)

    file.seek(0)
    file_content = file.read().decode('utf-8')
    print(file_content)

    task_thread = threading.Thread(target=save_txt, args=(file_content,))
    task_thread.start()

    # os_operator.save_txt(file_content)


    return jsonify({"status": 200})






@app.route('/files', methods=['GET'])
@validate_token
def list_files():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    files = os.listdir(script_dir+'/results')
    print(files)
    return jsonify(files)

@app.route('/download', methods=['GET'])
@validate_token
def download_file():
    filename = request.args.get('filename')
    print('download: '+filename)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir + '/results', filename)  
    return send_file(filepath, as_attachment=True)

@app.route('/delete', methods=['POST'])
@validate_token
def delete_file():
    filename = request.form.get('filename')
    print('delete: ',filename)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir + '/results', filename)  
    if os.path.exists(filepath):
        os.remove(filepath)
        return jsonify({'message': 'File deleted successfully'})
    else:
        return jsonify({'error': 'File not found'})


if __name__ == '__main__':
    app.run(host="0.0.0.0" ,port=30100, threaded=True)
