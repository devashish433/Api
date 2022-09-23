from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

data = [
    {
    'id': 1,
    'Name': "Devashish"
},
{
    'id': 2,
    'Name': "Ram"
},
{
    'id': 3,
    'Name': "Shyam"
},
{
    'id': 4,
    'Name': "Laxman"
}
    ]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/app/api/data/all')
def show():
    return jsonify(data)


@app.route('/app/api/data', methods=['GET'])
def id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Unkown Request"

    result = []

    for data_item in data:
        if data_item['id'] == id:
            result.append(data_item)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)