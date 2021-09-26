class frog:
    def __init__(self, name, isfrog):
        self.name = name
        self.isfrog = isfrog




frogCheck = frog("Liav", True)

if(frogCheck.isfrog):
    print(f"[+] {frogCheck.name} is absolutely a frog! ")

else:
    print(f"[!] {frogCheck.name} definitely not a frog! ")