import hashlib
import hmac
from time import time


class SignatureVerifier:
    def __init__(self, signing_key: str):
        self.signing_key = signing_key
        self.secret_version = "s0="
        self.max_delay = 60 * 5

    def is_valid(
            self,
            body_or_null: str | None,
            timestamp_or_null: str | None,
            signature_or_null: str | None,
    ) -> bool:
        if timestamp_or_null is None or signature_or_null is None or body_or_null is None:
            return False

        if abs(time() - int(timestamp_or_null)) > self.max_delay:
            return False

        calculated_signature = self.generate_signature(timestamp=timestamp_or_null, body=body_or_null)
        return hmac.compare_digest(calculated_signature, signature_or_null)

    def generate_signature(self, body: str, timestamp: str) -> str:
        base_string = "swit:{}:{}".format(timestamp, body)
        signature = hmac.new(self.signing_key.encode(), base_string.encode(), hashlib.sha256)
        return self.secret_version + signature.hexdigest()
