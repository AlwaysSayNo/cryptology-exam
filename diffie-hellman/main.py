from algo import diffie_hellman

print("Diffie-Hellman algorithm")

while True:
    secret_1, secret_2 = diffie_hellman()

    if secret_1 == secret_2:
        print("Success: keys are successfully exchanged")
        print(f"Secret key: {secret_2}")
        break
    else:
        print("Error: keys haven't been exchanged successfully")
        print(f"User_1 secret key: {secret_1}")
        print(f"User_2 secret key: {secret_2}")

    print("TRY ONE MORE TIME")
