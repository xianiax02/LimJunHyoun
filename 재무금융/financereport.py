import pandas as pd
import FinanceDataReader as fdr
import matplotlib as mat
from pandas_datareader import data as wb
import numpy as np
import datetime
#설명: MDD함수, 수익률변동성함수,

#장부 임포트
book=pd.read_excel('거래장부.xlsx')
# print(book)
#기업명, 코드 대조 딕셔너리
trans={'파마리서치':'214450','태경비케이':'014580','단기채권':'153130','달러선물인버스':'261260','500':'379800','롯데정밀화학':'004000','삼성전자':'005930','메가스터디':'072870','메가스터디교육':'215200','KOSPI200':'KS200','KOSDAQ':'KQ11'}
#volatility, MDD, Sharp ratio, information ratio, compensated ratio/ function
class finance:
    def __init__(self,name,startdate):
        self.name=name
        self.code=trans[name]
        self.startdate=startdate
P=finance('파마리서치','2022-10-14')
T=finance('태경비케이','2022-10-14')
B=finance('단기채권','2022-10-14')
D=finance('달러선물인버스','2022-10-14')
F=finance('500','2022-10-14')
L=finance('롯데정밀화학','2022-10-14')
S=finance('삼성전자','2022-10-14')
M=finance('메가스터디','2022-11-29')
ME=finance('메가스터디','2022-12-02')
KP=finance('KOSPI200','2022-10-14')
KD=finance('KOSDAQ','2022-10-14')
list=[P,T,B,D,F,L,S,M,ME]
#잔고
remainders={P:480,T:17300,B:490,D:1310,F:2182,L:500,S:300,M:0,ME:504}
def table(a):
        table=fdr.DataReader(a.code,a.startdate)
        return table

def volatility(a):
    t1=table(a)
    V=np.std(t1['Change'])*100
    return V

def MDD(a):
    t1=table(a)
    MDDtage=(t1['Close'].cummin()/t1['Close'].cummax()-1)*100
    return MDDtage
#해당종목 거래 내역 추출
def extract(a):
    count=0
    table=pd.DataFrame([(0,0,0,0)],columns=['Date','Method','Price','Quantity'])
    for i in range(book.shape[0]):
        if book.loc[i,'종목']==a.name:
            sample=[book.loc[i,'날짜'],book.loc[i,'거래'],book.loc[i,'실행가격'],book.loc[i,'수량']]
            table.loc[count]=sample
            count+=1
    return table
#거래한 수익률 계산-->거래 일별 실현손익
def earnrate(a):
    table1=pd.DataFrame([(0,0,0)],columns=['Date','Profit','earnrate'])
    profit=0
    invest=1
    earnrate=0
    comptable=extract(a)
    for i in range(comptable.shape[0]):
        if comptable.loc[i,'Method']=='buy':
            profit-=comptable.loc[i,'Price']*comptable.loc[i,'Quantity']
            invest+=comptable.loc[i,'Price']*comptable.loc[i,'Quantity']
        else:
            profit+=comptable.loc[i,'Price']*comptable.loc[i,'Quantity']
        if invest!=1:
            earnrate=(profit/(invest-1))*100
            table1.loc[i]=[comptable.loc[i,'Date'],profit,earnrate]

        
    #오늘 날짜
    # today=datetime.date.today()
    today='2022-12-05'
    profit+=table(a).loc[str(today),'Close']*float(remainders[a])
    table1.loc[table1.shape[0]+1]=[str(today)+' 00:00:00',profit,(profit/invest)*100]
    return table1
    
#전체 수익률 구하는 함수
def profit():
    profit=0
    list=[P,T,B,D,F,L,S,M,ME]
    for a in list:
        profit+=earnrate(a).iloc[-1,1]
    profitrate=profit/5000000 
    return profitrate

def profit1():
    profit=0
    profitrate=0
    list=[P,T,M,ME]
    for a in list:
        profit+=earnrate(a).iloc[-1,1]
        profitrate+=earnrate(a).iloc[-1,2]
    return profitrate

def profit2():
    profit=0
    profitrate=0
    list=[L,S]
    for a in list:
        profit+=earnrate(a).iloc[-1,1]
        profitrate+=earnrate(a).iloc[-1,2]
    return profitrate

#표준편차 더하는 함수
def stdplus():
    dailyreturn=pd.DataFrame([(0)],columns=['dailyreturn'])
    list=[P,T,B,D,F,L,S,M,ME]
    #list=['파마리서치','태경비케이','단기채권','달러선물인버스','500','롯데정밀화학','삼성전자','메가스터디','메가스터디교육']
    for a in list:
        comptable=table(a)
        for i in range(comptable.shape[0]):
            dailyreturn.loc[i]+=comptable.iloc[i,5]
            dailyreturn.loc[i+1]=0
    dailyreturn=dailyreturn.iloc[0:-2]
    volatilitysum=np.std(dailyreturn['dailyreturn'])
    return volatilitysum
#kosdaq
def stdplus1():
    dailyreturn=pd.DataFrame([(0)],columns=['dailyreturn'])
    list=[P,T,M,ME]
    #list=['파마리서치','태경비케이','단기채권','달러선물인버스','500','롯데정밀화학','삼성전자','메가스터디','메가스터디교육']
    for a in list:
        comptable=table(a)
        for i in range(comptable.shape[0]):
            dailyreturn.loc[i]+=comptable.iloc[i,5]
            dailyreturn.loc[i+1]=0
    dailyreturn=dailyreturn.iloc[0:-2]
    volatilitysum=np.std(dailyreturn['dailyreturn'])
    return volatilitysum
#KOSPI
def stdplus2():
    dailyreturn=pd.DataFrame([(0)],columns=['dailyreturn'])
    list=[L,S]
    #list=['파마리서치','태경비케이','단기채권','달러선물인버스','500','롯데정밀화학','삼성전자','메가스터디','메가스터디교육']
    for a in list:
        comptable=table(a)
        for i in range(comptable.shape[0]):
            dailyreturn.loc[i]+=comptable.iloc[i,5]
            dailyreturn.loc[i+1]=0
    dailyreturn=dailyreturn.iloc[0:-2]
    volatilitysum=np.std(dailyreturn['dailyreturn'])
    return volatilitysum

#포트폴리오 누적 수익률-KOSPI누적 수익률 /VOLATILTY(포트폴리오 전체)
def sharp():
    benchmark=10.72
    result=(profit()-benchmark)/(stdplus()*100)
    return result

def sharp1():
    benchmark=10.72
    result=(profit1()-benchmark)/(stdplus1()*100)
    return result

def sharp2():
    benchmark=10.97
    result=(profit2()-benchmark)/(stdplus2()*100)
    return result


#각각 일별 수익률 더해서 전체 표준편차 더하기

# for a in list:
#     MDD(a).to_excel('MDD'+str(a.name)+'.xlsx')
#     print(volatility(a))
#     earnrate(a).to_excel('수익분석표'+str(a.name)+'.xlsx')
# print(profit1())
# print(profit2())
# print(sharp())
# print(sharp1())
# print(sharp2())
print(profit())






