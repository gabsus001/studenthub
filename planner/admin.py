from django.contrib import admin

from .models import Subject
from .models import Exam
from .models import Assignment
from .models import Note


admin.site.register(Subject)
admin.site.register(Exam)
admin.site.register(Assignment)
admin.site.register(Note)

#hasło: admin
#username: admin
#email: admin@gmail.com