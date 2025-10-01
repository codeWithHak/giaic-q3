class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            print("Creaitng new instance")
            cls._instance = super().__new__(cls)
            
        return cls._instance
        
new = Singleton()
another = Singleton()
