from django.views.generic.simple import direct_to_template
from django.conf.urls.defaults import *
from bookmarks.views import *
from bookmarks import views
import os
site_media = os.path.join(os.path.dirname(__file__), 'site_media')

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('', 
    #(r'^admin/(.*)', admin.site.root),
    url(r'^admin/', include(admin.site.urls)),
    #browsing
    (r'^$', main_page),
    (r'^popular/$', popular_page),
    (r'^user/(\w+)/$', user_page),
    (r'^tag/([^\s]+)/$',tag_page),
    (r'^search/$', search_page),
    (r'^bookmark/(\d+)/$', bookmark_page),
    # session mgt
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),
    (r'^register/$',register_page),
    (r'^register/success/$', direct_to_template,{'template': 'registration/register_success.html'}),
    # friends
    (r'^friends/(\w+)/$', friends_page),
    (r'^friend/add/$', friend_add),
    (r'^friend/invite/$', friend_invite),
    (r'^friend/accept/(\w+)/$', friend_accept),
   #Account mgt 
    (r'^tag/$',tag_cloud_page),
    (r'^save/$', bookmark_save_page),
    (r'^vote/$', bookmark_vote_page),

    #comment
    (r'^comments/',include('django.contrib.comments.urls')),
   # site media 
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': site_media}),
    
    # created model form 
    (r'^contact/$',contact_page),
    (r'^contact/edit/(?P<p_id>\d+)$',edit_contact_page),
    (r'^contact/success/$', direct_to_template,{'template': 'registration/contact_success.html'}),
    (r'^contact/edit/success/$',direct_to_template,{'template':'registration/contact_success.html'}),
)

