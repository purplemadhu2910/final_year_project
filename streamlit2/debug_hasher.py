
import streamlit_authenticator as stauth
try:
    print("Attempt 1: Hasher(['password']).generate()")
    print(stauth.Hasher(['password']).generate())
except Exception as e:
    print(f"Attempt 1 failed: {e}")

try:
    print("Attempt 2: Hasher().hash('password')")
    # Some versions might behave differently
    h = stauth.Hasher()
    print(h.hash('password'))
except Exception as e:
    print(f"Attempt 2 failed: {e}")
