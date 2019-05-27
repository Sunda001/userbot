import logging.config


def add_color(string: str, color, just=0):
    string = string.rjust(just)
    return f'\033[{color}m{string}\033[0m'


def configure_logging(level='DEBUG', root_level='INFO'):
    # setup logging level display
    levels = [
        (logging.DEBUG, add_color('DEBUG', '36', 5)),
        (logging.INFO, add_color('INFO', '32', 5)),
        (logging.WARNING, add_color('WARN', '33', 5)),
        (logging.ERROR, add_color('ERROR', '31', 5)),
        (logging.CRITICAL, add_color('CRIT', '7;31;31', 5)),
    ]
    for lvl, name in levels:
        logging.addLevelName(lvl, name)

    m = add_color(">", '36')

    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': f'[%(asctime)s] %(levelname)s %(name)20s:%(lineno)-3d {m} %(message)s',
                'datefmt': "%Y/%m/%d %H:%M:%S"
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            },
        },
        'loggers': {
            'handlers': {
                'handlers': ['console'],
                'level': level,
                'propagate': False,
            },
            'misc': {
                'handlers': ['console'],
                'level': level,
                'propagate': False,
            },
            'manager': {
                'handlers': ['console'],
                'level': level,
                'propagate': False,
            },
            'persistence': {
                'handlers': ['console'],
                'level': level,
                'propagate': False,
            },
            '__main__': {
                'handlers': ['console'],
                'level': level,
                'propagate': False,
            },
            '': {
                'handlers': ['console'],
                'level': root_level,
                'propagate': False,
            },
        }
    })