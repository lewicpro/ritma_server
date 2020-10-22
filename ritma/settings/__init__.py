from .settings import *

if DEBUG == True:
    from .local import *  # default for development only
else:
    from .prod import *  # default for production only
