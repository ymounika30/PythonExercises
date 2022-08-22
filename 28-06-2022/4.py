##4.write a python program even and odd using list comprehension.
obj = [f"{i}=Even" if i%2==0 else  f"{i}=odd" for i  in range(1,11)] 
print("\n".join(obj))
