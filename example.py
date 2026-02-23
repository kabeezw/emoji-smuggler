# Example usage of encode_payload and decode_payload functions

from emoji_smuggler import encode_payload, decode_payload

# Example data to encode.
data = "Hello, World!"

# Encoding the data.
encoded_data = encode_payload(data)
print(f"Encoded Data: {encoded_data}")

# Decoding the data back.
decoded_data = decode_payload(encoded_data)
print(f"Decoded Data: {decoded_data}")

# Ensure the decoded data matches the original data.
assert decoded_data == data, "Decoded data does not match the original data!"