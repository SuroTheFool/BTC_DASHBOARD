class CryptoAppError(Exception):
    """Base class to handle my errors in my application"""
    pass
class ConnectionsError(CryptoAppError):
    """Error when connecting to binance or websocket"""
    pass
class DataError(CryptoAppError):
    """Handle Errorswith my data format""" 
    pass

