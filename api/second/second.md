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

/bankinfo/add 		post

​	id	新增时为0，编辑时为编辑的银行ID（必填）

​	name	银行名称（必填）

​	description	银行描述



查询银行接口：

/bankinfo/query		get

​	name	银行名称

​	page	页数（必填）

​	pagesize	每页大小（必填）

返回值：{

​	“data”: [],

​	"total": 0

}



删除银行接口：

/bankinfo/delete	delete

​	ID	银行ID（必填）






