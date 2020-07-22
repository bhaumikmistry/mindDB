---
description: UUID in detail
---

# UUID

A Universally Unique Identifier (UUID) is a 128-bit number used to identify information in computer systems. The term globally unique identifier (GUID) is also used, typically software created by Microsoft.

When generated according to the standard methods, UUIDs are for practical purposes unique. Their uniqueness does not depends on a central registration authority or coordination between the parties generating them, unlike most other numbering schemes. While the probability that a UUID will be duplicated is not zero, It is close enough to zero to be negligible.  

#### Format
In its canonical textual representation, the 16 octets of UUID are represented as 32 hexadecimal (base-16) digits. displayed in five groups separated by hyphens, in the form 8-4-4-4-12 for total of 36 characters.
```
123e4567-e89b-12d3-a456-426614174000
xxxxxxxx-xxxx-Mxxx-Nxxx-xxxxxxxxxxxx
```

The four bit M and the 1-3 bit N fields code the format of the UUID itself.



https://docs.python.org/3/library/uuid.html