import sys

import gi

gi.require_version("Gtk", "4.0")
from gi.repository import GLib, Gtk


class View:
    def buscar(self, _w: Gtk.Widget):
        nombre = self.search_entry.get_text()
        self.callback_buscar(nombre)

    # Metodo que e invocado por presenter ao inicio do programa, que crea a aplicacion
    def create_app(self, app_created):
        self.app = Gtk.Application(application_id="com.example.myapp")
        self.app.connect('activate', app_created)
        self.app.run(None)

    def build_initial_window(self, callb_search_by_ingredient, callb_search_by_name, callb_search_random) -> None:
        self.close_current_window()

        # Creamos a ventana, e facemos que se conecte a señal "destroy".
        # cando se emita a señal, a funcion wind.close ejecutase
        initial_window = Gtk.ApplicationWindow(
            application=self.app,
            title="Ventana inicial"
        )
        self.app.add_window(initial_window)
        initial_window.connect("destroy", lambda wind: wind.close())

        # Create a horizontal box to hold label and buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=30)
        initial_window.set_child(hbox)

        # Left side: vertical box for the label
        left_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        hbox.append(left_box)

        label = Gtk.Label(label="Welcome!")
        left_box.append(label)

        image = Gtk.Image.new_from_file(
            "/home/manu/Desktop/python/IPM/long_island_cocktail.jpg")  # Replace with the actual path to your image file
        left_box.append(image)

        # Right side: vertical box for buttons
        right_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        hbox.append(right_box)

        # Exit button on the top right
        top_row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        right_box.append(top_row)

        # Create buttons and add them to the right box
        search_ingredient_entry = Gtk.SearchEntry(
            halign=Gtk.Align.CENTER,
            hexpand=True
        )
        search_ingredient_entry.placeholder_text = "Search by ingredient"

        search_name_entry = Gtk.SearchEntry(
            halign=Gtk.Align.CENTER,
            hexpand=True
        )
        search_name_entry.placeholder_text = "Search by name"

        button_search_random = Gtk.Button(label="Search Random")

        search_ingredient_entry.connect("activate", callb_search_by_ingredient)
        right_box.append(search_ingredient_entry)

        search_name_entry.connect("activate", callb_search_by_name)
        right_box.append(search_name_entry)

        right_box.append(button_search_random)
        button_search_random.connect("clicked", callb_search_random)

        initial_window.present()

    def close_current_window(self) -> None:
        old_window = self.app.get_active_window()
        if old_window is None:
            return
        old_window.destroy()
        return

    def build_search_window(self) -> None:
        self.close_current_window()
        search_window = Gtk.ApplicationWindow(
            application=self.app,
            title="Ventana busqueda"
        )
        self.app.add_window(search_window)
        search_window.connect("destroy", lambda wind: wind.close())

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=30)
        search_window.set_child(hbox)

        label = Gtk.Label(label="Waiting for search...")
        hbox.append(label)

        main_spinner = Gtk.Spinner()
        main_spinner.start()
        hbox.append(main_spinner)

        search_window.present()


    def build_connection_error_window(self, callb_go_to_initial_window) -> None:
        self.close_current_window()
        connection_error_window = Gtk.ApplicationWindow(
            application=self.app,
            title="Ventana busqueda"
        )
        self.app.add_window(connection_error_window)
        connection_error_window.connect("destroy", lambda wind: wind.close())

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=30)
        connection_error_window.set_child(hbox)

        label = Gtk.Label(label="Can't connect to our database :(!")
        hbox.append(label)

        connection_error_window.present()

    def build_ingredient_window(self, ingredient_name, ingredient_image, drink_names, drink_images,
                                callb_search_by_name, callb_go_to_initial_window) -> None:
        # Creamos a ventana, e facemos que se conecte a señal "destroy". cando se emita a señal,
        # a funcion wind.close ejecutase
        self.close_current_window()
        ingredient_window = Gtk.ApplicationWindow(
            application=self.app,
            title="Ventana search_by ingredient"
        )
        self.app.add_window(ingredient_window)
        initialWindow.connect("destroy", lambda wind: wind.close())

        # Create UI with gtk widgets: GtkImage for ingredient_image and ingredient_name,
        # ScrolledWindow(container) with GtkImages and GtkLabel for drink_names and drink_images
