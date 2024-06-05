from django.urls import path

from .views import (
    private_chat, 
    group_chat, 
    GroupChatListView, 
    GroupChatDetailView, 
    get_messages,
    chats,
)



urlpatterns = [
    path("chats/", chats, name="chats"),
    path('private_chat/<int:user_id>/', private_chat, name='private-chat'),
    path('group_chat/<int:pk>/', group_chat, name='group-chat'),
    path('group_list/', GroupChatListView.as_view(), name='group-list'),
    path('group_detail/<int:pk>/', GroupChatDetailView.as_view(), name='group-detail'),
    path('get_messages/<int:chat_id>/', get_messages, name='get-messages'),
]