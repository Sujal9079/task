from django.contrib import admin
from .models import Subject,TrainingProgram,NetworkExpansion,Game, Card, Review
# Register your models here.
admin.site.register(Subject)
admin.site.register(TrainingProgram)
admin.site.register(NetworkExpansion)
admin.site.register(Card)
admin.site.register(Review)
admin.site.register(Game)
