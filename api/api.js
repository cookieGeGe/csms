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

//首页统计接口
export function indexCount() {
    return request({
        url: '/wechat/count',
        method: 'get',
        data: {}
    })
}

// 首页和列表页面项目查询
export function queryProject(params) {

    /*
    params = {
        id: 'int		为0时表示首页和列表页面查询,否则为查询某一个具体的项目信息（id为0时后面的参数无效）',
        name: 'str	搜索关键字',
        type: 'int	企业类型',
        status: 'int		企业状态',
        area: 'list        区域对象列表',
        time: 'str		查询起始时间',
        page: 'int		页码',
    }
    */
    return request({
        url: '/user/login',
        method: 'get',
        data: params
    })
}

// 首页和列表页面企业查询
export function queryCompany(params) {
    /*
    params = {
        id: 'int		为0时表示首页和列表页面查询,否则为查询某一个具体的企业信息（id为0时后面的参数无效）',
        name: 'str	搜索关键字',
        type: 'int	企业类型',
        status: 'int		企业状态',
        area: 'list        区域对象列表',
        time: 'str		查询起始时间',
        page: 'int		页码',
    }
    */
    return request({
        url: '/user/login',
        method: 'get',
        data: params
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
        url: '/user/login',
        method: 'get',
        data: params
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
        url: '/user/login',
        method: 'get',
        data: params
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
        url: '/user/login',
        method: 'get',
        data: params
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
        url: '/user/login',
        method: 'get',
        data: params
    })
}


