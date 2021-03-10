import os


environment = os.environ.get("EX_TRACKER_ENV")
if environment != 'prod':
    from .dev import *
else:
    from .prod import *
