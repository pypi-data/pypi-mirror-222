def count_seconds(function):
    """Decorador para conocer el tiempo de ejecución

    """
    def wrapper():
        import time
        
        start = time.time()
        response = function()
        seconds = time.time() - start
        print(f">>> {seconds}")

        return response

    return wrapper
