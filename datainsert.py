#insert Pinter
from protein.models import Pinter, Panno
import csv

with open('/Users/johnnyliu/Documents/pfunction/ppf/pinter.csv', encoding='mac_roman', newline='')as csvfile:
    spamreader=csv.reader(csvfile, delimiter='\t')
    D=list(spamreader)


for d in D:
    q=Pinter(OSFA=d[2], OSFB=d[3])
    q.save()

#insert Panno
from protein.models import Pinter, Panno
import csv

with open('/Users/johnnyliu/Documents/pfunction/ppf/panno.csv', encoding='mac_roman', newline='')as csvfile:
    spamreader=csv.reader(csvfile, delimiter='\t')
    D=list(spamreader)


for d in D:
    q=Panno(genename=d[2], genefunc=d[4], genefunc_disc=d[9])
    q.save()
