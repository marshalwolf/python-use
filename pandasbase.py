#coding=utf-8
import numpy as np
import pandas as pd
import pylab

def main():
	#Data Structure
	s=pd.Series([i*2 for i in range(1,11)])
	print type(s)

	dates=pd.date_range("20180630", periods=8)
	df=pd.DataFrame(np.random.randn(8,5), index=dates,columns=list("ABCDE"))
	print df
	#基本操作
	print df.head(3)
	print df.tail(3)
	print df.index
	print df.values
	print df.T
	#print df.sort(columns="C")
	#print df.sort_index(axis=1,ascending=False)
	print df.describe()
	#切片
	print df["A"]
	print df[:3]
	print df["20180630":"20180702"]
	print df.loc[dates[0]] #直接取0630的数据
	print df.loc["20180630":"20180702",["B","D"]]
	print df.at[dates[0], "C"]
	print df.iloc[1:3,2:4]
	print df.iat[1,4]
	print df[df.B>0][df.A<0]
	#set
	s1=pd.Series(list(range(10,18)),index=pd.date_range("20180630",periods=8))
	df["F"]=s1
	print df
	df2=df.copy()
	print df2
	#Missing Values
	df1=df.reindex(index=dates[:4],columns=list("ABCD")+["G"])
	df1.loc[dates[0]:dates[1], "G"]=1
	print df1
	print df1.dropna()
	print df1.fillna(value=1)
	#Statistic
	print df.mean() #平均值
	print df.var() #方差
	s = pd.Series([1,2,4,np.nan,5,7,9,10], index=dates)
	print s
	print s.shift(2)
	print s.diff()
	print s.value_counts()
	#Concat
	pieces=[df[:3],df[-3:]]
	print pd.concat(pieces)

	left=pd.DataFrame({"key":["x","y"], "value":[1,2]})
	right=pd.DataFrame({"key":["x","z"], "value":[3,4]})
	print "LEFT:",left
	print "RIGHT:",right
	print pd.merge(left,right,on="key",how="left")
	df3 = pd.DataFrame({"A": ["a", "b", "c", "b"],"B": list(range(4))})
	print df3.groupby("A").sum()
	#Time Series
	t_exam=pd.date_range("20180630", periods=10,freq="S")
	print (t_exam)
	#Graph
	ts=pd.Series(np.random.randn(1000),index=pd.date_range("20180630",periods=1000))
	ts=ts.cumsum()
	from pylab import *
	ts.plot()
	show()
	#File
	df6=pd.read_csv("./myproject/test.csv")
	print df6
	df7=pd.read_excel("./myproject/test.xlsx","Sheet1")
	print df7
	df6.to_csv("./myproject/test2.csv")
	df7.to_excel("./myproject/test2.xlsx")
if __name__=="__main__":
	main()