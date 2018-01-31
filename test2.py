import comcom.procedural

comcom.procedural.init()

input = b"abc"
output = comcom.procedural.run_command(input, 'cat', ['cat'])
print(output)

comcom.procedural.destroy()
