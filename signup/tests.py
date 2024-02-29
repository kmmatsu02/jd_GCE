from django.test import TestCase, Client
from .models import User

c = Client()

class UserModelTests(TestCase):
    email = "admin@gmail.com"
    password = "admin_"

    def setUp(self):
        # 一時的にユーザーを作成する
        User.objects._create_user(self.email, self.password)

    def test_user_login(self):
        resp = c.login(email=self.email, password=self.password)
        print("resp:", resp)
        self.assertIs(resp, True)

    def test_validate_email(self):
        domain = "@gmail.com"
        n = 255 - len(domain)
        email = "".join([
            "a" for _ in range(n)
        ]) + domain
        "aaa...@gmail.com"
        user = User(email=email)
        """
        user.validate_email() => True, True == True
        user.validate_email() => False, True == False
        """
        self.assertIs(user.validate_email(), True, "this is errors")

    def test_validate_email_err(self):
        domain = "@gmail.com"
        n = 256 - len(domain)
        email = "".join([
            "a" for _ in range(n)
        ]) + domain
        "aaa...@gmail.com"
        user = User(email=email)
        """
        user.validate_email() => True, True == True
        user.validate_email() => False, True == False
        """
        self.assertIs(user.validate_email(), False, "this is errors")