import requests
from typing import Any


class Model:
    def search_by_name(self, name) -> Any:
        try:
            response = requests.get("wwww.thecocktaildb.com/api/json/v1/1/search.php?s=" + name, timeout=3)
            data = response.json()
            return data
        except Exception as e:
            return e





    def search_by_ingredient(self, ingredient_name) -> Any:
        try:
            response = requests.get("www.thecocktaildb.com/api/json/v1/1/filter.php?i=" + ingredient_name, timeout=3)
            data = response.json()
            return data
        except Exception:
            return []
    def get_all_drink_names(self, json_data) -> Any:
        drink_names_array = []
        for drinks in json_data:
            # drinks is a dictionary
            for drinks_attributes in drinks:
                drink_names_array.append(drinks_attributes["strDrink"])
        return drink_names_array

    def get_all_drink_images(self, json_data) -> Any:
        drink_images_array = []
        for drinks in json_data:
            # drinks is a dictionary
            for drinks_attributes in drinks:
                drink_images_array.append(drinks_attributes["strDrinkThumb"])
        return drink_images_array

    def get_ingredient_image_url(self, ingredient_name) -> Any:
        return "https://www.thecocktaildb.com/images/ingredients/" + ingredient_name + "Small.png"



    def search_random(self) -> Any:
        response = requests.get("www.thecocktaildb.com/api/json/v1/1/random.php")
        return response

    """def get_n_drinks(self, n, json_data) -> Any:
        drinks_array = []
        i=0
        while i < n:
            drinks_array.append(json_data["drinks"][i])
            i += 1
        return drinks_array"""



