from wf_blog.heloer import encrypt

class UserAdmin(object):
    def __init__(self, username, request):
        self.settings = request.registry.settings
        self.collection = request.mongodb['user_user']
        self.__get_stored_encrypt(username)

    def __get_stored_encrypt(self, username):
        record = self.collection.find_one({'username': username})
        if record:
            self.stored_encrypt = record['password']
        else:
            self.stored_encrypt = None

    def validate_user(self, password):
        """验证用户"""
        if self.stored_encrypt:
            if self.stored_encrypt == encrypt(password):
                return True
        return False
