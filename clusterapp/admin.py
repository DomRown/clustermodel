from django.contrib import admin
from .models import Movies, Genres

class MoviesAdmin(admin.ModelAdmin):

	list_display = ["id","title", "rating", "rating_count", "plot"]
	list_display_links= ["title"]
	#list_filter=["id"]
	search_fields=["id"]
	class Meta:
		model= Movies


class GenresAdmin(admin.ModelAdmin):
	list_display = ["id", "genre", "movie_ref"]
	search_fields=["genre"]

	class Meta:
		model=Genres

admin.site.register(Movies, MoviesAdmin)
admin.site.register(Genres, GenresAdmin)