from django.views.generic import TemplateView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from rest_framework.viewsets import ModelViewSet
from .models import Player, Match
from .serializers import UserSerializer, MatchSerializer
import os


class GoogleLoginView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class CallbackView(TemplateView):
    template_name = 'callback.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['access_token'] = request.GET.get('access_token')
        context['token_type'] = request.GET.get('token_type')
        context['expires_in'] = request.GET.get('expires_in')
        context['FRONTEND_CLIENT'] = os.environ.get('FRONTEND_CLIENT', 'http://localhost:3000/')
        return self.render_to_response(context)


class UserViewSet(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


class MatchViewSet(ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

