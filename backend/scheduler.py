
import time
import random
from utils.scraper_abparks import check_ab_parks
from utils.scraper_pcparks import check_pc_parks

def job():
    print("Checking Alberta Parks...")
    check_ab_parks("https://reserve.albertaparks.ca/")

    interval = random.uniform(2, 5)
    print(f"Sleeping for {interval:.2f} seconds between checks...")
    time.sleep(interval)

    print("Checking Parks Canada...")
    check_pc_parks("https://reservation.pc.gc.ca/")

def schedule_random_job():
    while True:
        interval = random.uniform(5, 10)
        print(f"Next cycle in {interval:.2f} seconds")
        time.sleep(interval)
        job()

if __name__ == "__main__":
    schedule_random_job()
