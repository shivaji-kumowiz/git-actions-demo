import logging


def fun():
    my_logger.info("in function fun");
    my_logger.info("this is info");
    my_logger.info("this is another info");
    my_logger.error("this is an error");
    my_logger.error("this is an another error");



def get_logger(
        LOG_FORMAT     = '%(levelname)-1s %(message)s',
        LOG_NAME       = '',
        LOG_FILE_INFO  = 'out.log',
        LOG_FILE_ERROR = 'out.err'):

    log           = logging.getLogger(LOG_NAME)
    log_formatter = logging.Formatter(LOG_FORMAT)
    # comment this to suppress console output
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(log_formatter)
    log.addHandler(stream_handler)
    file_handler_info = logging.FileHandler(LOG_FILE_INFO, mode='w')
    file_handler_info.setFormatter(log_formatter)
    file_handler_info.setLevel(logging.INFO)
    log.addHandler(file_handler_info)
    file_handler_error = logging.FileHandler(LOG_FILE_ERROR, mode='w')
    file_handler_error.setFormatter(log_formatter)
    file_handler_error.setLevel(logging.ERROR)
    log.addHandler(file_handler_error)
    log.setLevel(logging.INFO)

    return log


if __name__ == "__main__":
    my_logger = get_logger()
    my_logger.info("\n\n**********\n\n")
    my_logger.info("routes:")

