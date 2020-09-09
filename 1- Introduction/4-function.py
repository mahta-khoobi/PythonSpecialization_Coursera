def computepay(h,r):
    if h<=40:
        result = r * h
    elif h>40:
        result= 40 * r + ((h-40) * r * 1.5);

    return result

hrs = input("Enter Hours:")
hrs = float(hrs)

rate = input("Enter Rate:")
rate = float(rate)

p = computepay(hrs,rate)
print("Pay",p)
input('type something')
