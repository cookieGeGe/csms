# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

from APP.functions import db


class TbArea(db.Model):
    __tablename__ = 'tb_area'

    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50))
    FatherID = db.Column(db.Integer)
    HasChild = db.Column(db.Integer)


class TbAttendance(db.Model):
    __tablename__ = 'tb_attendance'

    ID = db.Column(db.Integer, primary_key=True)
    LaborID = db.Column(db.Integer)
    AttenTime = db.Column(db.DateTime)
    Remark = db.Column(db.String(50))


class TbBadrecord(db.Model):
    __tablename__ = 'tb_badrecord'

    ID = db.Column(db.Integer, primary_key=True)
    Type = db.Column(db.Integer)
    Description = db.Column(db.String(255))
    RecordTime = db.Column(db.DateTime)


class TbClas(db.Model):
    __tablename__ = 'tb_class'

    ID = db.Column(db.Integer, primary_key=True)
    CompanyID = db.Column(db.ForeignKey('tb_company.ID'), index=True)
    ClassName = db.Column(db.String(50))
    Description = db.Column(db.String(255))

    tb_company = db.relationship('TbCompany', primaryjoin='TbClas.CompanyID == TbCompany.ID', backref='tb_class')


class TbCompany(db.Model):
    __tablename__ = 'tb_company'

    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    Legal = db.Column(db.String(255))
    Address = db.Column(db.String(255))
    Phone = db.Column(db.String(255))
    License = db.Column(db.String(255))
    OtherPic = db.Column(db.String(255))
    BadRecord = db.Column(db.String(255))
    Type = db.Column(db.Integer)


class TbCompanyBadrecord(db.Model):
    __tablename__ = 'tb_company_badrecord'

    ID = db.Column(db.Integer, primary_key=True)
    CompanyID = db.Column(db.ForeignKey('tb_company.ID'), index=True)
    BadrecordID = db.Column(db.ForeignKey('tb_badrecord.ID'), index=True)

    tb_badrecord = db.relationship('TbBadrecord', primaryjoin='TbCompanyBadrecord.BadrecordID == TbBadrecord.ID', backref='tb_company_badrecords')
    tb_company = db.relationship('TbCompany', primaryjoin='TbCompanyBadrecord.CompanyID == TbCompany.ID', backref='tb_company_badrecords')


class TbGuarantee(db.Model):
    __tablename__ = 'tb_guarantee'

    ID = db.Column(db.Integer, primary_key=True)
    ProjectID = db.Column(db.ForeignKey('tb_project.ID'), index=True)
    Number = db.Column(db.String(255))
    CompanyID = db.Column(db.ForeignKey('tb_company.ID'), index=True)
    SignTime = db.Column(db.DateTime)
    Validity = db.Column(db.Integer)
    Amount = db.Column(db.String(255))
    Status = db.Column(db.Integer)
    Others = db.Column(db.String(255))
    Category = db.Column(db.Integer)

    tb_company = db.relationship('TbCompany', primaryjoin='TbGuarantee.CompanyID == TbCompany.ID', backref='tb_guarantees')
    tb_project = db.relationship('TbProject', primaryjoin='TbGuarantee.ProjectID == TbProject.ID', backref='tb_guarantees')


class TbLaborBadrecord(db.Model):
    __tablename__ = 'tb_labor_badrecord'

    ID = db.Column(db.Integer, primary_key=True)
    LaborID = db.Column(db.ForeignKey('tb_laborinfo.ID'), index=True)
    BadRecordID = db.Column(db.ForeignKey('tb_badrecord.ID'), index=True)

    tb_badrecord = db.relationship('TbBadrecord', primaryjoin='TbLaborBadrecord.BadRecordID == TbBadrecord.ID', backref='tb_labor_badrecords')
    tb_laborinfo = db.relationship('TbLaborinfo', primaryjoin='TbLaborBadrecord.LaborID == TbLaborinfo.ID', backref='tb_labor_badrecords')


class TbLaborinfo(db.Model):
    __tablename__ = 'tb_laborinfo'

    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50))
    Age = db.Column(db.Integer)
    Sex = db.Column(db.Integer)
    Birthday = db.Column(db.DateTime)
    Address = db.Column(db.String(255))
    Nationality = db.Column(db.String(25))
    IDCard = db.Column(db.String(25))
    Phone = db.Column(db.String(20))
    CompanyID = db.Column(db.ForeignKey('tb_company.ID'), index=True)
    JobNum = db.Column(db.String(25))
    ClassID = db.Column(db.ForeignKey('tb_class.ID'), index=True)
    WorkType = db.Column(db.Integer)
    Identity = db.Column(db.Integer)
    DepartureDate = db.Column(db.DateTime)
    EntryDate = db.Column(db.DateTime)
    Hardhatnum = db.Column(db.String(50))
    IDPhoto = db.Column(db.String(255))
    ConPhoto = db.Column(db.String(255))
    CloseupPhoto = db.Column(db.String(255))
    Education = db.Column(db.String(50))
    CreateTime = db.Column(db.DateTime)

    tb_clas = db.relationship('TbClas', primaryjoin='TbLaborinfo.ClassID == TbClas.ID', backref='tb_laborinfos')
    tb_company = db.relationship('TbCompany', primaryjoin='TbLaborinfo.CompanyID == TbCompany.ID', backref='tb_laborinfos')


