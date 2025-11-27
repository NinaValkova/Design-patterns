# decorators are useful for performing something around a function
import time


# new function which is a wrapper of the original
def time_it(func):
    # wrapper - calls the function and returns result of that function
    def wrapper():
        start = time.time()
        result = func()
        end=time.time()
        print(f'{func.__name__} took {int((end-start)*1000)}ms')
        return result
    return wrapper


@time_it
def some_op():
    print('Starting op')
    time.sleep(1)
    print('We are done')
    return 123        

if __name__ == '__main__':
    # time_it(some_op)() -  if there was not @time_it
    some_op()
