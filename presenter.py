from model import Model
from view import View

class Presenter:
    def __init__(self):
        self.view = View()
        self.model = Model()

    def run(self) -> None:
        self.view.create_app(self.app_created)

    def app_created(self, *args):
        self.view.build_initial_window(self.search_by_ingredient, self.search_by_name, self.search_random)

    def search_by_ingredient(self, ingredient_name) -> None:
        self.view.build_search_window()
        data = self.model.search_by_ingredient(ingredient_name)
        if not data:
            drink_names = self.model.get_all_drink_names(data)
            drink_images = self.model.get_all_drink_images(data)
            ingredient_image = self.model.get_ingredient_image_url(ingredient_name)

            self.view.build_ingredient_window(ingredient_name, ingredient_image, drink_names, drink_images, self.search_by_name, self.go_to_initial_window)
        else:
            # Timeout error
            self.view.build_connection_error_window(self.go_to_initial_window)

        return

    def search_by_name(self, name) -> None:
        self.view.build_search_window()
        #chamar a clase modelo para obter os datos
        model_response = self.model.search_by_name(name)


        return

    def search_random(self) -> None:

        return

    def go_to_initial_window(self):
        return
