day=int(input("enter day number:"))
switch={
    1:"Monday",
    2:"Tuesday",
    3:"Wednesday",
    4:"Thursday",
    5:"Friday",
    6:"Saturday",
    7:"Sunday"
    }
print(switch.get(day,"Invalid day"))
