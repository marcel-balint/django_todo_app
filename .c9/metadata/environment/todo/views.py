{"filter":false,"title":"views.py","tooltip":"/todo/views.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":35,"column":60},"action":"remove","lines":["from django.shortcuts import render, HttpResponse, redirect, get_object_or_404","from .models import Item","from .forms import ItemForm","","","# Create your views here.","def get_todo_list(request):","    results = Item.objects.all()","    return render(request, \"todo_list.html\", {","        'items': results","    })","","","def create_an_item(request):","    if request.method == \"POST\":","        form = ItemForm(request.POST, request.FILES)","        if form.is_valid():","            form.save()","            return redirect(get_todo_list)","    else:","        form = ItemForm()","","    return render(request, \"item_form.html\", {'form': form})","","","def edit_an_item(request, id):","    item = get_object_or_404(Item, pk=id)","","    if request.method == \"POST\":","        form = ItemForm(request.POST, instance=item)","        if form.is_valid():","            form.save()","            return redirect(get_todo_list)","    else:","        form = ItemForm(instance=item)","    return render(request, \"item_form.html\", {'form': form})"],"id":7},{"start":{"row":0,"column":0},"end":{"row":42,"column":34},"action":"insert","lines":["from django.shortcuts import render, HttpResponse, redirect, get_object_or_404","from .models import Item","from .forms import ItemForm","","","# Create your views here.","def get_todo_list(request):","    results = Item.objects.all()","    return render(request, \"todo_list.html\", {","        'items': results","    })","","","def create_an_item(request):","    if request.method == \"POST\":","        form = ItemForm(request.POST, request.FILES)","        if form.is_valid():","            form.save()","            return redirect(get_todo_list)","    else:","        form = ItemForm()","","    return render(request, \"item_form.html\", {'form': form})","","","def edit_an_item(request, id):","    item = get_object_or_404(Item, pk=id)","","    if request.method == \"POST\":","        form = ItemForm(request.POST, instance=item)","        if form.is_valid():","            form.save()","            return redirect(get_todo_list)","    else:","        form = ItemForm(instance=item)","    return render(request, \"item_form.html\", {'form': form})","","","def toggle_status(request, id):","    item = get_object_or_404(Item, pk=id)","    item.done = not item.done","    item.save()","    return redirect(get_todo_list)"]}]]},"ace":{"folds":[],"scrolltop":547,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":0,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":13,"state":"start","mode":"ace/mode/python"}},"timestamp":1562162271607,"hash":"6d226ad1b9c342a34953e24dffa65f8a5d5661fe"}