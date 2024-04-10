from django.shortcuts import render
from .models import Subject, TrainingProgram,NetworkExpansion, Card,Game, Review

def index(request):
    subjects = Subject.objects.all()
    training_programs = TrainingProgram.objects.all()
    network_data = NetworkExpansion.objects.all()
    cards = Card.objects.all()
    reviews = Review.objects.all()
    games = Game.objects.all()


    return render(request, 'index.html', {'subjects': subjects, 'training_programs': training_programs, 'network_data': network_data, 'cards': cards, 'reviews': reviews, 'games': games})
