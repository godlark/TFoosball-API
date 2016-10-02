from rest_framework import serializers
from .models import Player


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'exp',
            'att_ratio',
            'def_ratio',
            'win_streak',
            'lose_streak',
            'lowest_exp',
            'highest_exp'
        )
