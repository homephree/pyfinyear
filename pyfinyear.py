import datetime
import calendar


def finyear( newyear, inst):
    thisyear= inst.year
    lastyear= thisyear-1
    nextyear= thisyear+1
    if(inst.month >= newyear):
        return finyearnamefromyears( thisyear,nextyear)
    return finyearnamefromyears(lastyear,thisyear)


def finyearnamefromyears(firstyear, nextyear):
    return "{0}/{1}".format(min(firstyear,nextyear) % 100, max(firstyear,nextyear) % 100)
