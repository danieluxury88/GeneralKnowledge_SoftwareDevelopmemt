class ApplicationState:
    instance = None

    def __init__(self):
        self.isLoggedIn = False


    @staticmethod
    def getAppState():
        if not ApplicationState.instance:
            ApplicationState.instance = ApplicationState()
            print("Create new App State instance")
        return ApplicationState.instance
    
appsState1 = ApplicationState.getAppState()
print(appsState1.isLoggedIn)

appsState2 = ApplicationState.getAppState()
appsState1.isLoggedIn = True


print(appsState1.isLoggedIn)
print(appsState2.isLoggedIn)