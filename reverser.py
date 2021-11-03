ip = input('Enter ip to reverse: ')
ip = ip[::-1] #flips it
if ip[2] == '/':
    power = ip[:2]
    power = power[::-1]
    if power == '24':
        ip = ip[4:] #Gets the power and stuff out of there to prep
        ip = ip[::-1]
        for i in range(256):
            print(ip + str(i)) #simply runs through all ips if given input is /24
    elif int(power) > 15:
        ip = ip[5:] #Gets the power as well as the last . because we need to do the next number
        power = 32-int(power)
        for i in range(4):
            if ip[i] == '.':
                num = ip[:i]
                ip = ip[i:]
                break
        num = int(num[::-1])
        ip = ip[::-1]
        for q in range(2**(power-8)):
            for r in range(256):
                tm = num + q
                print(ip + str(tm) + '.' + str(r)) #goes through the previous cycle the amount of times necessary
    elif int(power) > 7:
        ip = ip[5:]
        power = 32-int(power)
        for i in range(4):
            if ip[i] == '.':
                num = ip[:i]
                ip = ip[i:] 
                ip = ip[1:] #Need to add the +1 here so that it also gets rid of the dot
                break
        num = int(num[::-1]) #Gets us the same number as last time. Now we need to expand
        for l in range(4):
            if ip[l] == '.':
                num2 = ip[:l]
                ip = ip[l:]
                break
        num2 = int(num2[::-1])
        ip = ip[::-1]
        for m in range(2**(power-16)):
            for q in range(256):
                for r in range(256):
                    tm0 = num2 + m
                    tm = num + q
                    print(ip + str(tm0) + '.' + str(tm) + '.' + str(r)) #goes through the previous cycle the amount of times necessary
    else: 
        print('This power is out of the range of the program because of how badly this is coded.')
        print('Range /8 to /24 (included)')
else:
    print(ip)