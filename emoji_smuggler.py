#!/usr/bin/env python3
import base64

VS_START = 0xE0100  # Variation Selectors Supplement start


# ---- stable base64 charset ----
B64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def encode_payload(payload: str, carrier="🚀") -> str:
    b64 = base64.b64encode(payload.encode()).decode().rstrip("=")

    encoded = []
    for ch in b64:
        val = B64.index(ch)      # 0–63 stable reversible mapping
        encoded.append(chr(VS_START + val))

    return carrier + ''.join(encoded)


def decode_payload(smuggled: str) -> str:
    vs = smuggled[1:]   # remove carrier

    b64_chars = []
    for ch in vs:
        val = ord(ch) - VS_START
        if 0 <= val < 64:
            b64_chars.append(B64[val])

    # restore padding
    b64 = ''.join(b64_chars)
    b64 += "=" * ((4 - len(b64) % 4) % 4)

    return base64.b64decode(b64).decode()


# ---- RUN DIRECTLY ----
payload = "btc to the moon"

encoded = encode_payload(payload, "🚀")
decoded = decode_payload(encoded)

print("\nHidden message:", payload)

print("\nEmoji with invisible payload:")
print(encoded)

# show proof rocket really exists
print("\nVisible check:", encoded[0])

print("\nDecoded check:", decoded)