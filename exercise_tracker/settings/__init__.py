import os


environment = os.environ.get("EX_TRACKER_ENV")
if environment != 'prod':
    print("DEVELOPMENT ENVIRONMENT")
    from .dev import *
else:
    print("PRODUCTION")
    from .prod import *
