from django.db import models

# Create your models here.

class Employee(models.Model):
    """员工详细信息表"""
    employee_id = models.IntegerField(verbose_name='员工编号', unique=True)
    name = models.CharField(verbose_name='员工姓名', max_length=50)
    sex_choices = (
        (1, '男'),
        (2, '女'),
    )
    sex = models.SmallIntegerField(choices=sex_choices, verbose_name='员工性别')
    id_card = models.IntegerField(verbose_name='身份证号码')
    native_place = models.CharField(verbose_name='籍贯', max_length=50)
    education_choices = (
        (1, '高中'),
        (2, '大专'),
        (3, '本科'),
        (4, '研究生'),
        (5, '硕士'),
        (6, '博士'),
    )
    graduate_school = models.SmallIntegerField(choices=education_choices, verbose_name='毕业院校')
    graduate_time = models.DateTimeField(verbose_name='毕业时间')
    major = models.CharField(verbose_name='专业', max_length=30)
    arrival_type_choices = (
        (1, '试用'),
        (2, '实习'),
        (3, '正式'),
    )
    arrival_type = models.SmallIntegerField(choices=arrival_type_choices, verbose_name='到岗类别')
    arrival_date = models.DateTimeField(verbose_name='到岗日期')
    date_start = models.DateTimeField(verbose_name='合同生效日期')
    date_end = models.DateTimeField(verbose_name='合同终止日期')
    #外键关联group表
    # project_team = models.ForeignKey(verbose_name='所属项目组')
    department = models.CharField(verbose_name='所属部门', max_length=50, default='金融科技服务部')
    work_addr_choices = (
        (1, '总部'),
        (2, '西山汇'),
    )
    work_addr = models.SmallIntegerField(choices=work_addr_choices, verbose_name='工作地点')
    jobs_choices = (
        (1, '运维'),
        (2, '开发'),
        (3, '实施'),
    )
    jobs = models.SmallIntegerField(choices=jobs_choices, verbose_name='工作岗位')
    self_assessment = models.TextField(verbose_name='自我评价', max_length=200)
    tel = models.IntegerField(verbose_name='本人联系电话')
    addr = models.CharField(verbose_name='居住地址', max_length=50)
    ele_email = models.EmailField(verbose_name='电子邮箱', unique=True)
    qq_no = models.IntegerField(verbose_name='qq号码')
    wechat_no = models.CharField(verbose_name='微信号码', max_length=50)
    emer_person = models.CharField(verbose_name='紧急联系人', max_length=20)
    emer_relation_choices = (
        (0, '父母'),
        (1, '配偶'),
        (2, '兄弟姐妹'),
        (3, '朋友'),
        (4, '同学'),
        (5, '其它'),
    )
    emer_relation = models.SmallIntegerField(choices=emer_relation_choices, verbose_name='紧急联系人关系')
    emer_phone = models.IntegerField(verbose_name='紧急联系人电话')
    entry_status_choices = (
        (0, '未审核'),
        (1, '未通过'),
        (2, '已通过'),
    )
    entry_status = models.SmallIntegerField(choices=entry_status_choices, verbose_name='员工入职状态')
    positive_status_choices = (
        (0, '已提交未审核'),
        (1, '已审核未复核'),
        (2, '已审核已延期'),
        (3, '已审核未通过'),
        (4, '已复核未通过'),
        (5, '已复核已通过'),
        (6, '已复核已延期'),
    )
    positive_status = models.SmallIntegerField(choices=positive_status_choices, verbose_name='员工转正状态')
    leave_staus_choices = (
        (0, '未审核'),
        (1, '未通过'),
        (2, '已通过'),
    )
    leave_staus = models.SmallIntegerField(choices=leave_staus_choices, verbose_name='离职审核状态')
    employee_status_choices = (
        (0, '实习'),
        (1, '试用'),
        (2, '正式员工'),
        (3, '离职'),
        (4, '项目经理'),
        (5, '项目主管'),
    )
    employee_status = models.SmallIntegerField(choices=employee_status_choices, verbose_name='员工状态')
    work_experience_choices = (
        (0, '无工作经历'),
        (1, '有工作经历'),
    )
    work_experience = models.SmallIntegerField(choices=work_addr_choices, verbose_name='工作经历')
    extend1 = models.TextField(verbose_name='扩展字段1', max_length=1000, null=True)
    extend2 = models.TextField(verbose_name='扩展字段2', max_length=1000, null=True)
    extend3 = models.TextField(verbose_name='扩展字段3', max_length=1000, null=True)




class WorkExceprience(models.Model):
    #工作经历表信息
    company_name = models.CharField(verbose_name='公司名称', max_length=20, null=True)
    position = models.CharField(verbose_name='担任职位', max_length=20, null=True)
    date_joined = models.DateTimeField(verbose_name='入职日期', null=True)
    date_leave = models.DateTimeField(verbose_name='离职日期', null=True)
    position_desc = models.TextField(verbose_name='职位描述', max_length=200, null=True)
    leave_reason = models.TextField(verbose_name='离职原因', max_length=200, null=True)
    extend1 = models.TextField(verbose_name='扩展字段1', max_length=1000, null=True)
    extend2 = models.TextField(verbose_name='扩展字段2', max_length=1000, null=True)
    extend3 = models.TextField(verbose_name='扩展字段3', max_length=1000, null=True)
    employee_id = models.ForeignKey(Employee, verbose_name='员工编号', on_delete=models.CASCADE)


class HomeRelation(models.Model):
    #员工家庭信息
    relation_name = models.CharField(verbose_name='家庭联系人姓名', max_length=20)
    relationship_choices = (
        (0, '父母'),
        (1, '配偶'),
        (2, '兄弟姐妹'),
        (3, '其它'),
    )
    relationship = models.CharField(choices=relationship_choices, verbose_name='家庭联系人关系', max_length=20)
    home_phone = models.IntegerField(verbose_name='家庭联系人电话')
    home_addr = models.CharField(verbose_name='家庭地址', max_length=50)
    extend1 = models.TextField(verbose_name='扩展字段1', max_length=1000, null=True)
    extend2 = models.TextField(verbose_name='扩展字段2', max_length=1000, null=True)
    extend3 = models.TextField(verbose_name='扩展字段3', max_length=1000, null=True)
    employee_id = models.ForeignKey(Employee, verbose_name='员工编号', on_delete=models.CASCADE)

