file = open('youtube.txt','w')
#or

with open('youtube.txt','w') as file:
    file.write('chai aur python')
#file closes by itself when u comes out of the block

try:
    file.write('chai aur code')
finally:
    file.close()