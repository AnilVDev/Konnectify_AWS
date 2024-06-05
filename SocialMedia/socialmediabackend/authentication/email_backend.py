
import ssl
from django.core.mail.backends.smtp import EmailBackend

class CustomEmailBackend(EmailBackend):
    def open(self):
        if self.connection:
            return False
        try:
            self.connection = self.connection_class(self.host, self.port, **self.connection_kwargs)
            if self.use_tls or self.use_ssl:
                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                if self.use_tls:
                    self.connection.starttls(context=context)
                    self.connection.ehlo()
            self.connection.login(self.username, self.password)
            return True
        except Exception:
            if not self.fail_silently:
                raise