# سطح junior

۱- گیت چیست؟

گیت یک سیستم ورژن کنترل توزیع شده است. که به اختصار DVCS نامیده می شود. کامل آن Distributed Version Control System. گیت
میتونه تغییرات یک فایل رو track کنه و به شما اجازه میده تا به یک تغییری که قبلا داده بودید برگردید.


--- 

۲- تفاوت Git با SVN ؟چیست

کل تفاوت ها در این جمله خلاصه میشه که : گیت یک سیستم ورژن کنترل توزیع شده است در صورتی که SVN یک سیستم کنترل نسخه متمرکز
هستش

--- 

۳- منظور از **branch** چیست؟

برنچ یک نسخه جداشده از کد می باشد

---

۴- منظور از pull request چیست؟

جواب: pull request برای زمانی است که یک نفر repository را میگیرد. تغییرات مورد نظر خودش رو توی branch میدهد و قصد داره
تغییرات خودش رو به برنچ دیگری merge کند

---

۵- تفاوت git pull با git fetch چیست؟

به عبارت ساده، git pull یک git fetch هستش که با git merge همراه هست

زمانی که از **pull** استفاده میکنیم، git تلاش میکنه تا کارها رو به صورت اتوماتیک برای شما انجام بده. بنابراین git هر
کامیتی که pull شده باشه رو بر روی برنچی در حال کار با اون هستید merge میکنه. **pull** به صورت اتوماتیک کامیت ها رو merge
میکنه بدون اینکه اجازه بده اول اونها رو review کنیم. اگه حواسمون به برنچ نباشه باعث میشه conflict های زیادی پیش بیاد

زمانی که از **fetch** استفاده میکنیم، Git هر گونه commit را از branch هدف که در branch فعلی شما وجود ندارد جمع آوری می
کند و آنها را در local repository ذخیره می کند. اگر چه آنها رو با branch فعلی مرج نمیکند. زمان که بخواهیم ریپازیتوری رو
آپدیت نگهداریم به درد میخوره. برای ادغام کردن به branch اصلی از merge استفاده میکنیم

##### *

source*: [stackoverflow.com](https://stackoverflow.com/questions/292357/what-is-the-difference-between-git-pull-and-git-fetch)

--- 

۶- گیت فورک **Fork** چیست؟ تفاوت بین فورک کردن یک برنچ با clone کردن در چیست؟

**فورک** یک کپی از راه دور، سمت سرور از یک مخزن است که از نسخه اصلی متمایز هستش. در حقیقت fork یک مفهوم برای گیت نیست،
بیشتر ایده سیاسی/اجتماعی بوده

**کلون** یک **fork** نیست. یک clone یک کپی محلی از یک مخزن راه دور است.زمانی که ما clone می کنیم در اصل تمام فایل های
درون repository رو داریم کپی میکنیم. این کپی شامل تاریخچه و تمام برنچ ها می باشد

**برنچ** مکانیزمی است برای مدیریت تغییرات در یک مخزن به منظور ادغام آنها با بقیه کدها.

##### *

source*: [stackoverflow.com](https://stackoverflow.com/questions/3329943/git-branch-fork-fetch-merge-rebase-and-clone-what-are-the-differences/)

---

# سطح Mid

۱- مزایای Forking Workflow را توضیح دهید

گردش کار Forking اساساً با سایر Workflow های محبوب Git متفاوت است. به جای استفاده از یک مخزن سمت سرور به عنوان پایگاه
کد "مرکزی"، به هر توسعه دهنده ای مخزن سمت سرور خود را می دهد. Forking Workflow اغلب در پروژه های منبع باز عمومی دیده می
شود.مهم ترین مزیت fork workflow اینه هر کسی میتونه برای خودش پروژه رو بگیره هر کاری نیاز هست انجام بده و در نهایت توسعه
دهنده ها به repository خودشون این کد ها رو push میکنند و بعدش به repository اصلی درخواست می دهند که باعث میشه history
خیلی تمیز تری داشته باشیم

---

۲- چه زمانی از git stash استفاده کنیم؟

دستور git stash تغییراتی که uncommitted هستند رو میگیره (هم staged هم unstaged)، برای استفاده بعدا ذخیرشون میکنه، و بعدا
با استفاده working copy اونها رو revert میکنه.
(به حالت قبلی برمیگردونه)مثلا:

:

```terminal
$ git status
On branch master
Changes to be committed:
new file: style.css
Changes not staged for commit:
modified: index.html
$ git stash
Saved working directory and index state WIP on master: 5002d47 our new homepage
HEAD is now at 5002d47 our new homepage
$ git status
On branch master
nothing to commit, working tree clean
```

یکی دیگه از زمان هایی که میتونیم از stash استفاده کنیم موقعی هست که یادمون میفته فراموش کردیم یه تغییراتی رو توی commit
قبلی انجام بدیم و الان داریم روی قسمت جدید کار میکنیم.

```terminal
# Assume the latest commit was already done
# start working on the next patch, and discovered I was missing something

# stash away the current mess I made
$ git stash save

# some changes in the working dir

# and now add them to the last commit:
$ git add -u
$ git commit --ammend

# back to work!
$ git stash pop
```

---
