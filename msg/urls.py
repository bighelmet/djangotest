# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 14:18:25 2018

@author: ying
"""

from django.contrib import admin
from django.urls import path
import msg.views as bv


urlpatterns = [
    path('edit/<article_id>/<title>/<content>',bv.edit_action,name='edit_action'),
    path('request/<article_id>',bv.get_article),
    path('delete/<article_id>',bv.delete_article),
]