from django.shortcuts import render
import requests
from .models import News
from django.db import IntegrityError
from rest_framework import generics
from .serializers import NewsSerializer
from django.views.generic import TemplateView,ListView

class HomeView(ListView):

	template_name = "news/home.html"
	model = News
	context_object_name = 'news'
	queryset = News.objects.all().order_by('-published_date')[:20]
	

class ListNewsView(generics.ListAPIView):
	
    queryset = News.objects.all().order_by('-published_date')[:50]
    serializer_class = NewsSerializer	


class MigrateData(TemplateView):
	
	def get(self,request):
		url = 'https://newsapi.org/v2/everything?apiKey=&q=Halloween'
		raw_data = requests.get(url).json()
		articles = raw_data['articles']
		print(len(articles))
		for item in range(len(articles)):
			print('inserting..')
			try:
				News.objects.create(source_name=articles[item]['source']['name'],
										author = articles[item]['author'],
										title = articles[item]['title'],
										url = articles[item]['url'],
										description = articles[item]['description'],
										published_date=articles[item]['publishedAt'],
										content = articles[item]['content'])
				print('done..')

			except IntegrityError as ie:
				print('unique constraint error..')

			except Exception as ex:
				print('ran into generic Exception')
	  			

		return render(request,'news/insert.html')
