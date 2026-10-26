"""
This is for "What makes me mad" tool or plugin
"""

class UserInput:
    """
        classInput, takes user name and why as a whole

        input: Name, Why
    """
    def __init__(self, name, why = None):
        self.name = name
        self.why = why

    def user_name(self, name):
        """
            This is to rename user
        """
        self.name = name

    def user_why(self, why):
        """
            This is to set user's 'why'
        """
        self.name = why

def main():
    """
        Healthcheck for this add_tool1.py if run as is
    """
    print("Healthcheck")

    try:
        user = UserInput("health")
        print("user initialized successfully")
        user.user_why("Today, I am mad because I messed up my burger shift")
        print("userWhy working")
        user.user_name("I am not health anymore")
        print("userName working")
    except Exception as e:
        raise (f"Error found: {e}")

if __name__ == "__main__":
    main()
