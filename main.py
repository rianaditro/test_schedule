from log_task import logger
import time
import schedule


def job(logger=logger):
    logger.info("This is a log message")
    print("This is app is running")

def main(logger=logger):
    schedule.every(4).hours.do(job, logger=logger)

    schedule.run_all()

    while True:
        schedule.run_pending()
        time.sleep(1)
        print("Waiting...")


if __name__ == "__main__":
    logger = logger()
    job(logger)
    # main(logger)