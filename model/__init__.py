class AbstractUtilDTO:
    def __init__(self, dictionary = None):
        if dictionary != None:
            for k, v in dictionary.items():
                setattr(self, k, v)
                
                
    def __str__(self):
        var = ""
        for k, v in self.__dict__.items():
            var = var + k + "='" + str(getattr(self, k, v)) + "', "
        return "%s{%r}" % (self.__class__, var)