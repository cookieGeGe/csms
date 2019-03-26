/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2019/3/26 21:25:10                           */
/*==============================================================*/


drop table if exists Tb_Progress;

drop table if exists tb_area;

drop table if exists tb_attendance;

drop table if exists tb_badrecord;

drop table if exists tb_class;

drop table if exists tb_company;

drop table if exists tb_company_badrecord;

drop table if exists tb_guarantee;

drop table if exists tb_labor_badrecord;

drop table if exists tb_laborinfo;

drop table if exists tb_permission;

drop table if exists tb_pro_class;

drop table if exists tb_project;

drop table if exists tb_user;

drop table if exists tb_user_area;

drop table if exists tb_user_per;

drop table if exists tb_wage;

/*==============================================================*/
/* Table: Tb_Progress                                           */
/*==============================================================*/
create table Tb_Progress
(
   ID                   int not null auto_increment,
   ProjectID            int comment '项目ID',
   UploadTime           datetime comment '项目进度时间',
   Pictures             varchar(255) comment '施工方上传图片',
   Content              varchar(512) comment '进度报告',
   Status               int comment '项目状态',
   primary key (ID)
);

alter table Tb_Progress comment '项目进度表';

/*==============================================================*/
/* Table: tb_area                                               */
/*==============================================================*/
create table tb_area
(
   ID                   int not null auto_increment,
   Name                 varchar(50),
   FatherID             int,
   HasChild             int,
   primary key (ID)
);

alter table tb_area comment '地区表';

/*==============================================================*/
/* Table: tb_attendance                                         */
/*==============================================================*/
create table tb_attendance
(
   ID                   int not null auto_increment,
   LaborID              int comment '劳工ID',
   AttenTime            datetime comment '打卡时间',
   Remark               varchar(50) comment '备注',
   primary key (ID)
);

alter table tb_attendance comment '考勤记录表';

/*==============================================================*/
/* Table: tb_badrecord                                          */
/*==============================================================*/
create table tb_badrecord
(
   ID                   int not null auto_increment,
   Type                 int comment '不良记录类型',
   Description          varchar(255) comment '不良记录描述',
   RecordTime           datetime,
   primary key (ID)
);

alter table tb_badrecord comment '不良记录表';

/*==============================================================*/
/* Table: tb_class                                              */
/*==============================================================*/
create table tb_class
(
   ID                   int not null auto_increment,
   CompanyID            int comment '公司ID',
   ClassName            varchar(50) comment '班组名字',
   Description          varchar(255) comment '描述',
   primary key (ID)
);

alter table tb_class comment '班组表';

/*==============================================================*/
/* Table: tb_company                                            */
/*==============================================================*/
create table tb_company
(
   ID                   int not null auto_increment,
   Name                 varchar(255) comment '公司名字',
   Legal                varchar(255) comment '法人',
   Address              varchar(255) comment '公司地址',
   Phone                varchar(255) comment '联系方式',
   License              varchar(255) comment '营业执照',
   OtherPic             varchar(255) comment '公司照片',
   BadRecord            varchar(255) comment '不良记录',
   Type                 int comment '公司类型',
   primary key (ID)
);

alter table tb_company comment '企业公司表';

/*==============================================================*/
/* Table: tb_company_badrecord                                  */
/*==============================================================*/
create table tb_company_badrecord
(
   ID                   int not null auto_increment,
   CompanyID            int comment '公司ID',
   BadrecordID          int comment '不良记录ID',
   primary key (ID)
);

alter table tb_company_badrecord comment '公司不良记录表';

/*==============================================================*/
/* Table: tb_guarantee                                          */
/*==============================================================*/
create table tb_guarantee
(
   ID                   int not null auto_increment,
   ProjectID            int comment '项目ID',
   Number               varchar(255) comment '保函编号',
   CompanyID            int comment '担保公司ID',
   SignTime             datetime comment '合同签订日期',
   Validity             int comment '有效期（月）',
   Amount               varchar(255) comment '金额',
   Status               int comment '状态',
   Others               varchar(255) comment '附件',
   Category             int comment '担保类别',
   primary key (ID)
);

