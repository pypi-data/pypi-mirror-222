from hci_framework.utils import kafkalogs

import time
from datetime import datetime
import logging

while True:
    logging.warning(f'{datetime.now()}')
    time.sleep(1)
