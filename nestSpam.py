def spam1():

    def spam2():

        def spam3():
            z = " even more spam"
            print("In spam3 locals are {}".format(locals()))
            return z

        y = " more spam"
        print("In spam2 locals are {}".format(locals()))
        y += spam3()
        return y

    x = "spam"
    print("In spam1 locals are {}".format(locals()))
    x += spam2()
    return x


print(spam1())
print(locals())
print(globals())