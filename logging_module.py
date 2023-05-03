from logging import getLogger, StreamHandler, DEBUG, Logger, INFO, Formatter, FileHandler
import os

def get_logger(logger_name:str=None, result_dir: str = None, log_file_name: str = "default",
               stdout_log_level: str = "INFO", fileout_log_level: str = "DEBUG",) -> Logger:
    '''loggerを作成する関数
        Args:
            logger_name (str): Name of logger.
            result_dir (str, optional): Out path of log file.
            log_file_name (str, optional): Name of log file. 
            stdout_log_level (str, optional): Log Level for stdout.
            fileout_log_level (str, optional): Log Level for fileout.
        Returns:
            logger (Logger): 設定済みのlogger
        Usage:
        >>> # 以下を実行するのは、ファイルにつき一度だけにしてください。
        >>> cd_logger = get_logger(__name__) # この関数が含まれるファイルと同じ階層にlogファイルが作成される
        >>> cd_logger.info('INFOMATOIN')
        >>> # 以下の場合、この関数が含まれるファイルと同じ階層のlogディレクトリ直下にtest.logが作成される
        >>> logger = get_logger(__name__, result_dir='log', log_file_name='test')
        >>> logger.debug('DEBUG')
        >>> # 以下のようにクラス名を付けることも可能
        >>> # この場合、クラスごとに複数回loggerを定義してもいい
        >>> class_logger = get_logger(__name__+'.'+__class__.__name__)
        >>> class_logger.warning('WARNING')
    '''
    
    # Set Log Format
    logger = getLogger(logger_name)
    logger.setLevel(DEBUG)
    
    formatter = Formatter('%(asctime)s %(name)s:%(lineno)s %(funcName)s [%(levelname)s]: %(message)s')  # ログのフォーマット
    
    # Logging Setting for stdout
    handler = StreamHandler()
    handler.setLevel(stdout_log_level.upper())
    handler.setFormatter(formatter)  # Set Format
    logger.addHandler(handler)
    
    # Logging Setting for fileout
    if log_file_name.lower() == "default":
        log_file_name = os.path.basename(__import__('__main__').__file__).split('.')[0]
    if result_dir==None:
        result_dir = '.'
    file_handler = FileHandler(f'{result_dir}/{log_file_name}.log', 'a')  # Set Log File

    file_handler.setLevel(fileout_log_level.upper())  # Log Level for fileout
    file_handler.setFormatter(formatter)  # Set Format
    logger.addHandler(file_handler)
    
    # Not Propagate
    logger.propagate = False
    
    return logger