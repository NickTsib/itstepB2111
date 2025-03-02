import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="logs_p8_1.log",
                    filemode='a',
                    format="We have next logging message: %(asctime)s%(levelname)s - %(message)s")

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
