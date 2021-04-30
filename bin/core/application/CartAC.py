"""
Cart Layer
"""
from bin.core.application.MongoOperations import CartFormation


def fetch_cart_items(user_name):
    """
    This method is for fetching cart items
    :return: User ID JSON
    """
    try:
        cart_obj = CartFormation()
        response = dict()
        if user_name == "admin":
            cart_data = cart_obj.list_cart_item_from_collection()
            response["message"] = cart_data
            response["status"] = "OK"
            print("Cart Data : ", cart_data)
        else:
            response["message"] = "Invalid user to perform this action"
            response["status"] = "ERROR"
        return response
    except Exception as e:
        import traceback
        print("ERROR :", traceback.print_exc())
        print(str(e))
        raise Exception(str(e))


def add_cart_items(input_json):
    """
    This method is for adding item into cart
    :param input_json:
    :return:
    """
    try:
        cart_obj = CartFormation()
        response = dict()
        if len(input_json) == 1:
            cart_data = cart_obj.add_item_into_collection(input_json[0])
            if cart_data:
                response["message"] = "Successfully inserted the cart in database"
                response["status"] = "OK"
            else:
                response["message"] = "Invalid user to perform this action"
                response["status"] = "ERROR"
        elif len(input_json) > 1:
            cart_data = cart_obj.add_multiple_item_into_collection(input_json)
            if cart_data:
                response["message"] = "Successfully inserted the cart in database"
                response["status"] = "OK"
            else:
                response["message"] = "Invalid user to perform this action"
                response["status"] = "ERROR"
        else:
            response["message"] = "Cart is empty"
            response["status"] = "ERROR"
        return response
    except Exception as e:
        import traceback
        print("ERROR :", traceback.print_exc())
        print(str(e))
        raise Exception(str(e))


def update_cart_items(input_json):
    """
    This method is for updating the  cart item
    :param input_json:
    :return:
    """
    try:
        response = dict()
        if input_json.get("user_name", "") == "admin":
            cart_obj = CartFormation()
            cart_data = cart_obj.update_cart_data(input_json)
            print("Cart Data : ", cart_data)
            response["message"] = cart_data
            response["status"] = "Successfully updated the cart item"
        else:
            response["message"] = "Invalid user to perform this action"
            response["status"] = "ERROR"
        return response
    except Exception as e:
        import traceback
        print("EROR :", traceback.print_exc())
        print(str(e))
        raise Exception(str(e))


def remove_cart(input_json):
    """
    This method is for removing the cart
    :param input_json:
    :return:
    """
    try:
        response = dict()
        if input_json.get("user_name", "") == "admin":
            cart_obj = CartFormation()
            cart_data = cart_obj.remove_cart(input_json)
            print("Cart Data : ", cart_data)
            response["message"] = "Successfully Deleted the whole cart item"
            response["status"] = "OK"
        else:
            response["message"] = "Invalid user to perform this action"
            response["status"] = "ERROR"
        return response
    except Exception as e:
        import traceback
        print("EROR :", traceback.print_exc())
        print(str(e))
        raise Exception(str(e))
