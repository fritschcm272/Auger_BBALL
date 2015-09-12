from django.contrib import admin
from .models import Team,Player,Game,StatLine,PlayByPlay,Season

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Game)
admin.site.register(StatLine)
admin.site.register(PlayByPlay)
admin.site.register(Season)
