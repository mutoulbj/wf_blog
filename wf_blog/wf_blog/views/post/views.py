# -*- coding: utf-8 -*-
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPForbidden

from wf_blog.resources import Root
from wf_blog.helper import login_required
from wf_blog.model import Post


class PostView(Root):
    @view_config(renderer='/posts/detail.html', route_name='post_detail')
    def post_detail(self):
        post = Post.get_post(self.request.mongodb, str(self.request.matchdict['id']))
        return {'post': post}

    @view_config(renderer='/posts/new_post.html', route_name='new_post', permission='admin', decorator=login_required)
    def new_post(self):
        if self.request.method == 'POST':
        	title = self.request.POST['title']
        	content = self.request.POST['content']
        	category = self.request.POST['category']
        	if not category:
        		category = u"未分类"
        	if title and content:
        		Post.add_post(self.request.mongodb, title, content, category)
        		return HTTPFound('/admin/all_posts')  # TODO: 跳转到详细页
        	else:
        		return {'error': 'error'}
        return {}

    @view_config(renderer='/posts/edit.html', route_name='post_edit', permission='admin', decorator=login_required)
    def post_edit(self):
        tid = self.request.matchdict['id']
        if self.request.method == 'POST':
            title = self.request.POST['title']
            content = self.request.POST['content']
            category = self.request.POST['category']
            if not category:
                category = u"未分类"
            if title and content:
                Post.update_post(self.request.mongodb, str(tid), title, content, category)
                return HTTPFound('/admin/all_posts')  # TODO: 跳转到详细页
        post = Post.get_post(self.request.mongodb, str(tid))
        return {'post': post}
