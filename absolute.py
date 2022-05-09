from xml.dom.minidom import parseString


number = int(input("input any number : "))
if number < 0 :
    absolute = number * -1
    print(f'the aboslulte value is {absolute}')
else:
    print(f'the aboslulte value is {number}')