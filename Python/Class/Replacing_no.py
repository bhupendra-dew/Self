class repalce:
    def rep(self, a, b):
        self.a = a
        self.b = b
        self.a = self.b
        return self.a

l = [1,2,3,4,5]
b = []

rod = repalce()

for i in range(len(l)):
    if l[i] % 5 == 0:
        a = rod.rep(l[i], "@")
        b.append(a)
    elif l[i] % 4 == 0:
        a = rod.rep(l[i], "#")
        b.append(a)
    else:
        a = rod.rep(l[i], "*")
        b.append(a)
print(b)