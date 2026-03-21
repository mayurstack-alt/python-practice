N=int(input())
failedcount=0
passedcount=0
gradeAstudent=0
highestavg=0
for i in range(1,N+1):
        m1, m2, m3, m4, m5 = map(int, input().split())
        if((m1<35) or (m2<35) or (m3<35) or (m4<35) or (m5<35)):
            failedcount=failedcount+1
        else:
            avgMarks=(m1+m2+m3+m4+m5)/5
            if((m1==100) or (m2==100) or (m3==100) or (m4==100) or (m5==100)):
                avgMarks=avgMarks+5
            if(avgMarks>100):
                avgMarks=100
            if(avgMarks>=90):
                gradeAstudent=gradeAstudent+1
                passedcount=passedcount+1
            elif((avgMarks>=75) and (avgMarks<90)):
                passedcount=passedcount+1
            elif((avgMarks>=60) and (avgMarks<75)):
                passedcount=passedcount+1
            elif(avgMarks<60):
                failedcount=failedcount+1
                continue
      
            if(avgMarks>highestavg):
                highestavg=avgMarks
           
print(passedcount)
print(failedcount)
print(f"{highestavg:.2f}")
print(gradeAstudent)