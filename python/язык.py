# определяет какой язык
from langdetect import detect
print(detect('سلام دوستان من این مدلی که وصل شدم الان چهار ماه شده بدون مسدودی. سرور گرفتم ماهیانه اجارشو میدم و یه هزنیه کانفیگ هم پرداخت کردم یکبار کل خانواده وصل هستیم مشکلیم نداشتیم مسدودم نشده.سرعتم کم هم میشه ولی مقطعیه. این آموزش های مجانی تو اینترنت هم در دسترس فیلتر کننده ها هم هست قبل که میگفتم هزینه دادم برام کانفیگ اختصاصی کردند همه مسخره میکردند میگفتند سرت کلاه گذاشتن اینا که رایگانش هست الان سرور همشون مسدود شده. من نمیدونم فاز فکریشون چیه یعنی فهمیدن این موضوع خیلی سخته که آموزشی که به شکل پابلیک و رایگان در دسترس شما قرار داره در دسترس فیلرکننده ها هم هست؟ خواستم فیدبکم را بعد از این مدت داده باشم'))
print(detect('I write in Russian'))