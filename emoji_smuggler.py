#!/usr/bin/env python3
import base64

VS_START = 0xE0100
B64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

# invisible separator that fixes Android rendering
SAFE_SEPARATOR = "\u200C"


def encode_payload(payload: str, carrier="🚀"):
    b64 = base64.b64encode(payload.encode()).decode().rstrip("=")

    encoded = []
    for ch in b64:
        encoded.append(chr(VS_START + B64.index(ch)))

    # separator AFTER emoji keeps rocket visible everywhere
    return carrier + SAFE_SEPARATOR + ''.join(encoded)


def decode_payload(sm