from django.contrib import admin

from .models import BlogPost

# admin.site.register(BlogPost)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title",
                    "slug",
                    "published",
                    "author",
                    "date",
                    "word_count",
                    )

    list_editable = ("title", "published","slug", )
    list_display_links = ("date", )
    search_fields = ("title", )
    list_filter = ("published", )
    autocomplete_fields = ("author", )
    list_per_page = 100

    empty_value_display = "Inconnu"