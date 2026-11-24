#!/usr/bin/env python3
"""The Plumber's Inbox — make.fun bounty entry.

Writes a cold email of about 120 words (at most 800 characters,
subject line included) to /output/entry.txt: a bookkeeping service
pitching a busy plumber — same-day invoices, receipts matched from
phone photos, VAT and payroll filed on time, one flat monthly fee,
and a single easy ask at the end.

Deterministic: the text is a constant, so every run writes the same
bytes. No network.
"""
import os

TEXT = (
    "Subject: Your invoices, done before your first job\n"
    "\n"
    "Hi Dave,\n"
    "\n"
    "You're on a burst-pipe call-out by 7am and the boiler-swap "
    "paperwork is still on the kitchen table at 7pm. I do bookkeeping "
    "for two-van firms like yours, and I take that pile off your hands: "
    "invoices sent the same day, receipts snapped on your phone matched "
    "for you, VAT and payroll filed on time.\n"
    "\n"
    "It is a flat £180 a month, no contract, and I learn your job codes "
    "in week one so nothing lands back on your desk.\n"
    "\n"
    "Worth ten minutes on Thursday between jobs? Reply YES and I will "
    "call you.\n"
    "\n"
    "— Sarah, ClearLedger Books"
)


def main():
    assert 1 <= len(TEXT) <= 800, f"text is {len(TEXT)} characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    print(f"wrote {path} ({len(TEXT)} characters, {len(TEXT.split())} words)")


if __name__ == "__main__":
    main()
