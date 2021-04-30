# ShoppingCart
Problem - Create a shopping cart REST API(Use Python/Mongodb) that handles CRUD operations for a specific user like create cart, get items, add items and remove items.

####PORT - 59004

## API Endpoints : 

- For Fetcing all the Cart Items - http://localhost:59004/FetchCartItems?user_name=admin  --> [GET REQUEST]
- For inserting data into cart(in a list) - http://localhost:59004/AddIntoCart  --> [POST REQUEST]
- For deleting the whole cart - http://localhost:59004/DeleteCartItem     --> [POST REQUEST]
- For Update the cart item - http://localhost:59004/UpdateCart     --> [POST REQUEST]

**Insert Input JSON :**

```
[{
    "item_name": "Mi Note 10",
    "item_type": "electronics",
    "quantity": 1,
    "user_name": "admin",
    "FullName": "Aman Khandelwal",
    "price": "Rs 20000"
},
{
    "item_name": "Boat Rockerzz",
    "item_type": "electronics",
    "quantity": 1,
    "user_name": "admin",
    "FullName": "Aman Khandelwal",
    "price": "Rs 2500"
}]
```

- While updating the data I'm creating one unique UUID for that particular cart and also storing the timestamp.

**Update JSON :**

```{
    "id": "cart_9b7cee445a2743cb8da7a5a2fc1867ef",  // Unique ID
    "item_name": "Boat Rockerzz",
    "user_name": "admin",
    "price": "Rs 2900"  // Change Value
}
```


**Delete JSON:**

```
{
    "id":"cart_9b7cee445a2743cb8da7a5a2fc1867ef",
    "user_name": "admin"
}
```

#####[Reference Video Link](https://drive.google.com/file/d/1Gv2eGbq7D9DyMBZXjPGGILcpZWWwl1st/view)


## Code credit

Code credits for this code go to [Aman Khandelwal](https://github.com/wolfblunt)