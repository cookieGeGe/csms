#### 二期修改

##### 2019-10-09

修改接口：
    
    /user/regist:
    增加字段：
        permission    权限类型位， 为1表示根据地区，为2表示根据项目 
        projectid   权限类型位为2时，必填，为项目ID
分包企业有多个，以列表的形式存在数据库字段中其中包括，企业ID，企业负责人

##### 2019-10-10

添加银行接口：

```
/bankinfo/add 		post

	id	新增时为0，编辑时为编辑的银行ID（必填）
	name	银行名称（必填）
	description	银行描述
```

查询银行接口：

```
/bankinfo/query		get

	id	查询具体银行的ID（必填，如果不是查询某个银行，是查询列表默认为0）
	name	银行名
	page	页数（必填）
	pagesize	每页大小（必填）

返回值：{
	“data”: [],
	"total": 0
}
```





删除银行接口：

/bankinfo/delete	delete

​	ID	银行ID（必填）



查询银行接口：

/bankinfo/allbank	get



##### 2019-10-13

企业增加其他信息接口：

```
OtherInfo 	其他信息
```

添加项目修改思路：

​	1.数据库添加银行外键

​	2.项目进度添加项目联系人字段

​	3.项目询问人更改结构

​	4.项目进度添加工资发放进度表格，

​	5.单独做一个工资发放进度表格页面



项目创建编辑中：

​	新增：

```
Bank		银行ID  int         
SubCompany	分包企业   list字符串   里面是多个企业对象包括，企业ID，Person企业负责人
Account		银行卡号
```



新建项目进度：

```
Connect		月联系人	str
Workers		用工人数	int
ShouldIssues	应发放数	str
RealIssues		实际发放数	str
Payment			支付款项	str
Overdraft		欠款		str
TotalSalary		总工资		str
```



项目详情中：

```
SubCompany:	list    {ID：企业id，CompanyName:企业名称,  Person:负责人，Status: 状态（1为不良，0为正常）}
Bank		银行id
BankName		银行名称
BuildStatus		建设方是否不良（1为不良，0为正常）
ConsStatus		施工方是否不良（1为不良，0为正常）
```



项目进度：

```
/project/progress/connect		get

返回数据:
	connect_list		list  ['person1', 'person2']
```

```	
/project/progrerss/pic/list		get (只需要修改图片链接就可以了)
请求参数：
	ID	分组的ID（必填）
	
返回数据： {
	pic_list: [
	{
		ID: 图片ID,
		GroupID: 分组ID,
		Purl:	大图路径,
		Name:	名称
	}
	]
}
```






