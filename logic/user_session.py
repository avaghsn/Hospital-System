class UserSession:
    """ tracks logged-in user to access to their national id """

    def __init__(self):
        self.current_user = None

    def login(self, national_id):
        self.current_user = national_id

    def logout(self):
        self.current_user = None

    def get_current_user(self):
        return self.current_user
