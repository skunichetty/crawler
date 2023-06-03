import threading
import unittest
from typing import List

from crawler.rw_lock import RWLock

NUM_THREADS = 10
NUM_ITERATIONS = 10000


class RWLockTests(unittest.TestCase):
    def test_basic(self):
        value = [0]
        lock = RWLock()

        def increment():
            for index in range(NUM_ITERATIONS):
                if index % 5 == 0:
                    lock.wlock()
                    value[0] += 1
                    lock.wrelease()
                else:
                    lock.rlock()
                    print(value[0])
                    lock.rrelease()

        pool: List[threading.Thread] = []
        for _ in range(NUM_THREADS):
            tdx = threading.Thread(target=increment)
            tdx.start()
            pool.append(tdx)

        for thread in pool:
            thread.join()

        assert value[0] == NUM_THREADS * (NUM_ITERATIONS // 5)
