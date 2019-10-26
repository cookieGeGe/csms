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
subCompany : [
	{
		ID: 企业1的ID,
		Person: 企业负责人
	}，
	{
		ID: 企业2的ID,
		Person: 企业负责人
	}，
]


Account		银行卡号
```



新建和编辑项目进度：

```
Connect		项目联系人（联系人字符串）	str
Workers		用工人数	int
ShouldIssues	应发放数	str
RealIssues		实际发放数	str
Payment			支付款项	str
Overdraft		欠款		str
TotalSalary		总工资		str
```



项目进度中获取项目下所有劳工：

```
/labor/one/project		get		获取一个项目下的所有劳工（项目ID38下有两个劳工，没有头像）
请求参数：
	projectid	项目ID	int
返回值：
	{
		data:[
			{
				id:劳工ID	int,
				name:劳工姓名 str,
				avatar:劳工头像 str	图片链接地址
			}
		]
	}
```





项目详情中：

```
SubCompany:	list    {ID：企业id，CompanyName:企业名称,  Person:负责人，Status: 状态（1为不良，0为正常）}
Bank		银行id
BankName		银行名称
BuildStatus		建设方是否不良（1为不良，0为正常）
ConsStatus		施工方是否不良（1为不良，0为正常）
```



项目进度中获取项目联系人接口：

```
/project/progress/connect		get

	ID 项目ID int

返回数据:
	connect_list		list  ['person1', 'person2']  多个联系人字符串
```





项目进度中获取图片分组接口：

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



劳工新建、编辑：

```
增加字段：
	SubCompany	分包公司ID	int
	Isbadrecord		不良分类（0-2代表正常，不良，黑名单） int
	BadRecord	不良信息备注		str
修改字段:
	Train	劳工是否培训（0表示未培训，不上传图片）		int
    
```

劳工详情

```
增加返回字段：
	isDeparture		bool	劳工是否离场，离场为true
```





权限：

```
增加权限：
	permission_show		查看权限管理
	labor_badrecord_show	查看劳工不良信息
	labor_badrecord_edit	编辑劳工不良信息
```



首页：

```
/index/info
增加返回值：
	bankinfo:[
		{
			id: 4
            name: "瑞士银行S"		银行名称
            totalcards: 2			银行卡数
            totalpay: 2042			代发项目金额
            totalproject: 7			代发项目数
		},
	]
```




