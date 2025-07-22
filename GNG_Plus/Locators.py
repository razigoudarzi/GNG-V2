
#Login Page
#فیلد نام کاربری
username_box_css_selsctor = "input[name = 'username']"
#فیلد رمز ورود
password_box_css_selector = "input[name = 'password']"
#دکمه ی ورود
login_box_css_selector = "dx-button[role='button']"

# .....................................................................................................................
#unsuccess_Tc
#دیالوگ باکس پیغام خطا
dialog_box_css_selector = "div.dx-dialog-message"
#.......................................................................................................................

#required_fields_Tc  - فرم انواع اعلام نیاز
#پنل اعلام نیاز
request_title_link = "li[aria-label='اعلام نیاز']"
#منوی تنظیمات
setting_link = "li[aria-label = 'تنظیمات']"

#منوی انواع اعلام نیاز
request_types = "li[aria-label='انواع اعلام نياز']"
#دکمه ی افزودن
plus_button ="//div[@title ='افزودن'][1]"
#فیلد عنوان اعلام نیاز
request_title = ".dx-texteditor-input[name = 'name']"
#فیلد عنوان طرف حساب 1
party_title = ".dx-texteditor-input[name='partyOneName']"
#دکمه ی ثبت
save_button = "div[aria-label='ثبت']"

#.......................................................................................................................
#Details,Detail_Tc,Edit_Tc   -فرم انواع اعلام نیاز

#سه نقطه ی کنار رکورد
overflow_button_xpath  = "//div[@role = 'button'  and @aria-label = 'overflow'][1]"
#گزینه ی نمایش جزئیات
detail_xpath = "//div[@role= 'option'][3]"
#عنوان طرف حساب 2
party2_Css_selector = "input[name= 'partyTwoName']"
#عنوان طرف حساب 3
party3_Css_Selector = "input[name= 'partyThreeName']"
#دکمه ی انصراف
ignore_button_xpath = "//div[@aria-label= 'انصراف'][1]"
#گزینه ی ویرایش
edit_button_xpath = "//div[@role = 'option'][1]"

#.......................................................................................................................

#Disabled_field
#پنل اعلام نیاز
request_xpath= "(//li[@aria-label= 'اعلام نياز'])[1]"
#منوی اقدامات
actions_xpath ="//li[@aria-label = 'اقدامات']"
#منوی اعلام نیاز
request_xpath2 = "(//li[@aria-label = 'اعلام نياز'])[2]"
#دکمه ی جستجو
search_button = "//dx-button[@aria-label= 'جستجو']"
#دراپ داون نوع اعلام نیاز
request_type_drop_down_xpath = "//dx-drop-down-box[@ng-reflect-label='نوع اعلام نیاز']"

check_box_xpath = "(//*[@class='dx-checkbox-container'])[2]"

#.......................................................................................................................
# -فرم  اعلام نیاز

#دکمه ی افزودن
plus_butyon_xpath = "(//div[@title= 'افزودن'])[1]"

#فیلد طبقه بندی کالا
product_categori_xpath = "(//input[@autocomplete='one-time-code' ])[4]"
#واحد
unit_xpath = "(//input[@autocomplete='one-time-code' ])[6]"
#جک باکس واحد
check_box1 = "(//div[@aria-label='انتخاب ردیف'  and @role = 'checkbox'])[12]"
check_box_xpath2="(//div[@aria-label='انتخاب ردیف'  and @role = 'checkbox'])[12]"
search_id_xpath = "(//input[@aria-label = 'فیلتر کردن ستون'])[11]"



#......................................................................................................................
#Import from excel
#این تست کیس تکمیل نشده است
select_request_xpath = "(//div[@aria-label='انتخاب ردیف'])[1]"
search_button_xpath = "//dx-button[@role = 'button' and @aria-label = 'جستجو']"
plus_button_xpath = "(//div[@title = 'افزودن'])[1]"
product_group_xpath ="//dx-drop-down-box[@ng-reflect-label = 'طبقه بندی کالا']"
select_request_xpath2 = "(//div[@aria-label='انتخاب ردیف'])[11]"
unit_xpath = "//dx-drop-down-box[@ng-reflect-label = 'واحد']"
select_request_xpath3= "(//div[@aria-label='انتخاب ردیف'])[12]"
save_button_xpath = "//div[@aria-label= 'ثبت']"


#.......................................................................................................................
#filter,filter_Tc - فرم اعلام نیاز
#بازنشانی فیلتر
refresh_field_xpath = "//dx-button[@aria-label = 'بازنشانی فیلتر']"
#دراب دان نوع اعلام نیاز
request_type_drop_down_xpath = "//dx-drop-down-box[@ng-reflect-label='نوع اعلام نیاز']"

#.......................................................................................................................
#Search ,search_Tc - فرم انواع اعلام نیاز
search_input_css_selector = "input[aria-label='جستجو در گرید']"
# فیلد عنوان اعلام نیاز در ردیف اول
target_field_xpath  = "(//*[@class = 'gng-datagrid-header-searchable'])[1]"


#.......................................................................................................................
#sort
# مربوط به سناریو سورت کردن ستون آی دی که تست کیس آن نوشته نشده است
column_id_xpath = "(//td[@aria-label = 'ستون شناسه'])[1]"



#.......................................................................................................................
#Logout
#آیکون امکانات کاربر
user_icone_xpath = "//div[@role = 'button' and @title = 'امکانات کاربر']"
#گزینه ی خروج
logout_icon_xpath  = "//span[text() ='خروج']"


#.......................................................................................................................
#checkBox_request
#چک باکس طرف حساب اول در فرم انواع اعلام نیاز
party_checkbox1_xpath = "(//dx-check-box[@role = 'checkbox'])[1]"
#چک باکس طرف حساب دوم در فرم اعلام نیاز
party_checkbox2_xpath = "(//dx-check-box[@role = 'checkbox'])[2]"

#دکمه ی افزودن
insert_button_xpath = "(//div[@aria-label= 'افزودن'])[1]"
#عنوان طرف حساب اول
party1_name_css_Selector ="input[name = 'partyOneName']"
#تاگل فعال کردن طرف حساب دوم
party2_switch_on_xpath = "(//div[@class='dx-switch-on'])[2]"
#عنوان طرف حساب دوم
party2_name_xpath = "//input[@name = 'partyTwoName']"
#جک باکس طرف حساب 1
check_box_party1_selected = "(//dx-check-box)[1]"
#چک باکس طرف حساب 2
check_box_party2_selected = '(//dx-check-box)[2]'
#جک باکس طرف حساب 3
check_box_party3_selected = '(//dx-check-box)[3]'


