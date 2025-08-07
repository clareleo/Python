import logging


class Debug:
    def debug_ming(self):
        logging.basicConfig(
            format='%(levelname)s (%(asctime)s): (Line: %(lineno)d [%(filename)s])',
            datefmt='%y/%m/%d %I:%M:%S %p',
            level=logging.DEBUG
        )
        logging.info("Oh yeah!There's nothing wrong with your program.")
        logging.warning("Oh no!")


if __name__ == "__main__":
    o = Debug()
    o.debug_ming()
