"""Test Phase 5 (your wild card) in isolation.

Run from the project root with:  python tests/test_phase5.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine import phase5_encrypt, phase5_decrypt

test = "Hello World!"
encrypted = phase5_encrypt(test, {})
print(f"Original:  {test}")
print(f"Phase 5:   {encrypted}")
print(f"Reversed:  {phase5_decrypt(encrypted, {})}")
print(f"Match:     {test == phase5_decrypt(encrypted, {})}")


def encrypt(plaintext, key):
    """Apply all 5 encryption phases in sequence."""
    result = plaintext

    # Phase 1: Substitution (shift all characters)
    result = phase1_encrypt(result, key)

    # Phase 2: Transposition (reverse blocks)
    result = phase2_encrypt(result, key)

    # Phase 3: Key-dependent (password-based variable shift)
    result = phase3_encrypt(result, key)

    # Phase 4: Noise injection (add decoy characters)
    result = phase4_encrypt(result, key)

    # Phase 5: Wild Card (your invention!)
    result = phase5_encrypt(result, key)

    return result


def decrypt(ciphertext, key):
    """Reverse all 5 encryption phases."""
    result = ciphertext

    # Decrypt in REVERSE order!

    # Phase 5: Reverse your wild card
    result = phase5_decrypt(result, key)

    # Phase 4: Remove noise characters
    result = phase4_decrypt(result, key)

    # Phase 3: Reverse password-based shift
    result = phase3_decrypt(result, key)

    # Phase 2: Reverse transposition (self-inverse)
    result = phase2_decrypt(result, key)

    # Phase 1: Reverse substitution (shift back)
    result = phase1_decrypt(result, key)

    return result
