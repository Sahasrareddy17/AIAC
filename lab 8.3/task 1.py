import unittest

def is_valid_email(email):
    # Check for presence of '@' and '.'
    if '@' not in email or '.' not in email:
        return False
    # Must not start or end with '@' or '.'
    if email.startswith('@') or email.startswith('.') or email.endswith('@') or email.endswith('.'):
        return False
    # Only one '@' allowed
    if email.count('@') != 1:
        return False
    # '@' must not be adjacent to '.' at start or end
    if '.@' in email or '@.' in email:
        return False
    return True

class TestIsValidEmail(unittest.TestCase):
    def test_valid_emails(self):
        self.assertTrue(is_valid_email("user@example.com"))
        self.assertTrue(is_valid_email("john.doe@domain.co.uk"))
        self.assertTrue(is_valid_email("a.b@c.d"))
        self.assertTrue(is_valid_email("abc.def@mail.com"))

    def test_missing_at_or_dot(self):
        self.assertFalse(is_valid_email("userexample.com"))
        self.assertFalse(is_valid_email("user@examplecom"))
        self.assertFalse(is_valid_email("userexamplecom"))

    def test_starts_or_ends_with_special(self):
        self.assertFalse(is_valid_email("@user@example.com"))
        self.assertFalse(is_valid_email(".user@example.com"))
        self.assertFalse(is_valid_email("user@example.com@"))
        self.assertFalse(is_valid_email("user@example.com."))

    def test_multiple_at(self):
        self.assertFalse(is_valid_email("user@@example.com"))
        self.assertFalse(is_valid_email("user@ex@ample.com"))

    def test_adjacent_at_dot(self):
        self.assertFalse(is_valid_email("user@.example.com"))
        self.assertFalse(is_valid_email("user.@example.com"))
        self.assertFalse(is_valid_email("user@exam.ple@com"))

    def test_empty_string(self):
        self.assertFalse(is_valid_email(""))

if __name__ == "__main__":
    unittest.main()