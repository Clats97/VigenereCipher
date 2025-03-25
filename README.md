# VigenereCipher
A simple CLI &amp; GUI Vigenere cipher tool. This tool will encrypt and decrypt text using the Vigenere cipher method. It's more secure than Caesar or ROT13.

### Simple Explanation of the Vigenère Cipher:

The **Vigenère cipher** is a method of encrypting text by using a keyword. Unlike a basic Caesar cipher (which shifts letters by a fixed amount), the Vigenère cipher uses different shifts based on the letters of a keyword.

### How It Works (Step-by-Step):

**Step 1: Choose a Keyword**
- You select a word, for example: `KEY`.

**Step 2: Write Your Plaintext**
- Suppose the message is: `HELLO`

**Step 3: Repeat Your Keyword**
- Repeat the keyword beneath your message, letter by letter:
```
Message:   H  E  L  L  O
Keyword:   K  E  Y  K  E
```

**Step 4: Convert Letters into Numerical Values**
- Assign numbers from `0 to 25` for each letter (`A=0, B=1, C=2... Z=25`):

| Message | H(7) | E(4) | L(11) | L(11) | O(14) |
|---------|------|------|-------|-------|-------|
| Keyword | K(10)| E(4) | Y(24) | K(10) | E(4)  |

**Step 5: Add the Numbers (Modulo 26)**
- Add the numerical values of message and keyword letters together, then take the remainder when divided by `26` (modulo 26):

| Calculation | (7+10)=17 | (4+4)=8 | (11+24)=35 mod 26=9 | (11+10)=21 | (14+4)=18 |
|-------------|-----------|---------|----------------------|------------|-----------|
| Result      | 17        | 8       | 9                    | 21         | 18        |

**Step 6: Convert Back to Letters**
- Translate the numeric results back to letters (`A=0, B=1... Z=25`):

| Result Number | 17 | 8 | 9 | 21 | 18 |
|---------------|----|---|---|----|----|
| Encrypted     | R  | I | J | V  | S  |

The ciphertext becomes `RIJVS`.

---

### Decryption (Reversing the Process):
To decrypt, simply reverse this process:
- Convert letters back to numbers.
- Subtract keyword numbers from ciphertext numbers (using modulo 26).
- Convert numbers back to letters.

---

### Why Vigenère is Better than Caesar:
- It doesn't always shift by the same amount, making it harder to crack.
- It resists frequency analysis better, because each letter can be encrypted differently depending on the keyword.



