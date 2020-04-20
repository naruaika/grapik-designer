import os
import gi

gi.require_version('Gdk', '3.0')
gi.require_version('Gtk', '3.0')

from gi.repository import Gdk
from gi.repository import Gio
from gi.repository import Gtk

from .canvas import Canvas


class AppWindow():

    def __init__(self, context: Gtk.Application) -> None:
        self.context = context

        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.builder = Gtk.Builder.new_from_file(os.path.join(script_dir, '../data/ui/window.glade'))
        self.builder.connect_signals(self)

        self.main_window = self.builder.get_object('main_window')
        self.main_window.set_application(context)
        self.main_window.show()

        self.setup_ui()

    def setup_ui(self) -> None:

        def setup_win() -> None:
            self.main_window.maximize()

        def setup_css() -> None:
            style_provider = Gtk.CssProvider()
            script_dir = os.path.dirname(os.path.abspath(__file__))
            style_provider.load_from_file(Gio.File.parse_name(os.path.join(script_dir, '../data/css/main.css')))
            Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), style_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        def setup_uis() -> None:
            design_page = self.builder.get_object('design_page')
            design_page.add(Canvas(context=self.context))

        setup_win()
        setup_css()
        setup_uis()

    def on_change_tool(self, widget: Gtk.Button) -> None:
        if not widget.get_active():
            return

        self.context.config['current_tool'] = widget.get_name()

        win = self.builder.get_object('design_page').get_window()
        if widget.get_name() != 'select_tool':
            win.set_cursor(Gdk.Cursor.new_from_name(win.get_display(), 'crosshair'))
        else:
            win.set_cursor(Gdk.Cursor.new_from_name(win.get_display(), 'default'))
