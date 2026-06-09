class User:
    # атрибуты класса
    user_count = 0
    default_password = "123456789"

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.role = "user"
        self.password = User.default_password
        User.user_count += 1

    @classmethod
    def get_user_count(cls):
        return cls.user_count

    @classmethod
    def create_admin(cls, name, phone):
        user = cls(name, phone)
        user.role = "admin"
        user.password = "qwerty123"
        return user

    @staticmethod
    def validate_password(pswd):
        if len(pswd) < 8:
            return False
        return True

    def change_password(self, new_password):
        if not User.validate_password(new_password):
            raise ValueError("Пароль короткий")
        self.password = new_password

print(f"Всего пользователей: {User.user_count}")
user1 = User("Igor", "996555000000")
print(user1.password)
print(f"Всего пользователей: {User.user_count}")
admin1 = User.create_admin("Radomir", "996555000001")
print(admin1.password, admin1.role)
print(User.get_user_count())
print(f"Всего пользователей: {User.user_count}")
user1.change_password("1weqreqwewrwerwqerqew")
print(user1.password)
print(User.validate_password("fsd"))