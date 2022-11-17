from plyer import notification

import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title= " ***Take Rest*** ",
            message="rest is vital for better mental health,insreased concentration and memory,a healthier immune system,reduced stress and improve mood",
            app_icon="C:/Users/acer/try.ico",
            timeout=5)
        time.sleep(10)