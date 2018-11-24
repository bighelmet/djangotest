# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 19:06:35 2018

@author: ying
"""

from django.contrib import admin
from django.urls import path
import blog.views as bv


urlpatterns = [
    path('', bv.index),
    path('article/<article_id>', bv.article_page,name='article_page'),
    path('edit/<article_id>',bv.edit_page,name='edit_page'),
    path('edit/action/<article_id>/<title>/<content>',bv.edit_action,name='edit_action'),
    path('request/<article_id>',bv.get_article),
]
