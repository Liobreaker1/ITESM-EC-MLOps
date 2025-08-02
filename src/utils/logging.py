from logging import getLogger, Logger, Formatter, StreamHandler, DEBUG


def setup_logging(identifier: str) -> Logger:
    logger = getLogger( identifier )
    logger.setLevel(DEBUG)

    # Create handler which logs even debug messages
    ch = StreamHandler()
    ch.setLevel(DEBUG)
    
    # Create formatter and add it to the handlers
    formatter = Formatter('%(asctime)s:%(name)s:%(module)s:%(levelname)s:%(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    
    return logger

