from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.utils.timezone import now
from .models import Chat, Message, GroupChat
from .forms import MessageForm
from user.models import CustomUser, Doctor



@login_required
def chats(request):
    """View for the user's chat list."""
    private_chats = Chat.objects.filter(user=request.user, group=None).order_by('-last_read_time')
    group_chats = GroupChat.objects.filter(members=request.user).order_by('-updated_at')

    # Get the last message for each chat
    for chat in private_chats:
        chat.last_message = chat.message_set.latest('created_at') if chat.message_set.exists() else None

    for group in group_chats:
        group.last_message = group.message_set.latest('created_at') if group.message_set.exists() else None

    context = {
        'private_chats': private_chats,
        'group_chats': group_chats,
    }
    return render(request, 'chat/chats.html', context)

@login_required
def private_chat(request, user_id):
    """View for a private chat between two users."""
    other_user = get_object_or_404(CustomUser, pk=user_id)

    # Create a chat if it doesn't exist
    chat, created = Chat.objects.get_or_create(user=request.user, group=None)
    if created:
        chat.members.add(other_user)

    # Get the messages for this chat
    messages = chat.message_set.all().order_by('created_at')

    # Handle posting new messages
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat = chat
            message.sender = request.user
            message.save()
            return JsonResponse({'message': message.text, 'sender': message.sender.username, 'created_at': message.created_at.strftime("%H:%M:%S")}, status=200)
        else:
            return JsonResponse({'error': form.errors}, status=400)

    # Mark messages as read
    chat.last_read_time = now()
    chat.save()

    return render(request, 'chat/private_chat.html', {
        'other_user': other_user,
        'chat': chat,
        'messages': messages,
        'form': MessageForm(),
    })


@login_required
def group_chat(request, pk):
    """View for a group chat."""
    group = get_object_or_404(GroupChat, pk=pk)

    # Check if user is a member of the group
    if request.user not in group.members.all():
        return redirect('chat:group-list')

    # Get the messages for this group
    messages = group.message_set.all().order_by('created_at')

    # Handle posting new messages
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat = Chat.objects.get_or_create(user=request.user, group=group)[0]
            message.sender = request.user
            message.save()
            return JsonResponse({'message': message.text, 'sender': message.sender.username, 'created_at': message.created_at.strftime("%H:%M:%S")}, status=200)
        else:
            return JsonResponse({'error': form.errors}, status=400)

    # Mark messages as read
    chat = Chat.objects.get_or_create(user=request.user, group=group)[0]
    chat.last_read_time = now()
    chat.save()

    return render(request, 'chat/group_chat.html', {
        'group': group,
        'messages': messages,
        'form': MessageForm(),
    })


class GroupChatListView(LoginRequiredMixin, ListView):
    """View to list all group chats."""
    model = GroupChat

    def get_queryset(self):
        # Filter groups based on user's role
        if self.request.user.is_doctor:
            return GroupChat.objects.filter(type='doctors').order_by('-updated_at')
        elif self.request.user.is_manager:
            return GroupChat.objects.filter(type='admins').order_by('-updated_at')
        else:
            return GroupChat.objects.filter(type='all').order_by('-updated_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unread_count'] = {
            group.id: group.get_unread_count(self.request.user)
            for group in self.get_queryset()
        }
        return context


class GroupChatDetailView(LoginRequiredMixin, DetailView):
    """View to show details of a group chat."""
    model = GroupChat

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = self.object.message_set.all().order_by('created_at')
        return context


@csrf_exempt
def get_messages(request, chat_id):
    """Ajax view to get new messages."""
    chat = get_object_or_404(Chat, pk=chat_id)
    messages = chat.message_set.filter(created_at__gt=request.GET.get('last_read_time')).order_by('created_at')
    data = [
        {
            'sender': message.sender.username,
            'text': message.text,
            'created_at': message.created_at.strftime("%H:%M:%S")
        } for message in messages
    ]
    return JsonResponse({'messages': data})