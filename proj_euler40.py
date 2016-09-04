astring = ''
i = 1
while len(astring) <= 1000000:
    astring += str(i)
    i += 1

print int(astring[0])*int(astring[9])*int(astring[99])*int(astring[999])*int(astring[9999])*int(astring[99999])*int(astring[999999])