from hci_framework.radiant.server import FrameworkAPI
from browser import html

# Material 3
# https://m3.material.io/develop/web
import material_3 as md


########################################################################
class BareMinimum(FrameworkAPI):

    # ----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)
        # self.add_css_file('css/theme.css')

        # md_list = md.list()
        # self.body <= md_list
        # for i, service in enumerate(self.MyClass.services()):
            # list_item = md.list_item(headline=service, active=(i == 0))
            # md_list <= list_item

        button = md.text_button('Logging')
        button.bind('click', self.send_log)
        self.body <= button

        self.body <= html.PRE(self.swarm.get_join_command())

    # ----------------------------------------------------------------------
    def send_log(self, evt):
        """"""
        print('logging message')
        self.logging.warning('logging message')


if __name__ == '__main__':
    BareMinimum()
