# from django.http import HttpResponse

# class HRMiddlewareOne:
#     def __init__(self,get_response):
#         self.get_response=get_response
        
#         print("one time run HRMiddlewareOne")

#     def __call__(self,request):
#         print("before run HRMiddlewareOne")
#         response=self.get_response(request)
#         print("after run HRMiddlewareOne")
#         return  response
# class HRMiddlewareTwo:
#     def __init__(self,get_response):
#         self.get_response=get_response
        
#         print("one time run HRMiddlewareTwo")

#     def __call__(self,request):
#         print("before run HRMiddlewareTwo")
#         response=self.get_response(request)
#         print("after run HRMiddlewareTwo")
#         return  response 

# class HRMiddlewarethree:
#     def __init__(self,get_response):
#         self.get_response=get_response
        
#         print("one time run HRMiddlewarethree")

#     def __call__(self,request):
#         print("before run HRMiddlewarethree")
#         response=self.get_response(request)
#         print("after run HRMiddlewarethree")
#         return  response 


  

