# Assignment 2 — my work area (Evaluating Cryptographic Primitives)

This folder holds my development of Assignment 2 — benchmarking the compute /
communication / storage cost of AES-CBC, AES-CTR, RSA-2048, AES-CMAC,
SHA3-256-HMAC, RSA+SHA3 signatures, ECDSA, and AES-GCM. See the assignment
[`README.md`](../README.md) for the problem, results, and run instructions.

## Final submission

`script/` is my finished submission:

- `execute_crypto.py` — my full `ExecuteCrypto` implementation (uses the
  `cryptography` library; times every operation in ms and computes packet/key
  lengths).
- `readme.pdf` — my A2 report (timing tables and pros/cons discussion).
- `original_plaintext.txt`, `setup_env.sh` — the input plaintext and a
  package-install stub.
- `example_test.py` — an empty placeholder (I did not ship a driver).

`examples/` holds the handout-provided sample keys, ciphertexts, and auth tags.

## Dev history

The zip files are my progressive snapshots of `execute_crypto.py`, oldest to
newest:

```
script_v1 -> script_v2 -> script_time -> script_v3 -> script_v4 -> script_time2
          -> script_v4.2 -> script_v5 -> script.zip (final)
script_failed.zip = a non-working intermediate
```

`2023_24_SIL765_Assignment_2.pdf` is the course handout, kept here alongside the
work.

## Running

```bash
pip3 install cryptography
```

Then drive `ExecuteCrypto` from a Python shell (see the assignment README for an
end-to-end example). Algorithm-name strings must match exactly, e.g.
`AES-128-CTR-ENC`, `AES-128-GCM-GEN`.
