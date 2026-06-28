# Assignment 1 — my Gradescope submission (#224604402)

This is my own numbered Gradescope submission folder for Assignment 1. From
`metadata.yml`:

- Submitter: Harsha Vardhan Somisetty (`cs1200390@cse.iitd.ac.in`)
- Submission ID: 224604402, created 2024-01-25, status `processed`

See the assignment [`README.md`](../README.md) for the full problem and approach.

## Contents

- `solution.zip` — zipped copy of my Assignment-1 solution.
- `solution/decipher_text.py` — my A1 solution. It recovers AES weak-key
  plaintexts by XORing the oracle ciphertext against a precomputed key-stream
  **mask** (chosen-plaintext key-stream recovery), implemented for the 16-, 32-,
  and 48-random-bit key cases in `decipher1/2/3`. `get_entry()` returns
  `2020CS10390`.
- `solution/readme.pdf` — my A1 report explaining the AES-CTR attack.

## Running

Pure Python (standard library only):

```python
from decipher_text import DecipherText
d = DecipherText()
plaintext, key = d.decipher1(ciphertext_bytes)   # 16-bit-key case
```

`ciphertext_bytes` is the byte string returned by the course encryption oracle.
