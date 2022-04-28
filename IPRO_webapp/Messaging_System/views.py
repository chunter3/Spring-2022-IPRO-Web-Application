from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from Messaging_System.models import Chat, Message
from users.forms import chatForm, messageForm
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.

def newChat(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "GET":
        form = chatForm()    
        context = {      
            'form': form    
        } 
        return render(request, 'Messaging_System/NewChat.html', context)
    if request.method == "POST":
        form = chatForm(request.POST)    
        username = request.POST.get('username')    
        try:      
            receiver = User.objects.get(username = username)      
            if Chat.objects.filter(user1 = request.user, user2 = receiver).exists():
                chat = Chat.objects.filter(user1 = request.user, user2 = receiver)[0]
                chatpk = chat.pk
                return redirect('chat', pk = chatpk)
            elif Chat.objects.filter(user1 = receiver, user2 = request.user).exists():        
                chat = Chat.objects.filter(user1 = receiver, user2 = request.user)[0]
                chatpk = chat.pk
                return redirect('chat', pk = chatpk)
            else:        
                newchat = Chat(          
                    user1 = request.user,          
                    user2 = receiver        
                )        
                newchat.save()
                chatpk = newchat.pk
                return redirect('chat', pk = chatpk)    
        except:      
            return redirect('newchat')    
        

def showChats(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "GET":
        chats = Chat.objects.filter(Q(user1 = request.user) | Q(user2 = request.user)) 
        context = {    
            'chats': chats  
        }  
        return render(request, 'Messaging_System/Messages.html', context)
           
def newMessage(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        chat = Chat.objects.get(pk = pk)    
        if chat.user2 == request.user:      
            messageReceiver = chat.user1    
        else:      
            messageReceiver = chat.user2      
        newMessage = Message(        
            chat = chat,        
            sender = request.user,                                                     
            receiver = messageReceiver,        
            body = request.POST.get('message'),                
        )       
        newMessage.save()      
        return redirect('chat', pk = pk)
    

def showMessages(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "GET":
        form = messageForm()
        chat = Chat.objects.get(pk = pk)
        message_list = Message.objects.filter(chat__pk__contains = pk)
        context = {      
            'chat': chat,      
            'form': form,      
            'message_list': message_list    
        }    
        return render(request, 'Messaging_System/chat.html', context)