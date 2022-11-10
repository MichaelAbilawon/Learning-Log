from django.contrib import admin
from learning_logzs.models import Entry

from learning_logzs.models import Topic

# Register your models here.

admin.site.register(Topic)
admin.site.register(Entry)