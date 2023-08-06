import hashlib
import hmac
from time import time


class SignatureVerifier:
    def __init__(self, signing_secret: str):
        self.signing_secret = signing_secret
        self.secret_version = "s0="
        self.max_delay = 60 * 5

    def is_valid(
            self,
            body: str,
            timestamp: str,
            signature: str,
    ) -> bool:
        if timestamp is None or signature is None or body is None:
            return False

        if abs(time() - int(timestamp)) > self.max_delay:
            return False

        calculated_signature = self.generate_signature(timestamp=timestamp, body=body)
        return hmac.compare_digest(calculated_signature, signature)

    def generate_signature(self, body: str, timestamp: str) -> str:
        base_string = "swit:{}:{}".format(timestamp, body)
        signature = hmac.new(self.signing_secret.encode(), base_string.encode(), hashlib.sha256)
        return self.secret_version + signature.hexdigest()
