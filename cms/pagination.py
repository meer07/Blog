__author__ = 'naoya-kaige'
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class pagination:
    list = None
    def __init__(self,contents_list):
        self.list = contents_list

    def make_pagination(self,page):
        paginator = Paginator(self.list,3)

        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)

        return contacts