# Write a function, which takes a non-negative integer (seconds) as input and returns the time in
# a human-readable format (HH:MM:SS)
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures.

def make_readable(seconds):
    s = str(seconds % 60)
    s = s if len(s) == 2 else "0"+s

    m = str((seconds // 60) % 60)
    m = m if len(m) == 2 else "0"+m

    h = str(seconds // 3600)
    h = h if len(h) == 2 else "0"+h

    return f"{h}:{m}:{s}"
