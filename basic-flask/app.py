from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    print(request.args)
    return "Hello world!"

# Passing parameter using request URL
@app.route("/name/", methods=["GET","POST"])
def get_user_name():
    print(request.args)
    return f"Hello {'ss'}!"

# Passing multiple parameters using flask request
@app.route("/user/",methods=["GET","POST"])
def get_user_detail():
    name = request.args.get('name')
    lname = request.args.get('lname')
    address = request.args.get('address', 'Address not found')
    print(request.args)
    obj = request.get_data() # if request has boday data
    print(obj)
    if obj:
        body_data = json.loads(obj)
        print(body_data.get('name', 'Name Not found'))
        print(body_data.get('address', 'Name Not found'))
        print(body_data)
        print(type(obj))
    
    return jsonify({'user name': name, 'user last name':lname})

@app.route("/test/", methods=["GET", "POST"])
def test():
    print(request.args)
    num = int('1')
    return f"Hello world! {num}"

if __name__=="__main__":
    app.run(debug=True, port=5001)