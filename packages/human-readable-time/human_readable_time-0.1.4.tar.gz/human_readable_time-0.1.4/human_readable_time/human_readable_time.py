# First Solution:
def make_readable1(seconds):
    if seconds < 0:
        raise ValueError("Seconds cannot be negative.")
    HH = MM = SS = 0
    MM, SS = divmod(seconds, 60)
    HH, MM = divmod(MM, 60)
    HH = str(HH).zfill(2)
    MM = str(MM).zfill(2)
    SS = str(SS).zfill(2)

    return f"{HH}:{MM}:{SS}"

# Second Solution:
def make_readable2(seconds):
    if seconds < 0:
        raise ValueError("Seconds cannot be negative.")
    HH, remaining = divmod(seconds, 3600)
    MM, SS = divmod(remaining, 60)
    return f"{HH:02d}:{MM:02d}:{SS:02d}"

