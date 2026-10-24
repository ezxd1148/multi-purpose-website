# This is for "What makes me mad" tool or plugin

class userInput:
    def __init__(self, name, why = None):
        self.name = name
        self.why = why
    
    def userName(self, name):
        """
            This is to rename user     
        """
        self.name = name

    def userWhy(self, why):
        """
            This is to set user's 'why'
        """
        self.name = why

def main():
    print("Healthcheck")

    try:
        user = userInput("health")
        print("user initialized successfully")
        user.userWhy("Today, I am mad because I messed up my burger shift")
        print("userWhy working")
        user.userName("I am not health anymore")
        print("userName working")
    except:
        raise Exception("Some error idk")

if __name__ == "__main__":
    main()
