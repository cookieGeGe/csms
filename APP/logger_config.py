import logging.config
from sys import stdout, stderr
from os import makedirs
from os.path import exists, join

from APP.settings import BASE_DIR

LOG_DIR = join(BASE_DIR, 'log')
if not exists(LOG_DIR):
    # 新建目录
    makedirs(LOG_DIR)

# 日志配置
LOGGING_CONFIG_LOCAL = dict(
    version=1,
    disable_existing_loggers=False,

    loggers={
        "root": {  # 根日志-----日志对象-----记录异常以及系统运行状态
            "level": "INFO",  # 等级
            "handlers": ["console", "root_file"],  # 使用的控制类
        },
        "error": {  # 错误日志-----日志对象-----记录严重框架错误
            "level": "INFO",  # 等级
            "handlers": ["error_console", "error_file"],  # 使用的控制类
            "propagate": True,
            "qualname": "error"
        },
        "access": {  # 日志流水日志-----日志对象-----记录访问日志流水
            "level": "INFO",  # 等级
            "handlers": ["access_console", "access_file"],  # 使用的控制类
            "propagate": True,
            "qualname": "access"
        }
    },
    handlers={
        "console": {  # 根日志-----控制台-----记录异常以及系统运行状态
            "class": "logging.StreamHandler",  # 控制类
            "formatter": "generic",  # 输出内容格式
            "stream": stdout,  # 标准输出
        },
        "error_console": {  # 错误日志-----控制台-----记录严重框架错误
            "class": "logging.StreamHandler",  # 控制类
            "formatter": "generic",  # 输出内容格式
            "stream": stderr,  # 错误输出
        },
        "access_console": {  # 日志流水日志-----控制台-----记录访问日志流水
            "class": "logging.StreamHandler",  # 控制类
            "formatter": "access",  # 输出内容格式
            "stream": stdout,  # 标准输出
        },
        "root_file": {  # 根日志-----文件-----记录异常以及系统运行状态
            "class": "logging.handlers.TimedRotatingFileHandler",  # 控制类
            "level": "INFO",  # 等级
            "formatter": "generic",  # 输出内容格式
            "filename": LOG_DIR + 'root_log.txt',  # 文件名称前缀
            "when": "D",  # 以天数作区分
            "interval": 1,  # 一天一个
            "backupCount": 30,  # 最多30个
            "encoding": "utf8",  # 默认UTF-8编码
        },
        "access_file": {  # 日志流水日志-----文件-----记录访问日志流水
            "class": "logging.handlers.TimedRotatingFileHandler",  # 控制类
            "level": "INFO",  # 等级
            "formatter": "access",  # 输出内容格式
            "filename": LOG_DIR + 'access_log.txt',  # 文件名称前缀
            "when": "D",  # 以天数作区分
            "interval": 1,  # 一天一个
            "backupCount": 30,  # 最多30个
            "encoding": "utf8",  # 默认UTF-8编码
        },
        "error_file": {  # 错误日志-----文件-----记录严重框架错误
            "class": "logging.handlers.TimedRotatingFileHandler",  # 控制类
            "level": "ERROR",  # 等级
            "formatter": "generic",  # 输出内容格式
            "filename": LOG_DIR + 'exception_log.txt',  # 文件名称前缀
            "when": "D",  # 以天数作区分
            "interval": 30,  # 三十天一个
            "backupCount": 15,  # 最多15个
            "encoding": "utf8",  # 默认UTF-8编码
        }
    },
    formatters={
        "generic": {
            "format": "[%(asctime)s] - %(filename)s - %(funcName)s - %(lineno)d - %(levelname)s : %(message)s",
            "datefmt": "[%Y-%m-%d %H:%M:%S %z]",
            "class": "logging.Formatter"
        },
        "access": {
            "format": "%(asctime)s - (%(name)s)[%(levelname)s][%(host)s]: " +
                      "%(request)s %(message)s %(status)d %(byte)d",
            "datefmt": "[%Y-%m-%d %H:%M:%S %z]",
            "class": "logging.Formatter"
        },
    }
)

logging.config.dictConfig(LOGGING_CONFIG_LOCAL)
logger = logging.getLogger('root')
error_logger = logging.getLogger('error')
access_logger = logging.getLogger('access')
