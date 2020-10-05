import matplotlib.pyplot as plt
st= str(input("Enter an equation : "))
s = st + '+'
l = len(s)
a= []
n = 0
beg,end = 0,0
for i in range(1,l):
    if s[i] in ['+','-']:
        a.append(s[beg:i])
        beg = i
x,y = [],[]
num = []
add = 0
j = -100
while j<=100:
    j+=0.01
    x.append(j)
    add=0
    for i in a:
        sign  = i[0]
        xpos = i.find('x')
        if xpos == -1:
            const = float(i[1:])
            if sign == '+':
                add+=const
            else:
                add-=const
        else:
            if i[-1].isdigit() and i[1].isdigit():
                coeff = float(i[1:xpos])
                fact = float(i[xpos+1:])
                if sign == '+':
                    add+=coeff*(j**fact)
                else:
                    add-=coeff*(j**fact)
            elif i[-1].isdigit():
                fact = float(i[xpos+1:])
                if sign == '+':
                    add+=(j**fact)
                else:
                    add-=(j**fact)
            elif i[1].isdigit():
                coeff = float(i[1:xpos])
                if sign == '+':
                    add+=coeff*j
                else:
                    add-=coeff*j
            else:
                if sign == '+':
                    add+=j
                else:
                    add-=j
    y.append(add)
#print (x)
#print (y)
plt.plot(x,y,label = st,color = 'red')
#plt.xlabel('x - axis')
#plt.ylabel('y - axis')
#plt.title(st.upper())
ax = plt.gca()
plt.grid(True)
plt.legend(bbox_to_anchor=(1.1, 1.05))
#plt.style.use('ggplot')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.show()
plt.close()
