with open('file.txt', 'r') as f:
  print(type(f))

  f.seek(10)            # move to the 10th byte in the files. "seek" ar kaj hochhea fist 10th byte bad diyea next byte niyea kaj kora.

# The tell() function returns the current position within the file, in bytes. this can be useful for keeping track of your
# location within the file or for seeking to a specific position relative to the current position.

  print(f.tell())       # ""tell()"" ar madhomea amra jantea pari koto porjonto or kun position a achi akhon. ""seek()"" korea rakha hoyeachea.
  data = f.read(5)      # read a next 5 byte
  print(data)




with open('sample.txt', 'w') as f:
  print(type(f))
  f.write('Hello World3!')            # 'hello world3!' print korea.
  f.truncate(5)                       # amra jea write koreachi ta jano 5 Connector jeano thakea, atai "truncate()" ar kaj.

with open('sample.txt', 'r') as f:
  print(f.read())
