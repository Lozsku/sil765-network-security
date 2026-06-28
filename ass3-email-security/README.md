# Assignment 3 — Message Handling System security (handout only)

## Problem

A black-box security analysis of the IITD email message-handling system
(`mailstore.iitd.ac.in` IMAP over 993, `smtp.iitd.ac.in` SMTP over STARTTLS/465).
The handout (`2023_24_SIL765_Assignment_3.pdf`) asked for:

- `my_sender` — send an email with a fixed OTP-style body.
- `my_receiver` — fetch the most recent inbox email with full headers.
- `my_parser` — extract the security protocols from the headers.
- Analysis: basic (which TLS/SSL protocols are used), advanced (step-by-step
  **DKIM** signature verification and recovering missing header info), and
  comparative (Gmail vs IITD, including counting DKIM signatures and explaining
  the differences).

## What's here

Only the course handout `2023_24_SIL765_Assignment_3.pdf` (the problem
statement). My own sender/receiver/parser code is not part of this archive.
