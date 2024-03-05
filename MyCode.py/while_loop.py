no_of_slices = 6
 
print("Before the while loop, no_of_slices = ", no_of_slices)
 
while no_of_slices > 0:
  no_of_slices -= 1
  print("I will eat a slice of pizza. Remaining slices: ", no_of_slices)
  input()
else:
  print("No more pizza for me.")
 
print("After the while loop, no_of_slices = ", no_of_slices)
