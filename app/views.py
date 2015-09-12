from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpRequest
from django.template import RequestContext
from django.contrib import messages
from django.db.models import Q
from django.views.generic.edit import FormView
from datetime import datetime
import itertools
import operator
from collections import OrderedDict

from app import models as bmodels
from app import forms as bforms
from app import helpers

from .models import Game
from .models import Team
from .models import Player
from .models import Season

from tabination.views import TabView



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )



def teams(request):
    teams = Team.objects.all().order_by('team_name')
    return render(request, 'app/teams.html', {'teams': teams})



def team_detail(request,pk):
    team_detail = get_object_or_404(Team, pk=1),
    games = Game.objects.filter(Q(hometeam=1) | Q(awayteam=1))
    players = Player.objects.filter(player_team=1)
    seasons = Season.objects.filter(team=1)
    model = Team
    model = Game
    model = Player
    model = Season
    return render(request, 'app/team_detail.html', {'team_detail': team_detail, 'games': games, 'players': players, 'seasons': seasons})

def game_detail(request,pk):
    game = get_object_or_404(Game, pk=pk),
    team_detail = get_object_or_404(Team, pk=1),
    home = Team.objects.filter(hometeam=pk)
    away = Team.objects.filter(awayteam=pk)
    model = Team
    model = Game
    model = Player
    model = Season

    games = Game.objects.filter(Q(hometeam=1) | Q(awayteam=1))
    players = Player.objects.filter(player_team=1)
    seasons = Season.objects.filter(team=1)
    
    return render(request, 'app/game_detail.html', {'team_detail': team_detail,'game': game, 'teams': teams, 'games': games, 'players': players, 'seasons': seasons, 'away': away, 'home': home})

def player_detail(request,pk):
    player_detail = get_object_or_404(Player, pk=pk),
    team_detail = get_object_or_404(Team, pk=1),
    games = Game.objects.filter(Q(hometeam=1) | Q(awayteam=1))
    players = Player.objects.filter(player_team=1)
    seasons = Season.objects.filter(team=1)
   
    return render(request, 'app/player_detail.html', {'player_detail': player_detail, 'team_detail': team_detail, 'games': games, 'players': players, 'seasons': seasons})

def season_detail(request,pk):
    season_detail = get_object_or_404(Season, pk=pk),
    team_detail = get_object_or_404(Team, pk=1),
    game = get_object_or_404(Game, pk=pk)
    games = Game.objects.filter(Q(hometeam=1) | Q(awayteam=1))
    players = Player.objects.filter(player_team=1)
    seasons = Season.objects.filter(team=1)
    home = Team.objects.filter(hometeam=pk)
    away = Team.objects.filter(awayteam=pk)
   
    return render(request, 'app/season_detail.html', {'season_detail': season_detail, 'team_detail': team_detail, 'games': games, 'away': away, 'home': home, 'game': game, 'players': players, 'seasons': seasons})







