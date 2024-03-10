import unittest


class EmailSender:
    def send_email(self, to, subject, body):
        # Code to send email
        return True


def is_network_available():
    # Code to check if network is available 
    return True


class TestEmailSender(unittest.TestCase):

    @unittest.skipUnless(is_network_available(), "Network unavailable")
    def test_send_email(self):
        self.assertTrue(EmailSender().send_email(1, 2, 3))


if __name__ == "__main__":
    unittest.main()
