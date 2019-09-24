from flask import Flask, request
from flask_restful import Resource,Api,reqparse
from flask_jwt import JWT, jwt_required

from security import authentication,identity

app = Flask(__name__)
app.secret_key = "revanth"
api = Api(app)
jwt = JWT(app,authentication,identity)

items = []

class Item(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument('price',
        type=float,
        required=True,
        help = "this feild is required"
    )

    @jwt_required()
    def get(self,name):
        item = next(filter(lambda x:x['name']==name,items),None)
        return {"item":item},404 if item else 404

    def post(self,name):
        if next(filter(lambda x:x['name']==name,items),None):
            return {"message":"item with '{}' alreay exist".format(name)},404
        request_data = Item.parse.parse_args()
        item = {"name":name,"price":request_data['price']}
        items.append(item)
        return item, 201

    def delete(self,name):
        global items
        items = list(filter(lambda x:x['name']!=name,items))
        return {'message':'items is deleted'}

    def put(self,name):
        
        request_data = Item.parse.parse_args()
        item = next(filter(lambda x:x['name']==name,items),None)
        if item:
            item.update(request_data)
        else:
            item = {'name':name,'price':request_data['price']}
            items.append(item)
        return item
        

class ItemList(Resource):
    def get(self):
        return {"items":items}

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')

app.run(port=5000,debug=True)