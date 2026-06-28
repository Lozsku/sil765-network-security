# Assignment 2 — Evaluating Cryptographic Primitives

## Problem

The handout (`2023_24_SIL765_Assignment_2.pdf`) asked me to prototype a set of
encryption and authentication primitives and measure three costs for each:

- **Computational** — execution time, in milliseconds.
- **Communication** — packet length, in bits.
- **Storage** — key length, in bits.

Then discuss the pros and cons of each. The required primitives were:

- Encryption: AES-128-CBC, AES-128-CTR, RSA-2048 (encrypting a 128-bit key).
- Authentication: AES-128-CMAC, SHA3-256-HMAC, RSA-2048 + SHA3-256 signature,
  ECDSA-256 + SHA3-256 signature.
- Authenticated encryption: AES-128-GCM (encrypt+tag, decrypt+verify).

## What I did

I implemented the `ExecuteCrypto` class in `SIL_ASS2/script/execute_crypto.py`
using Python's `cryptography` (hazmat) library. The pieces:

- `generate_keys()` — a 16-byte symmetric key, two RSA-2048 key pairs
  (sender and receiver), and one ECC SECP256R1 key pair, all PEM-encoded.
- `generate_nonces()` — random 16-byte nonces per algorithm (12 bytes for GCM).
- `encrypt` / `decrypt` — AES-CBC (PKCS7 padding), AES-CTR, and RSA-OAEP
  (SHA-256).
- `generate_auth_tag` / `verify_auth_tag` — AES-CMAC (implemented with
  HMAC-SHA256), HMAC-SHA3-256, RSA-PSS signature over SHA3-256, and ECDSA over a
  prehashed SHA3-256 digest.
- `encrypt_generate_auth` / `decrypt_verify_auth` — AES-GCM AEAD.
- Helper timing/sizing functions `cal_packet_length`, `cal_packet_len2`, and
  `cal_key_length`. Every operation is wrapped in `time.time()` deltas printed in
  ms, and ciphertexts/signatures are base64-encoded for transport.

## Results (from `sil_ass2_report.pdf`)

Single-run measurements:

| Algorithm | Exec. time (ms) | Packet length (bits) | Key length (bits) |
|-----------|-----------------|----------------------|-------------------|
| AES-128-CBC-ENC | 0.16117 | 1152 | 128 |
| AES-128-CBC-DEC | 0.08202 | | |
| AES-128-CTR-ENC | 0.07200 | 1040 | 128 |
| AES-128-CTR-DEC | 0.03743 | | |
| RSA-2048-ENC | 1.21069 | 2176 | 13632 |
| RSA-2048-DEC | 36.66472 | | |
| AES-128-CMAC-GEN | 0.06008 | 1296 | 128 |
| AES-128-CMAC-VRF | 0.03362 | | |
| SHA3-256-HMAC-GEN | 0.03362 | 1296 | 128 |
| SHA3-256-HMAC-VRF | 0.02098 | | |
| RSA-2048-SHA3-256-SIG-GEN | 37.29677 | 3792 | 3608 |
| RSA-2048-SHA3-256-SIG-VRF | 0.97823 | | |
| ECDSA-256-SHA3-256-SIG-GEN | 1.01280 | 1808 | 1424 |
| ECDSA-256-SHA3-256-SIG-VRF | 0.97013 | | |
| AES-128-GCM-GEN | 0.10180 | 142 | 128 |
| AES-128-GCM-VRF | 0.04554 | | |

Main takeaways: symmetric primitives are roughly 1–2 orders of magnitude faster
than the asymmetric ones; **RSA private-key operations dominate the cost**
(decrypt ~37 ms, sign ~37 ms) while RSA verify is cheap; ECDSA sign and verify
are balanced (~1 ms each) and far cheaper to store than RSA; AES-CTR beats
AES-CBC (no padding, smaller packet); and AES-GCM gives confidentiality plus
integrity in a single pass. The report also lists per-algorithm pros/cons
(padding-oracle risk in CBC, length-extension caveats, RSA key-size limits, etc.).

## Key files

- `SIL_ASS2/script/execute_crypto.py` — my final implementation.
- `SIL_ASS2/script/readme.pdf` — the bundled A2 report.
- `sil_ass2_report.pdf` — root-of-this-folder copy of the A2 report (timing tables).
- `sil_notes.docx` — my working notes (Word document).
- `SIL_ASS2/script/original_plaintext.txt` — the input plaintext
  ("Paris 2024 will see a new vision of Olympism in action…").
- `SIL_ASS2/examples/` — sample keys, ciphertexts, and auth tags.
- `SIL_ASS2/script_v1..v5, script_time*, script_failed.zip` — my iterative dev
  snapshots (see `SIL_ASS2/README.md` for the order).
- `handout-starter/` and `handout-starter.zip` — the **empty handout skeleton**
  (the starter `execute_crypto.py` with unfilled method bodies), kept for
  reference. This is the provided template, not my solution.
- `2023_24_SIL765_Assignment_2.pdf` — the course handout (also kept inside
  `SIL_ASS2/`).

## How to run

Requires Python 3 and the `cryptography` package:

```bash
pip3 install cryptography
```

The script defines `ExecuteCrypto` but ships no driver (`example_test.py` is an
empty placeholder), so drive it from a Python shell:

```python
from execute_crypto import ExecuteCrypto

ec = ExecuteCrypto()
sym, pub_s, priv_s, pub_r, priv_r, ecc_pub, ecc_priv = ec.generate_keys()
n_cbc, n_ctr, *_rest = ec.generate_nonces()

plaintext = open("original_plaintext.txt").read().strip()

ct = ec.encrypt("AES-128-CTR-ENC", sym, plaintext, n_ctr)
pt = ec.decrypt("AES-128-CTR-DEC", sym, ct, n_ctr)   # prints timing/size

tag = ec.generate_auth_tag("SHA3-256-HMAC-GEN", sym, plaintext, n_cbc)
ec.verify_auth_tag("SHA3-256-HMAC-VRF", sym, plaintext, n_cbc, tag)

ct_gcm, tag_gcm = ec.encrypt_generate_auth("AES-128-GCM-GEN", sym, sym, plaintext, b"0"*12)
ec.decrypt_verify_auth("AES-128-GCM-VRF", sym, sym, ct_gcm, b"0"*12, tag_gcm)
```

Algorithm-name strings must match exactly, e.g. `AES-128-CBC-ENC`,
`AES-128-CTR-DEC`, `RSA-2048-ENC`, `AES-128-CMAC-GEN`, `SHA3-256-HMAC-VRF`,
`RSA-2048-SHA3-256-SIG-GEN`, `ECDSA-256-SHA3-256-SIG-VRF`, `AES-128-GCM-GEN`,
`AES-128-GCM-VRF`.

## Expected output

Each operation prints its execution time (ms) and, for decryption/verification,
the packet length and key length used to build the report tables above.