alter table tb_guarantee comment '保函表';

/*==============================================================*/
/* Table: tb_labor_badrecord                                    */
/*==============================================================*/
create table tb_labor_badrecord
(
   ID                   int not null auto_increment,
   LaborID              int comment '劳工ID',
   BadRecordID          int comment '不良记录ID',
   primary key (ID)
);

alter table tb_labor_badrecord comment '劳工不良记录表';

/*==============================================================*/
/* Table: tb_laborinfo                                          */
/*==============================================================*/
create table tb_laborinfo
(
   ID                   int not null auto_increment,
   Name                 varchar(50) comment '姓名',
   Age                  int comment '年龄',
   Sex                  int comment '性别(0表示女，1表示男)',
   Birthday             datetime comment '生日',
   Address              varchar(255) comment '地址',
   Nationality          varchar(25) comment '名族',
   IDCard               varchar(25) comment '身份证号码',
   Phone                varchar(20) comment '电话号码',
   CompanyID            int comment '公司ID',
   JobNum               varchar(25) comment '工号',
   ClassID              int comment '班组ID',
   WorkType             int comment '工种',
   Identity             int comment '身份（配置字典映射）',
   DepartureDate        datetime comment '离场日期',
   EntryDate            datetime comment '进场日期',
   Hardhatnum           varchar(50) comment '安全帽号',
   IDPhoto              varchar(255) comment '证件照片',
   ConPhoto             varchar(255) comment '合同照片',
   CloseupPhoto         varchar(255) comment '近身照片',
   Education            varchar(50) comment '学历',
   CreateTime           datetime comment '创建时间',
   primary key (ID)
);

alter table tb_laborinfo comment '劳工信息表';

/*==============================================================*/
/* Table: tb_permission                                         */
/*==============================================================*/
create table tb_permission
(
   ID                   int not null auto_increment,
   PerName              varchar(255) comment '权限名称',
   Permission           varchar(255) comment '权限',
   Description          varchar(255) comment '描述',
   FatherID             int comment '父ID',
   URLName              varchar(50) comment '子级URL',
   HasChild             int comment '是否有子目录',
   primary key (ID)
);

alter table tb_permission comment '权限表';

/*==============================================================*/
/* Table: tb_pro_class                                          */
/*==============================================================*/
create table tb_pro_class
(
   ID                   int not null auto_increment,
   ProjectID            int,
   ClassID              int,
   primary key (ID)
);

alter table tb_pro_class comment '项目班组表';

/*==============================================================*/
/* Table: tb_project                                            */
/*==============================================================*/
create table tb_project
(
   ID                   int not null auto_increment,
   Name                 varchar(255) comment '项目名称',
   Type                 int comment '项目类型',
   Duration             int comment '项目工期（单位：月）',
   Participants         int comment '参与人数',
   Price                varchar(255) comment '中标价格',
   GAmount              varchar(255) comment '担保金额',
   StartTime            datetime comment '开工时间',
   Address              varchar(255) comment '项目地址',
   OwnerManager         int comment '业主负责人',
   ConsManager          int comment '施工方负责人',
   Supervisor           int comment '监理负责人',
   LaborManager         int comment '劳务专员',
   LaborCompany         int comment '劳务公司',
   Pay                  int comment '项目支付情况',
   TotalPrice           varchar(255) comment '总产值',
   TotalPayment         varchar(255) comment '总领款',
   RealHair             varchar(255) comment '最终发放统计',
   Status               int comment '项目状态',
   WagePercent          varchar(50) comment '工资到账比例',
   CompanyID            int comment '所属公司ID',
   AreaID               int comment '县级区域ID',
   primary key (ID)
);

alter table tb_project comment '项目表';

/*==============================================================*/
/* Table: tb_user                                               */
/*==============================================================*/
create table tb_user
(
   ID                   integer not null auto_increment,
   LoginName            varchar(255) comment '登录名称',
   UserName             varchar(255) comment '用户名称',
   Password             varchar(255) comment '密码',
   Email                varchar(50) comment '邮箱',
   Phone                varchar(20) comment '电话',
   Desccription         varchar(255) comment '描述',
   AdminType            int comment '管理员类型（0表示超级管理员，1表示普通用户）',
   CompanyID            int comment '所属公司ID',
   primary key (ID)
);

