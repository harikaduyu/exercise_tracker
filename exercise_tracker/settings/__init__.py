import os


environment = os.environ.get("EX_TRACKER_ENV")
if environment == 'develop':
    print("DEVELOPMENT ENVIRONMENT")
    from .dev import *
else:
    print("PRODUCTIOn")
    from .prod import *
