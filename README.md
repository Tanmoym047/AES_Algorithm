## AES-128 Key Expansion (Key Schedule)

### 1. Initial Key

The AES-128 algorithm uses a 128-bit (16-byte) cipher key. The initial key is represented in hexadecimal format:

```python
key = 0x736174697368636a6973626f72696e67
```

The key is divided into four 32-bit words (W[0]–W[3]), with each word containing four bytes.

```python
key_dictionary = {
    0: [0x73, 0x61, 0x74, 0x69],
    1: [0x73, 0x68, 0x63, 0x6A],
    2: [0x69, 0x73, 0x62, 0x6F],
    3: [0x72, 0x69, 0x6E, 0x67],
}
```

### 2. AES S-Box

The AES Substitution Box (S-Box) is a predefined 16 × 16 lookup table containing 256 hexadecimal values.

It is used in the `subword()` function to substitute each byte with its corresponding S-Box value.

For each byte:
- The upper four bits determine the row.
- The lower four bits determine the column.

```python
row = (item & 0xF0) >> 4
column = item & 0x0F
subword.append(s_box[row][column])
```

### 3. Round Constants (Rcon)

AES-128 uses ten round constants during key expansion. Each round constant is represented as a four-byte word.

```python
rotate_con = {
    1: [0x01, 0x00, 0x00, 0x00],
    2: [0x02, 0x00, 0x00, 0x00],
    3: [0x04, 0x00, 0x00, 0x00],
    4: [0x08, 0x00, 0x00, 0x00],
    5: [0x10, 0x00, 0x00, 0x00],
    6: [0x20, 0x00, 0x00, 0x00],
    7: [0x40, 0x00, 0x00, 0x00],
    8: [0x80, 0x00, 0x00, 0x00],
    9: [0x1B, 0x00, 0x00, 0x00],
    10: [0x36, 0x00, 0x00, 0x00]
}
```

### 4. Key Expansion Functions

The implementation uses the following functions:

**a. Hex XOR**

Performs byte-wise XOR between two four-byte words.

**b. RotWord**

Performs a cyclic left rotation of a four-byte word.

Example:

```text
Input:  [73, 61, 74, 69]
Output: [61, 74, 69, 73]
```

**c. SubWord**

Applies the AES S-Box substitution to every byte of a word.

**d. Calculate g()**

The `calculate_g()` function performs three operations:

1. RotWord
2. SubWord
3. XOR with the corresponding round constant (Rcon)

### 5. Key Expansion Algorithm

AES-128 generates a total of 44 words (W[0]–W[43]) from the original four words.

The expansion follows two rules:

- When `w % 4 == 0`:

  `W[w] = W[w-4] XOR g(W[w-1])`

- Otherwise:

  `W[w] = W[w-4] XOR W[w-1]`

The process continues until all 44 words have been generated.

### 6. Final Output

The implementation prints all 44 generated words in hexadecimal format.

These words form 11 round keys:
- Initial key: W[0]–W[3]
- Round 1 key: W[4]–W[7]
- Round 2 key: W[8]–W[11]
- ...
- Round 10 key: W[40]–W[43]

Thus, the AES-128 key expansion generates 11 round keys, each containing 128 bits (16 bytes).

### 7. Execution

Run the Python implementation:

```bash
python key_expansion.py
```

The output displays the expanded key words in hexadecimal format.
