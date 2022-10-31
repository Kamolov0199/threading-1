import threading
from familiya import *
from ism import *
from sharifi import *

t1 = threading.Thread(target=familiya)
t2 = threading.Thread(target=ism)
t3 = threading.Thread(target=sharifi)

t1.start()
t2.start()
t3.start()
