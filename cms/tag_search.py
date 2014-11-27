__author__ = 'naoya-kaige'

from cms.models import Blog

class tag_search:
    @classmethod
    def tag_list(self):
        return Blog.objects.all().order_by('tag')

