# Assignment 1 — Basic Cryptanalysis (AES with weak keys)

## Problem

AES-128 is secure with a strong, random key, but not if the key is predictable.
The handout (`2023_24_SIL765_Assignment_1.pdf`) defined three cases where only
the low-order bits of the 128-bit key are random and the rest are zero:

- Case 1 (`decipher1`): 16 random LSBs, rest 0
- Case 2 (`decipher2`): 32 random LSBs, rest 0
- Case 3 (`decipher3`): 48 random LSBs, rest 0

I was given an encryption oracle (submit a plaintext on Gradescope, get back the
ciphertext) and had to recover the secret key for each case **more efficiently
than brute force**, filling in `decipher1/2/3` in `decipher_text.py`.

## What I did

The cipher runs in AES-CTR mode. In CTR, AES encrypts a counter to produce a
key-stream, and the ciphertext is just `plaintext XOR key-stream`. So I did not
brute-force the key at all — I recovered the **key-stream** instead:

1. Submit known plaintexts to the oracle and collect the ciphertexts.
2. XOR each known plaintext against its ciphertext to expose the corresponding
   key-stream bytes.
3. With enough chosen-plaintext pairs, the full key-stream for that case is
   recovered.
4. To decrypt any ciphertext, convert it to a bit string and XOR it against the
   recovered key-stream mask (truncated to the ciphertext length), then re-pack
   the bits into bytes.

In `decipher_text.py` each `decipher1/2/3` holds the recovered key-stream mask
(`xor_mask`) and the recovered key (`deciphered_key`) for its case. A helper
`sixteen_to_secondary` turns the ciphertext bytes into a bit string, and
`get_entry()` returns my entry number `2020CS10390`.

This is the chosen-plaintext key-stream recovery attack described in my report:
brute force is fine for the 16-bit case but infeasible at 32/48 bits, whereas
key-stream recovery works regardless of how many key bits are random.

## Key files

- `224604402/solution/decipher_text.py` — my graded solution.
- `224604402/solution/readme.pdf` — the bundled report.
- `224604402/metadata.yml` — Gradescope submission metadata (submitter Harsha
  Vardhan Somisetty, `cs1200390@cse.iitd.ac.in`, submitted 2024-01-25). This
  numbered folder is my own Gradescope submission.
- `224604402/solution.zip` — zipped copy of the solution.
- `sil.pdf` / `readme.pdf` — root-level copies of the same AES-CTR cryptanalysis
  report (byte-for-byte identical to each other).
- `2023_24_SIL765_Assignment_1.pdf` — the course handout (problem statement).

## How to run

Pure Python, standard library only (no external dependencies):

```python
from decipher_text import DecipherText

d = DecipherText()
plaintext, key = d.decipher1(ciphertext_bytes)   # 16-bit-key case
# decipher2 -> 32-bit case, decipher3 -> 48-bit case
```

`ciphertext_bytes` is the byte string returned by the course encryption oracle
for that case.

## Expected output

Each `decipherN` prints the input ciphertext, the deciphered plaintext, and the
recovered key, then returns `(deciphered_text, deciphered_key)`.
