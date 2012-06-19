import logging
import sys

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,format=sys.argv[0] + " : %(levelname)s: %(message)s")

r=range(100)
t='I will not talk in class'

for i in r:
    logger.info(t)
