class CryptoAppError(Exception):
    """Base class to handle my errors in my application"""
    pass
class ConnectionsError(CryptoAppError):
    """Error when connecting to binance or websocket"""
    def __init__(self,message:str,symbol:str):
        super().__init__(message)
class DataError(CryptoAppError):
    def __init__(self,message:str,data:str):
        super().__init__(message)
    """Handle Errorswith my data format""" 
    pass
class ImageLoadError(CryptoAppError):
    def __init__(self,message:str,path:str):
        super().__init__(message)
    """Handle images errors""" 
    pass


