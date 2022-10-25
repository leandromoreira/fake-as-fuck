import random
import time

def delay(min_ms=600, max_ms=2200):
    time.sleep(random.randint(min_ms,max_ms)/1000) # -- between 600ms to 2.2s

def average_people_typing():
    delay(60,200)

def average_people_waiting_for_click():
    delay(300,1220)
