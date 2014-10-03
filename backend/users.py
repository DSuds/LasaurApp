import sys, os, time, msvcrt

allowed = {
"admin":"",
"yourname":"password"
}

badgetime = 20
''' Badge type can be 'dec' or 'W2-4' for Weigand 2H10d+4H10d format '''
badgetype = 'dec'

def user_badge_in():
    badge = '0'
    print 'Waiting for user badge (%s)' % os.name+str(sys.stdin.isatty())
    
    if not sys.stdin.isatty():
        sys.stdin.flush()
        badge = sys.stdin.readline()
        print 'Got it!'
    elif os.name == 'nt':
        timeout = time.time() + float(badgetime)
        while msvcrt.kbhit():
            msvcrt.getch()

        while timeout>time.time() :
            if msvcrt.kbhit():
                ch = msvcrt.getch()
                if ch!='\r':
                    badge += ch
                else:
                    print 'Got it!'
                    break
                
            else:
                time.sleep(0.5)
                
    elif os.name == 'posix':
        sys.stdin.flush()
        i,o,e = select.select([sys.stdin],[],[], badgetime)
        if sys.stdin in i:
            badge = sys.stdin.readline()

    print 'Badge read:'+badge
    if badgetype == 'dec':
        badgenum = "%x" % int(badge)
    elif badgetype == 'W2-4':
        badgenum = "%x%x" % int(badge[0:4]), int(badge[5:])
    else:
        badgenum = badge
        
    return badgenum
