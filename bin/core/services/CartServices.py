"""
CART Service Layer
"""
import json
import traceback
from base64 import b64encode, b64decode
from flask import request, Blueprint
from bin.core.application import CartAC
import ast

# Canvas Blueprint
cart = Blueprint("Cart", __name__)


@cart.route("/FetchCartItems", methods=["GET"])
def fetch_cart_items_service():
    """
    API Endpoint for fetching users
    :return:
    """
    if request.method == 'GET':
        print("Inside Fetch Users")
        try:
            user_name = request.args.get("user_name", "")
            results = CartAC.fetch_cart_items(user_name)
            response = dict()
            response['status'] = "OK"
            response['message'] = results
            return response
        except Exception as e:
            print(str(e))
            message = 'Unable to fetch cart items'
            return message


@cart.route("/AddIntoCart", methods=["POST"])
def add_cart_items_service():
    """
    API Endpoint for creating project
    :return:
    """
    if request.method == 'POST':
        print("Inside add_cart_items_service")
        try:
            input_json = json.loads(request.get_data())
            print("Input JSON Type: ", type(input_json))
            print("Input JSON : " + str(input_json))
            response = CartAC.add_cart_items(input_json)
            return response
        except Exception as e:
            print(str(e))
            message = "Unable to add details in the collection"
            return dict(status="ERROR", message=message)


@cart.route("/UpdateCart", methods=["POST"])
def update_cart_items_service():
    """
    API Endpoint for creating project
    :return:
    """
    if request.method == 'POST':
        print("Inside add_cart_items_service")
        try:
            input_json = json.loads(request.get_data())
            print("Input JSON Type: ", type(input_json))
            print("Input JSON : " + str(input_json))
            response = CartAC.update_cart_items(input_json)
            return response
        except Exception as e:
            print(str(e))
            message = "Unable to add details in the collection"
            return dict(status="ERROR", message=message)


@cart.route("/DeleteCartItem", methods=["POST"])
def remove_cart_service():
    """
    API Endpoint for creating project
    :return:
    """
    if request.method == 'POST':
        print("Inside add_cart_items_service")
        try:
            input_json = json.loads(request.get_data())
            print("Input JSON Type: ", type(input_json))
            print("Input JSON : " + str(input_json))
            response = CartAC.remove_cart(input_json)
            return response
        except Exception as e:
            print(str(e))
            message = "Unable to add details in the collection"
            return dict(status="ERROR", message=message)


