c = {'z':10, 'b':1,'c': 9}
print sorted([(v,k) for k,v in c.items()],reverse=True)

print dir(list)