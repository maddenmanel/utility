from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# 启用 CORS 来允许跨域访问
CORS(app)

@app.route('/api/data')
def get_data():
    """
    返回一些模拟的 JSON 数据
    """
    return jsonify({
        'message': 'Hello from the server!',
        'status': 'success'
    })

@app.route('/test-frontend')
def test_frontend():
    """
    用于模拟前端跨域请求
    """
    return '''
        <html>
            <head><title>CORS Test</title></head>
            <body>
                <h1>Cross-Origin Request Test</h1>
                <script>
                    fetch("http://127.0.0.1:5000/api/data")
                        .then(response => response.json())
                        .then(data => {
                            console.log(data); // 输出返回的数据
                            document.body.innerHTML += "<pre>" + JSON.stringify(data, null, 2) + "</pre>";
                        })
                        .catch(error => {
                            document.body.innerHTML += "<h2>Error: " + error + "</h2>";
                        });
                </script>
            </body>
        </html>
    '''

if __name__ == '__main__':
    # 启动 Flask 服务器
    app.run(debug=True, host="0.0.0.0", port=5000)
