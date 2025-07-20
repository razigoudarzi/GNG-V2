from selenium.webdriver.common.by import By
#login page
#نام کاربری
username_box_css_selector = "input[name='username']"
#رمز ورود
password_box_css_selector = "input[name = 'password']"
#دکمه ورود
login_button_css_slector = "dx-button[role = 'button']"
#لینک پرسنلی
personnel_link_css_selector ="li[aria-label = 'پرسنلی']"
#اطلاعات پایه مشاغل
jobs_info_css_selector="li[aria-label = 'اطلاعات پایه مشاغل']"
#افزودن
plus_button = "(//div[@aria-label= 'افزودن'])"
#شغل
job_css_selctor = "li[aria-label = 'شغل']"
#فرم شغل
#دکمه کد شغل
#job_code = (By.NAME,'number')
job_code = "input[name='number']"
#نام شغل
#job_name = (By.NAME,'name')
job_name ="input[name='name']"
#دراپ داون رسته شغلی
job_drop_down = "(//input[@role= 'combobox'])[3]"
#رسته شغلی
Job_type = "(//div[@role= 'checkbox'])[4]"


#دراپ داون شغل معادل بیمه
job_bime_drop_down = "(//div[@aria-label= 'انتخاب'])[4]"
job_bime = "(//div[@role= 'checkbox'])[16]"

#دراپ داون  نوع شغل بیمه

job_type1= "(//div[@aria-label='انتخاب'])[7]"
job_type1_option1="(//div[@role='option'])[1]"


#ثبت

submit = "//div[@aria-label= 'ثبت']"

# فیلد سرچ کد شغل در گرید
#job_code_search = (By.XPATH, "(//input[@aria-label='فیلتر کردن ستون'])[1]")

# لوکیتور فیلتر جستجوی کد شغل در گرید
job_code_filter = 'input[aria-label="فیلتر کردن ستون"]'

# لوکیتور آیکون سطل زباله (حذف رکورد)
delete_icon =  "tr.dx-row.dx-data-row td a[title='حذف']"

# لوکیتور دکمه "تأیید" در دیالوگ حذف
confirm_button = 'div.dx-button-success span.dx-button-text'
