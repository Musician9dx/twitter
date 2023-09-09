import logging as lg
import os 
import sys

lg.basicConfig(
    format='[%(asctime)s : %(levelname)s : %(module)s: %(message)s]',
    level=lg.INFO,
    handlers=[
        lg.FileHandler('D:/INeuron/twitter/log/logs.log'),
        lg.StreamHandler(sys.stdout)
    ]
)
logger=lg.getLogger('logger')