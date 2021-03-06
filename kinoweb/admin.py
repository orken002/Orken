from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import  Category, Actor, Genre, Movie, MovieShots, RatingStar, Rating, Reviews

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "id")
    list_display_links = ("name",)

class ReviewInline(admin.TabularInline):
    model = Reviews
   

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "draft")
    list_filter = ("category", "year")
    search_fields = ("title", "category__name")
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    #fields = (("actors", "directors", "genres"), )
    fieldsets = (
        (None, {
            "fields": (("title", "tagline"), )
        }),
        (None, {
            "fields": (("description", "poster"), )
        }),
        (None, {
            "fields": (("year", "world_premiere", "country"), )
        }),
        ("Actors", {
            "classes": ("collapse",),
            "fields": (("actors", "directors", "genres"), )
        }),
        (None, {
            "fields": (("budget", "fees_in_usa", "fees_in_world"), )
        }),
          (None, {
            "fields": (("url", "draft"), )
        }),
    )

@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "movie", "id")
    readonly_fields = ("name", "email")

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src= {obj.image.url} width="50", height="60"')

    get_image.short_description = "Изображение"

@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ("title", "movie")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src= {obj.image.url} width="50", height="60"')

    get_image.short_description = "Изображение"


#admin.site.register(Category, CategoryAdmin)
#admin.site.register(Actor)
admin.site.register(Genre)
#admin.site.register(Movie)
#admin.site.register(MovieShots)
admin.site.register(RatingStar)
admin.site.register(Rating)
#admin.site.register(Reviews)
