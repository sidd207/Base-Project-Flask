import functools

def parse_response(status=400, success=200, func=None):
   if func is None:
       return functools.partial(parse_response, status, success)

   @functools.wraps(func)
   def wrapper(*args, **kwargs):
       status_code = status
       response = func(*args, **kwargs)
       if response.success:
           status_code = success
       return response.to_dict(), status_code
   return wrapper

