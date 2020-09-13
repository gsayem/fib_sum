import platform
import re
import socket
import uuid

import psutil
from injector import inject


# Health service
class HealthService:
    @inject
    def __init__(self):
        print("Health Service")

    # Get system health
    def get_system_health(self):
        try:
            info = {'platform': platform.system(), 'platform-release': platform.release(),
                    'platform-version': platform.version(), 'architecture': platform.machine(),
                    'hostname': socket.gethostname(), 'ip-address': socket.gethostbyname(socket.gethostname()),
                    'mac-address': ':'.join(re.findall('..', '%012x' % uuid.getnode())),
                    'processor': platform.processor(),
                    'ram': str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " GB"}
            return info
        except Exception as e:
            print(e)
        return "{System health information can't retrieve}"
