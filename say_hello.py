from logging_module import get_logger

def say_hello_func(result_dir: str):
    logger = get_logger(__name__, result_dir=result_dir)
    logger.info("Start : say_hello()")
    logger.info("Hello !")
    logger.info("End : say_hello()")