class TbPermission(db.Model):
    __tablename__ = 'tb_permission'

    ID = db.Column(db.Integer, primary_key=True)
    PerName = db.Column(db.String(255))
    Permission = db.Column(db.String(255))
    Description = db.Column(db.String(255))
    FatherID = db.Column(db.Integer)
    URLName = db.Column(db.String(50))
    HasChild = db.Column(db.Integer)


class TbProClas(db.Model):
    __tablename__ = 'tb_pro_class'

    ID = db.Column(db.Integer, primary_key=True)
    ProjectID = db.Column(db.ForeignKey('tb_project.ID'), index=True)
    ClassID = db.Column(db.ForeignKey('tb_class.ID'), index=True)

    tb_clas = db.relationship('TbClas', primaryjoin='TbProClas.ClassID == TbClas.ID', backref='tb_pro_class')
    tb_project = db.relationship('TbProject', primaryjoin='TbProClas.ProjectID == TbProject.ID', backref='tb_pro_class')


class TbProgres(db.Model):
    __tablename__ = 'tb_progress'

    ID = db.Column(db.Integer, primary_key=True)
    ProjectID = db.Column(db.ForeignKey('tb_project.ID'), index=True)
    UploadTime = db.Column(db.DateTime)
    Pictures = db.Column(db.String(255))
    Content = db.Column(db.String(512))
    Status = db.Column(db.Integer)

    tb_project = db.relationship('TbProject', primaryjoin='TbProgres.ProjectID == TbProject.ID', backref='tb_progress')


class TbProject(db.Model):
    __tablename__ = 'tb_project'

    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    Type = db.Column(db.Integer)
    Duration = db.Column(db.Integer)
    Participants = db.Column(db.Integer)
    Price = db.Column(db.String(255))
    GAmount = db.Column(db.String(255))
    StartTime = db.Column(db.DateTime)
    Address = db.Column(db.String(255))
    OwnerManager = db.Column(db.Integer)
    ConsManager = db.Column(db.Integer)
    Supervisor = db.Column(db.Integer)
    LaborManager = db.Column(db.Integer)
    LaborCompany = db.Column(db.Integer)
    Pay = db.Column(db.Integer)
    TotalPrice = db.Column(db.String(255))
    TotalPayment = db.Column(db.String(255))
    RealHair = db.Column(db.String(255))
    Status = db.Column(db.Integer)
    WagePercent = db.Column(db.String(50))
    CompanyID = db.Column(db.ForeignKey('tb_company.ID'), index=True)
    AreaID = db.Column(db.ForeignKey('tb_area.ID'), index=True)

    tb_area = db.relationship('TbArea', primaryjoin='TbProject.AreaID == TbArea.ID', backref='tb_projects')
    tb_company = db.relationship('TbCompany', primaryjoin='TbProject.CompanyID == TbCompany.ID', backref='tb_projects')


class TbUser(db.Model):
    __tablename__ = 'tb_user'

    ID = db.Column(db.Integer, primary_key=True)
    LoginName = db.Column(db.String(255))
    UserName = db.Column(db.String(255))
    Password = db.Column(db.String(255))
    Email = db.Column(db.String(50))
    Phone = db.Column(db.String(20))
    Desccription = db.Column(db.String(255))
    AdminType = db.Column(db.Integer)
    CompanyID = db.Column(db.ForeignKey('tb_company.ID'), index=True)

    tb_company = db.relationship('TbCompany', primaryjoin='TbUser.CompanyID == TbCompany.ID', backref='tb_users')


class TbUserArea(db.Model):
    __tablename__ = 'tb_user_area'

    ID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.ForeignKey('tb_user.ID'), index=True)
    AreaID = db.Column(db.ForeignKey('tb_area.ID'), index=True)

    tb_area = db.relationship('TbArea', primaryjoin='TbUserArea.AreaID == TbArea.ID', backref='tb_user_areas')
    tb_user = db.relationship('TbUser', primaryjoin='TbUserArea.UserID == TbUser.ID', backref='tb_user_areas')


class TbUserPer(db.Model):
    __tablename__ = 'tb_user_per'

    ID = db.Column(db.Integer, primary_key=True)
    UID = db.Column(db.ForeignKey('tb_user.ID'), index=True)
    PID = db.Column(db.ForeignKey('tb_permission.ID'), index=True)

    tb_permission = db.relationship('TbPermission', primaryjoin='TbUserPer.PID == TbPermission.ID', backref='tb_user_pers')
    tb_user = db.relationship('TbUser', primaryjoin='TbUserPer.UID == TbUser.ID', backref='tb_user_pers')


class TbWage(db.Model):
    __tablename__ = 'tb_wage'

    ID = db.Column(db.Integer, primary_key=True)
    ProjectID = db.Column(db.Integer)
    January = db.Column(db.Integer)
    February = db.Column(db.Integer)
    March = db.Column(db.Integer)
    April = db.Column(db.Integer)
    May = db.Column(db.Integer)
    June = db.Column(db.Integer)
    July = db.Column(db.Integer)
    August = db.Column(db.Integer)
    September = db.Column(db.Integer)
    October = db.Column(db.Integer)
    November = db.Column(db.Integer)
    December = db.Column(db.Integer)
