import multiprocessing
import threading
import logging 
import time

# from src.master import runMaster
# from src.forwarder import mainForwarder
# from src.forwarder.run_forwarder import forwarderRunner
from Map.maps.serveLocation import app

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("backgroundWorker.py")

def main():
    p3 = multiprocessing.Process(target=app.run(), args= ("0.0.0.0",  5000, True,)).start()


if __name__ == "__main__":
    main()