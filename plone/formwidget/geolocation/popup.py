# -*- coding: utf-8 -*-

from Products.CMFPlone.utils import safe_unicode
from Products.Five.browser import BrowserView


class PopupView(BrowserView):
    """
    This browser view is used to generate map popup content.
    It makes it easy to have your own view/template to customize the popup.
    """

    def __init__(self, context, request):
        title = getattr(context, "title", "") or ""
        description = getattr(context, "description", "") or ""
        self.context = context
        self.request = request
        self.title = safe_unicode(title)
        self.description = safe_unicode(description)
