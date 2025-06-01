from lib2to3.pgen2.tokenize import generate_tokens
from sqlite3 import Timestamp
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            text_type(user.pk) + text_type(Timestamp)
        )

generate_token = TokenGenerator()