#!/usr/bin/env python
# coding=utf-8

import xlwt
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
chartData = [
    {
        'Single Processor': 100,
        'List': (1993.0, 5, 1),
        'Constellations': 0,
        'SMP': 243,
        'Cluster': 0,
        'MPP': 122,
        'SIMD': 35,
    },
    {
        'Single Processor'
        : 93, 'List': (1993.0, 10, 1), 'Constellations'
    : 0, 'SMP'
    : 233, 'Cluster'
    : 0, 'MPP'
    : 149, 'SIMD'
    : 25,
    },
    {
        'Single Processor'
        : 72, 'List': (1994.0, 5, 1), 'Constellations'
    : 0, 'SMP'
    : 180, 'Cluster'
    : 0, 'MPP'
    : 225, 'SIMD'
    : 23,
    },
    {
        'Single Processor'
        : 45, 'List': (1994.0, 10, 1), 'Constellations'
    : 0, 'SMP'
    : 182, 'Cluster'
    : 0, 'MPP'
    : 246, 'SIMD'
    : 27,
    },
    {
        'Single Processor'
        : 29, 'List': (1995.0, 5, 1), 'Constellations'
    : 0, 'SMP'
    : 241, 'Cluster'
    : 0, 'MPP'
    : 219, 'SIMD'
    : 11,
    },
    {
        'Single Processor'
        : 22, 'List': (1995.0, 10, 1), 'Constellations'
    : 16, 'SMP'
    : 194, 'Cluster'
    : 0, 'MPP'
    : 261, 'SIMD'
    : 7,
    },
    {
        'Single Processor'
        : 19, 'List': (1996.0, 5, 1), 'Constellations'
    : 24, 'SMP'
    : 216, 'Cluster'
    : 0, 'MPP'
    : 234, 'SIMD'
    : 7,
    },
    {
        'Single Processor'
        : 3, 'List': (1996.0, 10, 1), 'Constellations'
    : 19, 'SMP'
    : 183, 'Cluster'
    : 0, 'MPP'
    : 288, 'SIMD'
    : 7,
    },
    {
        'Single Processor'
        : 0, 'List': (1997.0, 5, 1), 'Constellations'
    : 12, 'SMP'
    : 215, 'Cluster'
    : 1, 'MPP'
    : 270, 'SIMD'
    : 2,
    },
    {
        'Single Processor'
        : 0, 'List': (1997.0, 10, 1), 'Constellations'
    : 10, 'SMP'
    : 263, 'Cluster'
    : 1, 'MPP'
    : 226, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (1998.0, 5, 1), 'Constellations'
    : 14, 'SMP'
    : 266, 'Cluster'
    : 1, 'MPP'
    : 219, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (1998.0, 10, 1), 'Constellations'
    : 17, 'SMP'
    : 255, 'Cluster'
    : 2, 'MPP'
    : 226, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (1999.0, 5, 1), 'Constellations'
    : 25, 'SMP'
    : 222, 'Cluster'
    : 6, 'MPP'
    : 247, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (1999.0, 10, 1), 'Constellations'
    : 66, 'SMP'
    : 169, 'Cluster'
    : 7, 'MPP'
    : 258, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2000.0, 5, 1), 'Constellations'
    : 93, 'SMP'
    : 139, 'Cluster'
    : 11, 'MPP'
    : 257, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2000.0, 10, 1), 'Constellations'
    : 115, 'SMP'
    : 11, 'Cluster'
    : 28, 'MPP'
    : 346, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2001.0, 5, 1), 'Constellations'
    : 118, 'SMP'
    : 31, 'Cluster'
    : 32, 'MPP'
    : 319, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2001.0, 10, 1), 'Constellations'
    : 143, 'SMP'
    : 57, 'Cluster'
    : 43, 'MPP'
    : 257, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2002.0, 5, 1), 'Constellations'
    : 184, 'SMP'
    : 3, 'Cluster'
    : 81, 'MPP'
    : 232, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2002.0, 10, 1), 'Constellations'
    : 203, 'SMP'
    : 2, 'Cluster'
    : 92, 'MPP'
    : 203, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2003.0, 5, 1), 'Constellations'
    : 136, 'SMP'
    : 0, 'Cluster'
    : 151, 'MPP'
    : 213, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2003.0, 10, 1), 'Constellations'
    : 108, 'SMP'
    : 0, 'Cluster'
    : 221, 'MPP'
    : 171, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2004.0, 5, 1), 'Constellations'
    : 74, 'SMP'
    : 0, 'Cluster'
    : 298, 'MPP'
    : 128, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2004.0, 10, 1), 'Constellations'
    : 103, 'SMP'
    : 0, 'Cluster'
    : 298, 'MPP'
    : 99, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2005.0, 5, 1), 'Constellations'
    : 79, 'SMP'
    : 0, 'Cluster'
    : 304, 'MPP'
    : 117, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2005.0, 10, 1), 'Constellations'
    : 36, 'SMP'
    : 0, 'Cluster'
    : 361, 'MPP'
    : 103, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2006.0, 5, 1), 'Constellations'
    : 38, 'SMP'
    : 0, 'Cluster'
    : 364, 'MPP'
    : 98, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2006.0, 10, 1), 'Constellations'
    : 31, 'SMP'
    : 0, 'Cluster'
    : 361, 'MPP'
    : 108, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2007.0, 5, 1), 'Constellations'
    : 19, 'SMP'
    : 0, 'Cluster'
    : 374, 'MPP'
    : 107, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2007.0, 10, 1), 'Constellations'
    : 3, 'SMP'
    : 0, 'Cluster'
    : 406, 'MPP'
    : 91, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2008.0, 5, 1), 'Constellations'
    : 2, 'SMP'
    : 0, 'Cluster'
    : 399, 'MPP'
    : 99, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2008.0, 10, 1), 'Constellations'
    : 2, 'SMP'
    : 0, 'Cluster'
    : 409, 'MPP'
    : 89, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2009.0, 5, 1), 'Constellations'
    : 2, 'SMP'
    : 0, 'Cluster'
    : 410, 'MPP'
    : 88, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2009.0, 10, 1), 'Constellations'
    : 2, 'SMP'
    : 0, 'Cluster'
    : 418, 'MPP'
    : 80, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2010.0, 5, 1), 'Constellations'
    : 2, 'SMP'
    : 0, 'Cluster'
    : 424, 'MPP'
    : 74, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2010.0, 10, 1), 'Constellations'
    : 2, 'SMP'
    : 0, 'Cluster'
    : 413, 'MPP'
    : 85, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2011.0, 5, 1), 'Constellations'
    : 2, 'SMP'
    : 0, 'Cluster'
    : 411, 'MPP'
    : 87, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2011.0, 10, 1), 'Constellations'
    : 1, 'SMP'
    : 0, 'Cluster'
    : 409, 'MPP'
    : 90, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2012.0, 5, 1), 'Constellations'
    : 0, 'SMP'
    : 0, 'Cluster'
    : 406, 'MPP'
    : 94, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2012.0, 10, 1), 'Constellations'
    : 0, 'SMP'
    : 0, 'Cluster'
    : 407, 'MPP'
    : 93, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2013.0, 5, 1), 'Constellations'
    : 0, 'SMP'
    : 0, 'Cluster'
    : 417, 'MPP'
    : 83, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2013.0, 10, 1), 'Constellations'
    : 0, 'SMP'
    : 0, 'Cluster'
    : 423, 'MPP'
    : 77, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2014.0, 5, 1), 'Constellations'
    : 0, 'SMP'
    : 0, 'Cluster'
    : 427, 'MPP'
    : 73, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2014.0, 10, 1), 'Constellations'
    : 0, 'SMP'
    : 0, 'Cluster'
    : 415, 'MPP'
    : 85, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2015.0, 5, 1), 'Constellations'
    : 0, 'SMP'
    : 0, 'Cluster'
    : 414, 'MPP'
    : 86, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2015.0, 10, 1), 'Constellations'
    : 0, 'SMP'
    : 0, 'Cluster'
    : 426, 'MPP'
    : 74, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2016.0, 5, 1), 'Constellations'
    : 0, 'SMP'
    : 0, 'Cluster'
    : 431, 'MPP'
    : 69, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2016.0, 10, 1), 'Constellations'
    : 0, 'SMP'
    : 0, 'Cluster'
    : 432, 'MPP'
    : 68, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2017.0, 5, 1), 'Constellations'
    : 0, 'SMP'
    : 0, 'Cluster'
    : 432, 'MPP'
    : 68, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2017.0, 10, 1), 'Constellations'
    : 0, 'SMP'
    : 0, 'Cluster'
    : 437, 'MPP'
    : 63, 'SIMD'
    : 0,
    },
    {
        'Single Processor'
        : 0, 'List': (2018.0, 5, 1), 'Constellations'
    : 0, 'SMP'
    : 0, 'Cluster'
    : 437, 'MPP'
    : 63, 'SIMD'
    : 0,
    },

]
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("data",cell_overwrite_ok=True)
sheet2 = workbook.add_sheet('dataPercent')
sheet.write(0,0,'date')
sheet.write(0,1,'Single Processor')
sheet.write(0,2,'Constellations')
sheet.write(0,3,'SMP')
sheet.write(0,4,'Cluster')
sheet.write(0,5,'MPP')
sheet.write(0,6,'SIMD')
sheet2.write(0,0,'date')
sheet2.write(0,1,'Single Processor')
sheet2.write(0,2,'Constellations')
sheet2.write(0,3,'SMP')
sheet2.write(0,4,'Cluster')
sheet2.write(0,5,'MPP')
sheet2.write(0,6,'SIMD')
date=[]
SingleProcessor=[]
Constellations=[]
SMP=[]
Cluster=[]
MPP=[]
SIMD=[]
for i in range(len(chartData)):
    for key in chartData[i]:
        if key == 'List':
            sheet.write(i+1,0,str(chartData[i][key]))
            sheet2.write(i+1,0,str(chartData[i][key]))
            date.append(str(chartData[i][key]))
        elif key ==  'Single Processor':
            sheet.write(i+1,1,chartData[i][key])
            sheet2.write(i+1,1,chartData[i][key] / 500)
            SingleProcessor.append(chartData[i][key] / 500)
        elif key ==  'Constellations':
            sheet.write(i+1,2,chartData[i][key])
            sheet2.write(i+1,2, chartData[i][key] / 500)
            Constellations.append(chartData[i][key] / 500)
        elif key == 'SMP':
            sheet.write(i+1,3,chartData[i][key])
            sheet2.write(i+1, 3, chartData[i][key] / 500)
            SMP.append(chartData[i][key] / 500)
        elif key ==  'Cluster':
            sheet.write(i+1,4,chartData[i][key])
            sheet2.write(i+1, 4, chartData[i][key] / 500)
            Cluster.append(chartData[i][key] / 500)
        elif key == 'MPP':
            sheet.write(i+1,5,chartData[i][key])
            sheet2.write(i+1, 5, chartData[i][key] / 500)
            MPP.append(chartData[i][key] / 500)
        elif key == 'SIMD':
            sheet.write(i+1,6,chartData[i][key])
            sheet2.write(i+1, 6, chartData[i][key] / 500)
            SIMD.append(chartData[i][key] / 500)
        else:
            sheet.write(i+1,7,'error')
