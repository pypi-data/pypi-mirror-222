from radiant.framework.server import PythonHandler
from hci_framework.utils import kafkalogs
import logging as logging_orig


########################################################################
class logging(PythonHandler):
    """"""

    # ----------------------------------------------------------------------
    def services(self):
        """"""
        return admin.services

    # ----------------------------------------------------------------------
    def warning(self, msg):
        """"""
        return logging_orig.warning(msg)
