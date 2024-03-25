from flask import Flask, jsonify, abort, request
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

restaurants=[]

@app.route('/api/restaurants/', methods=["POST"])
def newRestaurant():
    if not request.json or not "name" in request.json:
        abort(400)
    restaurant = {
        "id": len(restaurants),
        "name": request.json["name"],
        "address": {
            "postalCode":request.json["address"]["postalCode"],
            "streetAddress":request.json["address"]["streetAddress"],
            "addressLocality":request.json["address"]["addressLocality"],
            "addressRegion":request.json["address"]["addressRegion"],
            "addressCountry":request.json["address"]["addressCountry"]
        },
        "url":request.json["url"],
        "menu":request.json["menu"],
        "telephone":request.json["telephone"],
        "priceRange":request.json["priceRange"]
    }
    restaurants.append(restaurant)
    return restaurants

@app.route('/api/restaurants/', methods=["GET"])
def returnRestaurants():
    return restaurants

@app.route('/api/restaurants/<int:restaurantId>', methods=["GET"])
def returnRestaurant(restaurantId):
    return restaurants[restaurantId]

@app.route('/api/restaurants/find-city/<string:cityName>', methods=["GET"])
def findCity(cityName):
    cityList = []
    for restaurant in restaurants:
        if "address" in restaurant and "addressRegion" in restaurant["address"]:
            if restaurant["address"]["addressRegion"] == cityName:
                cityList.append(restaurant)
    return jsonify(cityList)

@app.route("/api/restaurants/<int:restaurantId>", methods=["PUT"])
def updateRestaurant(restaurantId):
    restaurant = [restaurant for restaurant in restaurants if restaurant["id"] == restaurantId]
    if len(restaurant) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if "name" in request.json and type(request.json["name"]) != str:
        abort(400)
    if "url" in request.json and type(request.json["url"]) != str:
        abort(400)
    if "menu" in request.json and type(request.json["menu"]) != str:
        abort(400)
    if "telephone" in request.json and type(request.json["telephone"]) != str:
        abort(400)
    if "priceRange" in request.json and type(request.json["priceRange"]) != str:
        abort(400)
    if "postalCode" in request.json and type(request.json["postalCode"]) != str:
        abort(400)
    if "streetAddress" in request.json and type(request.json["streetAddress"]) != str:
        abort(400)
    if "addressLocality" in request.json and type(request.json["addressLocality"]) != str:
        abort(400)
    if "addressRegion" in request.json and type(request.json["addressRegion"]) != str:
        abort(400)
    if "addressCountry" in request.json and type(request.json["addressCountry"]) != str:
        abort(400)
    restaurant[0]["name"] = request.json.get("name", restaurant[0]["name"])
    restaurant[0]["url"] = request.json.get("url", restaurant[0]["url"])
    restaurant[0]["menu"] = request.json.get("menu", restaurant[0]["menu"])
    restaurant[0]["telephone"] = request.json.get("telephone", restaurant[0]["telephone"])
    restaurant[0]["priceRange"] = request.json.get("priceRange", restaurant[0]["priceRange"])
    restaurant[0]["address"]["postalCode"] = request.json.get("postalCode",restaurant[0]["address"]["postalCode"])
    restaurant[0]["address"]["streetAddress"] = request.json.get("streetAddress",restaurant[0]["address"]["streetAddress"])
    restaurant[0]["address"]["addressLocality"] = request.json.get("addressLocality",restaurant[0]["address"]["addressLocality"])
    restaurant[0]["address"]["addressRegion"] = request.json.get("addressRegion",restaurant[0]["address"]["addressRegion"])
    restaurant[0]["address"]["addressCountry"] = request.json.get("addressCountry",restaurant[0]["address"]["addressCountry"])
    return jsonify({"restaurant": restaurant[0]})

@app.route('/api/restaurants/<int:restaurantId>', methods=["DELETE"])
def deleteRestaurant(restaurantId):
    del(restaurants[restaurantId])
    return restaurants


if __name__ == '__main__':
 app.run(host="0.0.0.0", port=4999, debug=True)