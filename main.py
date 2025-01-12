import logging
import time
import schedule


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',
)


def job():
    print("Executing job")
    logging.info('Job executed')

def main():
    schedule.every(4).hours.do(job)

    schedule.run_all()

    while True:
        schedule.run_pending()
        time.sleep(1)
        print("Waiting...")


if __name__ == "__main__":
    main()