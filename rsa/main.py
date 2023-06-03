from algo import generate_keys, rsa_encrypt, rsa_decrypt


initial_text = input("-> Enter your text: ")

keys = generate_keys(13)
encrypted_text = rsa_encrypt(keys[0], initial_text)
decrypted_text = rsa_decrypt(keys[1], encrypted_text)

print("STATS: ")
print("* keys ", keys)
print("* encrypted text: ", encrypted_text)
print("* decoded text: ", decrypted_text)
