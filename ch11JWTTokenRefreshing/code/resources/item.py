from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity # get_jwt_claims  #get_jwt_claims used in the course
from models.item import ItemModel

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument(
        'store_id',
        type=int,
        required=True,
        help="Every item needs a store id"
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()

        return {'message': 'Item not found'}, 404

    @jwt_required(fresh=True)
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': f'An item with name {name} already exists.'}, 400

        data = Item.parser.parse_args()

        item = ItemModel(name, data['price'], data['store_id'])
        #item = ItemModel(name, **data)  #same as the line above

        try:
            item.save()
        except:
            return {'message': "An error occurred inserting the item."}, 500

        return item.json(), 201

    @jwt_required()
    def delete(self, name):
        claims = get_jwt()           #get_jwt_clais() was used in the class
        if not claims['is_admin']:
            return {'message': 'Admin privilege required.'}, 401

        item = ItemModel.find_by_name(name)
        if item:
            item.delete()

        return {'message': f'Item {name} deleted'}

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])
        else:
            item.price = data['price']

        item.save()

        return item.json()


class ItemList(Resource):
    #@jwt_optional                  #This is what was used in the course but not in later versions of Flask-JWT-Extended
    @jwt_required(optional=True)
    def get(self):
        user_id = get_jwt_identity()
        items = [item.json() for item in ItemModel.find_all()]
        #items = list(map(lambda x: x.json(), ItemModel.find_all()))
        if user_id:
            return {'items': items}, 200
        return {
            'items': [item['name'] for item in items],
            'message': 'More data available if you log in.'
        }, 200