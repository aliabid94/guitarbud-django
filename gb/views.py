from django.shortcuts import render, redirect
from .models import Song
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from random import randint
import os.path

def index(request):
	allsongs = Song.objects.all().order_by('-points')
	context = {'songs':allsongs, 'preinput':""}
 	return render(request, 'gb/index.html', context)

@csrf_exempt
def getsongs(request, searchstring):
		context = getsearchcontext(request, searchstring)
		return render(request, 'gb/songlist.html', context)

@csrf_exempt
def getsearch(request, searchstring):
	context = getsearchcontext(request, searchstring)
	songs = context['songs']
	if len(songs) == 1:
		return redirect("/tab/"+songs[0].urlname)
	context['preinput'] = searchstring
 	return render(request, 'gb/index.html', context)

def getsearchcontext(request, searchstring):
	allsongs = Song.objects.all().order_by('-points')
	context = {'songs':[], 'comment':''}
	if (searchstring == "-"):
		context = {'songs':allsongs}
		return context
	else:
		searchwords = searchstring.split()
		retsongs = []
		for song in allsongs:
			matches = True
			for word in searchwords:
				if (not word.lower() in song.name.lower()) and (not word.lower() in song.artist.lower()):
					matches = False
					break
			if matches:
				retsongs.append(song)
		if len(retsongs) == 0:
			context['comment'] = "No matches found"
		context['songs'] = retsongs; 
		return context	

@csrf_exempt
def gettab(request, tab_url):
	song = Song.objects.get(urlname = tab_url)
	context = {'song':song}
	return render(request, 'gb/tab.html', context)

@csrf_exempt
def random(request):
	allsongs = Song.objects.all()
	songnum = randint(0, len(allsongs)-1)
	return redirect("/tab/"+allsongs[songnum].urlname)

@csrf_exempt
def about(request):
	return render(request, 'gb/about.html', {});
