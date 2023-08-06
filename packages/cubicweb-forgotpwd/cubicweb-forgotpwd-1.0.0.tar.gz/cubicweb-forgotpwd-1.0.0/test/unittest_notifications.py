from cubicweb_web.devtools.testlib import WebCWTC
from logilab.common.testlib import unittest_main

from cubicweb.devtools.testlib import MAILBOX


class ForgotTC(WebCWTC):
    def setup_database(self):
        with self.admin_access.repo_cnx() as cnx:
            for index in range(4):
                user = self.create_user(cnx, f"test_user{index}")
                cnx.create_entity(
                    "EmailAddress",
                    address=f"test_user{index}@logilab.fr",
                    reverse_use_email=user,
                )
            cnx.commit()

    def test_reset_password(self):
        with self.admin_access.cnx() as cnx:
            count = cnx.execute("Any COUNT(X) WHERE X is Fpasswd")[0][0]
        assert count == 0
        MAILBOX[:] = []
        self.assertEqual(len(MAILBOX), 0)
        self.config.global_set_option("base-url", "http://babar.com/")
        with self.repo.internal_cnx() as cnx:
            cnx.call_service("forgotpwd_send_email", use_email="test_user1@logilab.fr")
            cnx.commit()
        with self.admin_access.cnx() as cnx:
            count = cnx.execute("Any COUNT(X) WHERE X is Fpasswd")[0][0]
        assert count == 1
        self.assertEqual(len(MAILBOX), 1)
        self.assertIn("http://babar.com", MAILBOX[0].content)


if __name__ == "__main__":
    unittest_main()
