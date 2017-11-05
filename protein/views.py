from __future__ import division
from django.shortcuts import render, redirect
from django.template import loader
from protein.models import Pinter, Panno
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from collections import Counter, OrderedDict
import operator


def index(request):
    template=loader.get_template('protein/index.html')
    if request.method=='GET':
        p=request.GET.get('p_name')
        mininter=request.GET.get('mininter')
        if mininter=='':
            mininter=10
        else:
            pass
        
        P=p
        R1=list(Pinter.objects.filter(OSFA=p).values_list('OSFB', flat=True))
        R2=list(Pinter.objects.filter(OSFB=p).values_list('OSFA', flat=True))
        R=R1+R2
        if R == []:
            no_of_relate_gene=0
            warning=""
        else:
            R=list(set(R))
            no_of_relate_gene=len(R)
            if no_of_relate_gene < mininter:
                warning="The results below doesn't meet the minimum number of physical interactions request!"
            else:
                warning=""
                
        f=[]
        for i in R:
            f=f+list(Panno.objects.filter(genename=i).values_list('genefunc', flat=True))
        l=len(f)
        c=OrderedDict(Counter(f))
        c=sorted(c.items(), key=operator.itemgetter(1), reverse=True)
        c=c[:5]
        if c==[]:
            pf1=pf2=pf3=pf4=pf5=''
            prob1=prob2=prob3=prob4=prob5=0
        else:
            pf1=c[0][0]
            prob1="{0:.2f}".format(c[0][1]/l)
            pf2=c[1][0]
            prob2="{0:.2f}".format(c[1][1]/l)
            pf3=c[2][0]
            prob3="{0:.2f}".format(c[2][1]/l)
            pf4=c[3][0]
            prob4="{0:.2f}".format(c[3][1]/l)
            pf5=c[4][0]
            prob5="{0:.2f}".format(c[4][1]/l)
        return render(request, 'protein/index.html', {'mininter': mininter, 'c': c, 'l': l, 'P': P, 'warning': warning, 'no_of_relate_gene': no_of_relate_gene, 'pf1':pf1, 'prob1': prob1, 'pf2':pf2, 'prob2': prob2, 'pf3':pf3, 'prob3': prob3, 'pf4':pf4, 'prob4': prob4, 'pf5':pf5, 'prob5': prob5})
    else:
        return render(request, 'protein/index.html')
        
