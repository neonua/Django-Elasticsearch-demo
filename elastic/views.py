from django.views.generic import View
from django.http import JsonResponse
from elastic.search import search

# Create your views here.


class Index(View):
    template_name = 'index.html'
    search_result_dict = {'result': 'None'}

    def get(self, request, *args, **kwargs):
        # get search request
        search_request = request.GET.get('q', None)
        if search_request:
            search_result = search(search_request)
            self.search_result_dict = search_result.to_dict()

        return JsonResponse(self.search_result_dict)
