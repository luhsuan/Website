# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.db import models


class news(models.Model):
    id = models.IntegerField(u'id',max_length=20,primary_key=True)
    title = models.CharField(u'title',max_length=50)
    species = models.CharField(u'species',max_length=20)
    content = models.TextField(u'content')
    user = models.CharField(u'userDateField',max_length=20)
    create_time = models.DateTimeField(u'create_time')
    vanish_time = models.DateTimeField(u'vanish_time')

    def __unicode__(self):
        return self.id
    class Meta(object):
        db_table="news"

class contact_us(models.Model):
    name = models.CharField(u'name',max_length=20)
    email = models.CharField(u'email',max_length=30)
    phone = models.CharField(u'phone',max_length=20)
    subject = models.CharField(u'subject',max_length=20)
    message = models.CharField(u'message',max_length=20)
    time = models.DateTimeField(u'time',max_length=20)
   
    def __unicode__(self):
        return self.id
    class Meta(object):
        db_table="contact_us"

# class Choice(models.Model):
#     question = models.ForeignKey(Question)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
