import datetime
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import FinanceDataReader as fdr
import matplotlib as mat
#date,time, timedelta,datetime
day=datetime.date{2020,5,15}#클래스로 인스턴스 생성
today=datetime.date.today()
time=datetime.time(14,25,32)#14시 25분 32초
duration=datetime.timedelta(days=7)
#duration*2하면 datetime.timedelta(days=14)의 인스턴스가 됨
whattimeisdurationaftertoday=today+duration
datetime_dt=datetime.datetime.strptime('2015-2-14 16:23:45','%Y-%m-%d %H:%M:%S')#스트링을 객체로
datetime_str=datetime_dt.strftime('%Y-%m-%d %H:%M:%S')#객체를 스트링으로
##lecture 2
today2=np.datetime64('2021-12-02 15:33:12')
an_day=np.datetime64(10000,'s')#1970.1.1.0:0:0에서 부터 만초 지난 시간 월-'M' 일 'D'
a2=np.array(['2021-12-01','2021-12-02','2021-12-03', dtype='datetime64'])#벡터 도입,타입이 데이트임을 명시함으로써 스트링이 아닌 날짜로 인스턴스 생성
b2=np.arrange(1,100,2)#(1부터 100까지 2간격 리스트 생성) 
c2=np.arrange('2020-11-01','2021-12-03',dtype='datetime64[D]')#(날짜 부터 날짜까지 하루간격 리스트 생성) 
d2=np.datetime64('2021-12-03')-np.datetime64('2020-10-15')#-->np.timedelta64(414,'D')
##lecture 3-->timestamp,period
a3=pd.Timestamp('2020-12-12 11:22:33')#ISO방식 날짜 생성
b3=pd.Timestamp(1000, unit='D')#UTC method
c3=pd.to_datetime('2021-1-2 11:33:55')#똑같이 타임스탬프 인스턴스 생성 대신 이건 리스트 받을 수 있음
d3=pd.to_datetime(['2020-01-01','2021-02-25'])#->Datetimeindex 인스턴스 만들어줌
e3=pd.date_range('2020-1','2021-12',freq='M')#언제부터 언제까지 프리권시 만큼(없으면 기본 일, 'D'는 영업일,'W'일요일(위켄드))
f3=pd.Period('2021-12-15','D')
f3.start_time#해당 기간 시작 시점 
f3.end_time#해당 기간 끝나는 시점
g3=pd.period_range('2020-3-5','2020-8-20',freq='M')#주기의 범위를 알려줌 --> 해당 날짜 사이에 주기가 몇번 있는지 알려줌 기본은 'D'->1일)
##lecture 4-->series
a4=pd.Series([80000,90000,200000,120000])#값(value)는 필수 이것만 쓰면 0,1,2,3의 인덱스에 값이 저장됨
print(a4[2])#-->200000
b4=pd.Series([80000,90000,200000,120000], index=['삼성전자','기아','현대차','카카오'])
#슬라이싱의 경우..숫자면 a<=,<=b-1, 한글이면 a<=,<=b
c4=b4[b4<10000]#-->b4<10000 일때 True 인 값만 반환해줌
d4=b4*2#산술연산도 됨
##lecture 5-->dataframe
a5=pd.DataFrame({'가격':[80000,250000,70000,120000],'거래량':[8000,25000,7000,1000]},index=['삼성전자','현대차','기아','카카오']})
##lecture6
sa_pr=wb.DataReader('005930.KS', data_source='yahoo',start='2021-1-1')
sa_pr_1=fdr.DataReader('005930','2020-1-1')
##lecture7--> indexing:[],loc[],iloc[]
a7=sa_pr['open']# type series
b7=a7['2021-01-08']#그 당시 값
a7=sa_pr['open','close']#-->2개이상이면 데이터프레임 나옴
c7=a7[0:5]#0~4행이 나옴
##lecture 8-->loc,iloc
a8=sa_pr.loc['2021-01-08',['High','Low']]
b8=sa_pr.loc['2021-01-08']#해당 행의 모든 열 갖고 옴
c8=sa_pr.loc[:,'open']#해당 열의 모든 행 갖고 옴
d8=sa_pr.iloc[0,1:3]
e8=sa_pr.iloc[0]#해당 행의 모든 열 갖고 옴
f8=sa_pr.iloc[:,3]#해당 열의 모든 행 갖고 옴
##lecture 9--> .isna 결측치 확인 .isin,np.in,-np.inf,np.nan
s1=pd.Series([np.nan,2,3,4,5])
s2=pd.Series([1,2,np.nan,np.nan,5])#not a number
s3=pd.Series([1,2,3,4,5])
df=pd.DataFrame({'s1':s1,'s2':s2,'s3':s3})
df['s1'].isna()#nan이면 True, 아니면 False
df.isna.sum()#True 를 1로 계산하여 더함
df.isin([np.nan,np.inf,-np.inf]).sum()
df.dropna()#na 있는 행을 아예 없앰
df.dropna(axis='columns')#열을 없앰
df.fillna(9)#na값을 모두 9로 바꾼다
df.fillna(method='pad')#앞의 숫자로 nan을 채움 method=bfill 뒤에 있는 값으로 채움
##lecture 10-->시계열 데이터 분석 shift
df=fdr.DataReader('AAPL','2021')#영업일 기준으로 나옴
df['close_early2']=df['Close'].shift(-2)#(열 새로 생성/n항뒤 숫자없으면 1)
##lecture 11 수익률 계산pct_change
df['pct_change']=df['close'].pct_change(2)#n만큼 전의 값을 빼서 n전 값으로 나눔-->기본은 1
##lecture 12 변화량 diff(n) a-b(a의 n칸 위)
df['close_diff']=df['close'].diff(2)#axis=0이 default(행이 2개 이동)/axis=1(열방향으로 이동)시에는 앞이 series가 아니라 다른 열이 있는 dataframe 이여야함을 주의
##lecture 13 이동평균(6일의 5일 이동 평균->2일부터 6일까지 5일간의 평균)
a=df['close'].rolling(window=5)#=>묶인 rolling 객체 형성
df['5dayaverage']=a.mean#==>묶인 것에 대한 이동평균
df['5daymax']=a.max()#5일간 가장 큰 값 보여줌
#lecture 14 날짜단위 바꾸기 resample /downsampling,upsampling
df.resample(rule='M').mean()#종가 평균을 달의 값으로 이용해 다운샘플링해본다 //'MS'는 월초, 'M'은 월말
#lecture 15 주식 수익률 계산
df['dailyreturn']=df['close'].pct_change()
#첫날 매도/매수-1에 각 날짜의 값에 1더해서 누적곱
df['st_rtn']=(1+df['dailyreturn']).cumprod()
startdate='2021-01-01'
enddate='2021-01-14'
tmp_df=df.loc[startdate:enddate,['st_rtn']]/df.loc[startdate,['st_rtn']]#새로운 데이터프레임제작
#lecture 17 최대낙폭지수
historicalmdd=df['close'].min()/df['close'].cummax()-1#하면 됨
#lecture 18 변동성 계산 표준편차 std 함수
df18=fdr.DataReader('AAPL','2020')
start='2021-06-13'
end='2022-02-03'
tmp_df=df.loc[start:end]
Volatlity=np.std(tmp_df['Change'])
#lecture 19 샤프비율 샤프지수
Sharp=np.mean(tmp_df)['Change']/Volatlity

