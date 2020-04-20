import sys
import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gio
from gi.repository import Gtk

from src.window import AppWindow


class Application(Gtk.Application):

    def __init__(self, **kwargs) -> None:
        Gtk.Application.__init__(self, application_id='org.grapik.Designer', flags=Gio.ApplicationFlags.FLAGS_NONE, **kwargs)

        self.config = {
            'current_tool': 'select_tool',
            'artboards': [],
        }

    def do_activate(self) -> None:
        win = self.get_active_window()
        if not win:
            win = AppWindow(context=self)


if __name__ == "__main__":
    app = Application()
    sys.exit(app.run(sys.argv))
