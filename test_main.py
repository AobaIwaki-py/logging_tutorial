from logging_module import get_logger
from logging import Logger
from say_hello import say_hello_func

def main_func(logger: Logger, result_dir: str):
    logger.info(f"Start : main()")
    say_hello_func(result_dir)
    main_hello_func(logger)
    logger.info(f"End : main()")
    
def main_hello_func(logger: Logger):
    logger.info(f"Start : main()")
    logger.info(f"Hello !")
    logger.info(f"End : main()")
    
if __name__=='__main__':
    result_dir = None
    logger = get_logger(__name__, result_dir=result_dir)
    main_func(logger, result_dir)