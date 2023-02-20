class Time:
        def __init__(self,h,m,s):
            self.__h=h
            self.__m=m
            self.__s=s
        def __add__(self,other):
            ss=self.__s+other.__s
            mm=self.__m+other.__m
            hh=self.__h+other.__h
            if ss>60:
                mm=mm+ss/60
                ss=ss%60
            if mm>60:
                hh=hh+int(mm/60)
                mm=int(mm%60)
            time="{0} hours:{1} minutes:{2} seconds".format(hh,mm,ss)
            return time
t1=Time(2,60,12)
t2=Time(3,34,30)
print("Sum of time:",t1+t2)