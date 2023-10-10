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


    

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include, url


from polls.views import *

urlpatterns = [
	url(r'^$', index),
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', about),
    url(r'^ai_clerk/$', ai_clerk),
    url(r'^content/$', content),
    url(r'^hornor/$', hornor),
    url(r'^index/$', index),
    url(r'^join-us/$', join_us),
    url(r'^news/$', news),
    url(r'^partner/$', partner),
    url(r'^product/$', product),
    url(r'^report/$', report),
    url(r'^responsobility/$', responsobility),
    url(r'^solution/$', solution),
    url(r'^team/$', team),
    url(r'^technology/$', technology),
    url(r'^getimg_name/$', getimg_name,name='getimg_name'),
    url(r'^news_content/$', news_content,name='news_content'),
    url(r'^report_content/$', report_content,name='report_content'),
    url(r'^content_db/$', content_db,name='content_db'),
    url(r'^sent_mail/$', sent_mail,name='sent_mail'),

]
urlpatterns += staticfiles_urlpatterns()
