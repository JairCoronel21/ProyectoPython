import ascii_magic
out = ascii_magic.from_image_file("correotest.py",columns="200",char="#")
ascii_magic.to_terminal(out)