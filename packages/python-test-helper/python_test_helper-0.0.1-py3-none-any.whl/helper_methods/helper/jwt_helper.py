from time import sleep

import jwt


def sleep_until_access_token_ready(access_token, max_attempts=30, sleep_interval=1):
    attempt = 0

    while attempt < max_attempts:
        try:
            jwt.decode(access_token, options={"verify_signature": False})
            break
        except jwt.exceptions.ImmatureSignatureError:
            sleep(sleep_interval)
            attempt += 1
