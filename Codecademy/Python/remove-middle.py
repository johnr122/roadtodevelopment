
#Write your function here
def remove_middle(lst, start, end):
  lst = lst[:start] + lst[end+1:]
  return lst

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))