import logging
logging.basicConfig(filename = 'example.log',level = logging.INFO)
logger = logging.getLogger(_name_)
logger.info("start reading database")
records = {"john":45,"tim":34}
logger.debug("Records:%s",records)
logger.info("updating records...")
logger.info("finish updating records")
