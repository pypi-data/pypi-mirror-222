def count_seconds(function):
    """Decorador para conocer el tiempo de ejecución

    """
    def wrapper(*args, **kwargs):
        import time
        
        start = time.time()
        response = function(*args, **kwargs)
        seconds = time.time() - start
        print(f">>> {seconds}")

        return response

    return wrapper
