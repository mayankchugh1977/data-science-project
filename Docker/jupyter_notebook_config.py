import os
from IPython.lib import passwd

c.NotebookApp.ip = '*'
c.NotebookApp.port = int(os.getenv('PORT', 8888))
c.NotebookApp.open_browser = False
c.MultiKernelManager.default_kernel_name = 'python2'
c.NotebookApp.token = ''
c.NotebookApp.password = ''


# sets a password if PASSWORD is set in the environment
# if 'PASSWORD' in os.environ:
#   password = os.environ['PASSWORD']
#   if password:
#     c.NotebookApp.password = passwd(password)
#   else:
#     c.NotebookApp.password = ''
#     c.NotebookApp.token = ''
#   del os.environ['PASSWORD']
