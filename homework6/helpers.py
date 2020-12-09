import time


def wait_until(action, timeout=5):
    start_time_ = time.time()
    while time.time() - start_time_ <= timeout:
        try:
            action()
            break
        except:
            pass
