import time
import sched

def schedule_function(schedule_time, function, *args):
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(schedule_time, 1, function, argument=args)
    print(f'current time: {time.asctime(time.localtime())}')
    print(f'{function.__name__}() scheduled for {time.asctime(time.localtime(schedule_time))}')
    s.run()

if __name__ == '__main__':
  schedule_function(time.time() + 5, print, "Hello World!\n")
  schedule_function(time.time() + 10, print, "Hello!","This is a test")