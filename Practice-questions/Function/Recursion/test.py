#Recursion function to print numbers from n to 1 and then print "Done"
def show(n):
    if n == 0:
        print("Done")
        return
    print(n)
    show(n-1)
show(5)