alter table tb_user comment '用户表';

/*==============================================================*/
/* Table: tb_user_area                                          */
/*==============================================================*/
create table tb_user_area
(
   ID                   int not null auto_increment,
   UserID               int,
   AreaID               int,
   primary key (ID)
);

alter table tb_user_area comment '用户管理区域表';

/*==============================================================*/
/* Table: tb_user_per                                           */
/*==============================================================*/
create table tb_user_per
(
   ID                   int not null auto_increment,
   UID                  int comment '用户ID',
   PID                  int comment '权限ID',
   primary key (ID)
);

alter table tb_user_per comment '用户权限关联表';

/*==============================================================*/
/* Table: tb_wage                                               */
/*==============================================================*/
create table tb_wage
(
   ID                   int not null auto_increment,
   ProjectID            int comment '项目ID',
   January              int comment '（0表示全额到，1,表示部分到，2表示未到）',
   February             int,
   March                int,
   April                int,
   May                  int,
   June                 int,
   July                 int,
   August               int,
   September            int,
   October              int,
   November             int,
   December             int,
   primary key (ID)
);

alter table tb_wage comment '工资表';

alter table Tb_Progress add constraint FK_Reference_17 foreign key (ProjectID)
      references tb_project (ID) on delete restrict on update restrict;

alter table tb_class add constraint FK_Reference_10 foreign key (CompanyID)
      references tb_company (ID) on delete restrict on update restrict;

alter table tb_company_badrecord add constraint FK_Reference_6 foreign key (CompanyID)
      references tb_company (ID) on delete restrict on update restrict;

alter table tb_company_badrecord add constraint FK_Reference_7 foreign key (BadrecordID)
      references tb_badrecord (ID) on delete restrict on update restrict;

alter table tb_guarantee add constraint FK_Reference_15 foreign key (ProjectID)
      references tb_project (ID) on delete restrict on update restrict;

alter table tb_guarantee add constraint FK_Reference_16 foreign key (CompanyID)
      references tb_company (ID) on delete restrict on update restrict;

alter table tb_labor_badrecord add constraint FK_Reference_4 foreign key (LaborID)
      references tb_laborinfo (ID) on delete restrict on update restrict;

alter table tb_labor_badrecord add constraint FK_Reference_5 foreign key (BadRecordID)
      references tb_badrecord (ID) on delete restrict on update restrict;

alter table tb_laborinfo add constraint FK_Reference_11 foreign key (CompanyID)
      references tb_company (ID) on delete restrict on update restrict;

alter table tb_laborinfo add constraint FK_Reference_3 foreign key (ClassID)
      references tb_class (ID) on delete restrict on update restrict;

alter table tb_pro_class add constraint FK_Reference_12 foreign key (ClassID)
      references tb_class (ID) on delete restrict on update restrict;

alter table tb_pro_class add constraint FK_Reference_13 foreign key (ProjectID)
      references tb_project (ID) on delete restrict on update restrict;

alter table tb_project add constraint FK_Reference_14 foreign key (CompanyID)
      references tb_company (ID) on delete restrict on update restrict;

alter table tb_project add constraint FK_Reference_21 foreign key (AreaID)
      references tb_area (ID) on delete restrict on update restrict;

alter table tb_user add constraint FK_Reference_18 foreign key (CompanyID)
      references tb_company (ID) on delete restrict on update restrict;

alter table tb_user_area add constraint FK_Reference_19 foreign key (UserID)
      references tb_user (ID) on delete restrict on update restrict;

alter table tb_user_area add constraint FK_Reference_20 foreign key (AreaID)
      references tb_area (ID) on delete restrict on update restrict;

alter table tb_user_per add constraint FK_Reference_1 foreign key (UID)
      references tb_user (ID) on delete restrict on update restrict;

alter table tb_user_per add constraint FK_Reference_2 foreign key (PID)
      references tb_permission (ID) on delete restrict on update restrict;

