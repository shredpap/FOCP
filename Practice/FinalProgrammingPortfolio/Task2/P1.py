def convert(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    minst,secst="minutes","seconds"
    if minutes==1 or minutes==0:
        minst="minute"
    if seconds==1 or seconds==0:
        secst="second"
    return "%02d %s, %02d %s" % (minutes, minst, seconds, secst)
retur= lambda dat : (len(dat),sum(dat.values())//len(dat),min(dat.values()),max(dat.values()),min(dat, key=dat.get))
count=0
data={}
# val=""
print("Park Run Timer\n~~~~~~~~~~~~~~\n\nLet's go!\n")
while True:
    try:
        val=(input("> "))
        valt=val.split("::")
        if val=="END":
            break
        int(valt[0])
        if valt[1]=="" or valt[0]=="":
            print("Error in data stream. Ignoring. Carry on.")
        else:
            count+=1
            data[valt[0]]=int(valt[1])
    except:
        print("Error in data stream. Ignorning. Carry on.")
try:
    t,a,m,ma,win=retur(data)
    a,m,ma=convert(a),convert(m),convert(ma)
    print("\nTotal Runners:  %d\nAverage Time:  %s\nFastest Time:  %s\nSlowest Time:  %s\n\nBest Time Here:  Runner #%s"%(t,a,m,ma,win))
except ZeroDivisionError:
    print("No data found. Nothing to do. What a pity.")