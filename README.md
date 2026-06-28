# SIL765 — Networks and System Security (IIT Delhi)

This is my coursework archive for **SIL765: Networks and System Security**,
Semester II, 2023–2024, IIT Delhi (CSE).

- **Me:** Somisetty Harsha Vardhan
- **Entry number:** 2020CS10390 (Gradescope login `cs1200390@cse.iitd.ac.in`)

This is a journal of what I did in the course. SIL765 was an applied security
course: half of it was hands-on cryptography (implementing and breaking
ciphers, benchmarking primitives) and half was system/network security analysis
(email security, web penetration testing, and a paper-presentation project on
side-channel attacks). Below I walk through each piece of graded work, what the
problem was, and what I actually built or analyzed.

Each assignment now lives in its own folder. Where I wrote code, the folder has
my real implementation and report. Where the course only gave us a handout (and
my own deliverable is not in this archive), I say so plainly and keep the
problem statement.

---

## What's in here

| Folder | Assignment | Topic | My work present? |
|--------|------------|-------|------------------|
| `ass1-aes-cryptanalysis/` | A1 — Basic Cryptanalysis | Breaking AES that uses weak (low-entropy) keys, via the encryption oracle | Yes — `decipher_text.py` + report |
| `ass2-crypto-primitives-benchmark/` | A2 — Evaluating Cryptographic Primitives | Implement and benchmark AES-CBC/CTR/GCM, RSA, CMAC, HMAC, RSA-PSS, ECDSA | Yes — `execute_crypto.py` + report (timing tables) |
| `ass3-email-security/` | A3 — Message Handling System | Black-box security analysis of the IITD email system (SMTP/IMAP/DKIM) | Handout only |
| `ass4-website-security/` | A4 — Website Security Analysis | Penetration testing two websites with two tools each | Handout only |
| `project-spectre/` | Course project | Paper presentation + proposal on Spectre / speculative-execution side channels | Handout only |

---

## Assignment 1 — Basic Cryptanalysis (AES with weak keys)

The problem: AES-128 is strong with a random key, but not if the key is
predictable. Three cases were defined where only the low-order bits of the
128-bit key are random and the rest are zero — 16, 32, and 48 random LSBs. Given
an encryption oracle (I submit a plaintext on Gradescope and get back its
ciphertext), I had to recover the secret key for each case **more efficiently
than brute force**.

What I did: the underlying mode is AES-CTR, which produces a key-stream that is
XORed with the plaintext. So instead of brute-forcing the key, I recovered the
key-stream directly. By XORing a known plaintext with its ciphertext I expose
the key-stream bytes; with enough chosen-plaintext pairs the whole key-stream is
recovered, and then any ciphertext can be decrypted by XORing it against that
recovered mask. My `decipher_text.py` implements exactly this — each
`decipher1/2/3` holds the recovered key-stream mask and the recovered key for
its case. Details and run instructions are in
[`ass1-aes-cryptanalysis/README.md`](ass1-aes-cryptanalysis/README.md).

---

## Assignment 2 — Evaluating Cryptographic Primitives

The problem: build a set of encryption/authentication primitives and measure
three costs for each — computational (run time, ms), communication (packet
length, bits), and storage (key length, bits) — then compare their pros and
cons.

What I did: I implemented `ExecuteCrypto` in `execute_crypto.py` on top of
Python's `cryptography` (hazmat) library, covering AES-128-CBC, AES-128-CTR,
RSA-2048-OAEP, AES-CMAC, SHA3-256-HMAC, RSA-2048-PSS signatures, ECDSA-P256
signatures, and AES-128-GCM. Each operation is timed in milliseconds, and I
computed packet and key lengths to fill the report's cost tables. The headline
result is that RSA private-key operations (decrypt, sign) dominate at ~37 ms
while symmetric primitives are 100–1000x faster. Full tables, files, and run
instructions are in
[`ass2-crypto-primitives-benchmark/README.md`](ass2-crypto-primitives-benchmark/README.md).

---

## Assignment 3 — Message Handling System (handout only)

The problem: a black-box security analysis of the IITD email system
(`mailstore.iitd.ac.in` IMAP over 993, `smtp.iitd.ac.in` SMTP over STARTTLS/465).
The deliverables were a sender, a receiver, and a header parser, plus an
analysis of the TLS/SSL protocols in use and a step-by-step **DKIM** signature
verification, with a Gmail-vs-IITD comparison.

Only the handout is in this archive — see
[`ass3-email-security/README.md`](ass3-email-security/README.md).

---

## Assignment 4 — Website Security Analysis (handout only)

The problem: use penetration-testing tools (Nmap, Metasploit, Burp Suite,
OpenVAS, etc.) to analyze two popular websites with two tools each — probing
vulnerabilities, exploiting critical ones found, and recommending mitigations.

Only the handout is in this archive — see
[`ass4-website-security/README.md`](ass4-website-security/README.md).

---

## Course project — Spectre / speculative-execution side channels

The project required picking a top-venue security paper, recording a
presentation, and writing a short proposal. My topic was **Spectre** and
micro-architectural side-channel attacks. This folder has the course handouts
and the reference slide decks I used. My own filled-in proposal/slides are not
in this archive — see
[`project-spectre/README.md`](project-spectre/README.md).

---

## What I learned / skills

- **Block-cipher modes** — practical differences between AES-CBC, AES-CTR, and
  AES-GCM (padding, nonces, AEAD), and why CTR/GCM avoid CBC's padding-oracle
  pitfalls.
- **Cryptanalysis** — exploiting low-entropy keys and the XOR/key-stream
  structure of CTR mode to recover plaintext without brute-forcing the key
  (chosen-plaintext key-stream recovery).
- **Benchmarking cryptographic primitives** — measuring compute, communication,
  and storage cost of real primitives and reasoning about the trade-offs.
- **Public-key crypto** — RSA-OAEP encryption, RSA-PSS and ECDSA signatures, and
  why RSA private-key operations are the expensive ones while ECDSA stays
  balanced and compact.
- **Email / DKIM security** — how SMTP/IMAP use TLS and how DKIM signatures are
  built and verified.
- **Web penetration testing** — using tools like Nmap, Burp Suite, and OpenVAS
  to find and exploit web vulnerabilities.
- **Side-channel attacks** — Spectre and speculative-execution attacks that leak
  data across security boundaries through micro-architectural state.

---

## Notes

- The PDFs named `2023_24_SIL765_*` are the **official course handouts** (problem
  statements). I kept each one with its assignment.
- I did not find any duplicate `(1)`/`(2)` PDF copies in this archive (the
  previous index mentioned some, but only single copies are present), so there is
  no `duplicates/` subfolder.
- No files were deleted or modified during reorganization — only moved, and
  README files added.
