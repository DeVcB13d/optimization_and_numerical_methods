# Program to find roots of an equation using false postion methon

# Function to find an approprite interval using sign change
def find_interval(f,start = 0,max_steps = 10):
    a = start
    b = start+1
    y_a = f(a)
    y_b = f(b) 
    steps = 0
    while y_a > 0 and y_b < 0 and steps <= max_steps:
        a = a+1
        b = b+1
        y_a = f(a)
        y_b = f(b) 
        steps+=1
    return a,b

def false_postion(f,max_iters = 10):
    a,b = (1,0)
    # Formula to calculate the false postion
    x_iter = lambda a,b,f: (a*f(b) - b*f(a)) / ( f(b) - f(a) )
    iters = 0
    while iters < max_iters:
        x_i = x_iter(a,b,f)
        y_i = f(x_i)
        if y_i < 0  :
            a = x_i
        elif y_i > 0 :
            b = x_i
        else:
            return x_i
        print("iteration {0} \n interval [{1} , {2}] \n f(x_{0}) = {3} \n x_{0} = {4}".format(iters,a,b,y_i,x_i))
        iters+=1
    print("Final root : ",x_i)




def main():
    function = lambda x : x**3 - 12
    false_postion(function)


main()
