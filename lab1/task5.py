import time


def time_decorator(task):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = task(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения: {execution_time} секунд")
        return result
    return wrapper


