from django.shortcuts import render
from bot import get_chat

# Create your views here.


async def bot_pars(request):
    return render(request, "chat.html", {"value": await get_chat()})
