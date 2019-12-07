/**
 * Created by 16288 on 2019/11/20.
 */
import request from '@/utils/request'

export function login(params) {
    return request({
        url: '/user/login',
        method: 'post',
        data: params
    })
}

// 企业中获取项目信息
export function queryGroupPics(params) {
    /*
    params = {
        id: 'int	    分组ID'
    }
    */
    return request({
        url: '/wechat/query/pics',
        method: 'get',
        params: params
    })
}

//首页统计接口
export function indexCount() {
    return request({
        url: '/wechat/count',
        method: 'get',
        params: {}
    })
}

// 首页和列表页面项目查询
export function queryProject(params) {

    /*
    params = {
        id: 'int		为0时表示首页和列表页面查询,否则为查询某一个具体的项目信息（id为0时后面的参数无效）',
        name: 'str	搜索关键字',
        type: 'int	类型',
        status: 'int		状态',
        area: 'list        区域对象列表',
        time: 'str		查询起始时间',
        page: 'int		页码',
    }
    */
    return request({
        url: '/wechat/query/project',
        method: 'get',
        params: params
    })
}

// 首页和列表页面项目查询
export function queryProgress(params) {

    /*
    params = {
        id: 'int	进度ID',
    }
    */
    return request({
        url: '/wechat/query/progress',
        method: 'get',
        params: params
    })
}

// 首页和列表页面企业查询
export function queryCompany(params) {
    /*
    params = {
        id: 'int		为0时表示首页和列表页面查询,否则为查询某一个具体的信息（id为0时后面的参数无效）',
        name: 'str	搜索关键字',
        type: 'int	类型',
        status: 'int		状态',
        area: 'list        区域对象列表',
        time: 'str		查询起始时间',
        page: 'int		页码',
    }
    */
    return request({
        url: '/wechat/query/company',
        method: 'get',
        params: params
    })
}

// 企业中获取项目信息
export function queryCompanyProject(params) {
    /*
    params = {
        id: 'int		企业ID',
        page: 'int		页码',
    }
    */
    return request({
        url: '/wechat/query/company/project',
        method: 'get',
        params: params
    })
}

// 首页和列表页面劳工查询
export function queryLabor(params) {
/*
    params = {
        id: 'int		为0时表示首页和列表页面查询,否则为查询某一个具体的企业信息（id为0时后面的参数无效）',
        name: 'str	搜索关键字',
        sex: '0,1,2   2表示所有，0为男， 1为女',
        jobtype: '0-5 工种类型，默认为5全部工种',
        education: '0-7 学历，默认为7全部学历',
        age: '0-6 年龄段，默认为7全部年龄段',
        type: 'int	企业类型',
        status: 'int		企业状态',
        area: 'list        区域对象列表',
        time: 'str		查询起始时间',
        page: 'int		页码',
    }
*/
    return request({
        url: '/wechat/query/labor',
        method: 'get',
        params: params
    })
}

// 考勤查询
export function queryAttend(params) {
/*
    params = {
        name: 'str	搜索关键字',
        type: 'str	company或者project或者labor',
        area: 'list        区域对象列表',
        days: 'int		最低打卡天数（type为labor时有效）',
        month: 'str		查询考勤年月格式为：xxxx-xx（type为labor时有效）',
        page: 'int		页码',
    }
*/
    return request({
        url: '/wechat/query/attend',
        method: 'get',
        params: params
    })
}

// 考勤查询
export function queryAttendInfo(params) {
/*
    params = {
        id: 'int	劳工ID',
        year: 'int		年',
        month: 'int		月',
    }
*/
    return request({
        url: '/wechat/query/attend/info',
        method: 'get',
        params: params
    })
}

// 考勤查询
export function querySalary(params) {
/*
    params = {
        id: 'int    是搜索还是获取某一个id的详情，id为0时参数：name,type,area，page才会生效
        name: 'str	搜索关键字',
        type: 'str	company或者project或者labor',
        area: 'list        区域对象列表',
        month: 'str		查询考勤年月格式为：xxxx-xx（type为labor时有效）',
        page: 'int		页码',
    }
*/
    return request({
        url: '/wechat/query/salary',
        method: 'get',
        params: params
    })
}

// 银行查询
export function queryBank(params) {
/*
    params = {
        id:    'int   默认为0,  为0时是主页搜索',
        bank: 'int    银行ID，默认为0',
        name: 'str    搜索关键字',
        time: 'str    时间字符串',
        area: 'list   区域对象列表',
        page: 'int    页码',
    }
*/
    return request({
        url: '/wechat/query/bank',
        method: 'get',
        params: params
    })
}

// 工资查询
export function queryBankInfo(params) {
/*
    params = {
        id:    'int   月份对应的ID',
    }
*/
    return request({
        url: '/wechat/query/bank/info',
        method: 'get',
        params: params
    })
}

// 保函查询
export function queryGuarantee(params) {
/*
    params = {
        id:    'int   默认为0,  为0时是列表搜索',
        name: 'str    搜索关键字',
        type: 'int    保函类型',
        area: 'list   区域对象列表',
        page: 'int    页码',
    }
*/
    return request({
        url: '/wechat/query/guarantee',
        method: 'get',
        params: params
    })
}

// 保函查询
export function queryQuestion(params) {
/*
    params = {
        id:    'int   默认为0,  为0时是列表搜索, 不为0时为问题详情搜索',
        name: 'str    搜索关键字',
    }
*/
    return request({
        url: '/wechat/query/question',
        method: 'get',
        params: params
    })
}


