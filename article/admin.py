from django.contrib import admin
from .models import Article,Category,Sosial,About

# Register your models here.
@admin.register(Category)
class CategoryAdim(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["name","created_date"]
    list_display_links = ["name"]
    search_fields = ["name"]
    list_filter = ["created_date"]

    class Meta:
        model = Article

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Sosial)
class SosialAdmin(admin.ModelAdmin):
    list_display = ["name"]