# workbook.save("data.xls")
sum1 = []
sum2 = []
sum3 = []
sum4 = []
N = len(date)
year = []
ind = np.arange(N)    # the x locations for the groups
width = 0.8       # the width of the bars: can also be len(x) sequence
for i in range(N):
    sum1.append( SingleProcessor[i]+SMP[i])
for i in range(N):
    sum2.append( SingleProcessor[i]+SMP[i]+MPP[i])
for i in range(N):
    sum3.append( SingleProcessor[i]+SMP[i]+MPP[i]+SIMD[i])
for i in range(N):
    sum4.append( SingleProcessor[i]+SMP[i]+MPP[i]+SIMD[i]+Constellations[i])
for i in range(N):
    if i%2==0:
         year.append( re.search( '[0-9]{4}',(date[i])).group())
    else:
        year.append('')
print(type(year[0]))
half_year = []
for i in year:
     half_year.append(i[2:])

p1 = plt.bar(ind, SingleProcessor, width,color='salmon')
# plt.text(0,0.02,'Single \n Proc.',color='red',fontweight='bold')
p2 = plt.bar(ind, SMP, width, bottom=SingleProcessor)
# plt.text(4,0.25,'SMP',color='blue',fontweight='bold',fontsize=15)
p3 = plt.bar(ind, MPP, width, bottom=sum1,color='violet')
# plt.text(6,0.7,'MPP',color='PURPLE',fontweight='bold',fontsize=15)
p4 = plt.bar(ind, SIMD, width, bottom=sum2,color='lightgreen')
# plt.text(0.5,0.95,'SIMD',color='GREEN',fontweight='bold',fontsize=15)
p5 = plt.bar(ind, Constellations, width, bottom=sum3,color='skyblue')
# plt.text(12,0.8,'Constellations',color='deepskyblue',fontweight='bold',fontsize=15)
p6 = plt.bar(ind, Cluster, width, bottom=sum4,color='gold')
# plt.text(35,0.6,'Cluster',color='yellowgreen',fontweight='bold',fontsize=15)

# plt.ylabel('Scores')
# plt.title('$ARCHITECTURES$',fontsize='xx-large',fontweight='bold')
plt.xticks(ind, half_year) #
# plt.yticks(np.arange(0, 1.2 , 0.1))
plt.yticks([0.2,0.4,0.6,0.8,1],['20%','40%','60%','80%','100%'])
#plt.legend((p1[0], p2[0],p3[0], p4[0],p5[0], p6[0]), ('SingleProcessor', 'SMP','MPP','SIMD','Constellations','Cluster'),loc='upper right')
plt.show()
