{"filter":false,"title":"urls.py","tooltip":"/django_todo_app/urls.py","undoManager":{"mark":6,"position":6,"stack":[[{"start":{"row":0,"column":0},"end":{"row":21,"column":0},"action":"remove","lines":["\"\"\"django_todo_app URL Configuration","","The `urlpatterns` list routes URLs to views. For more information please see:","    https://docs.djangoproject.com/en/1.11/topics/http/urls/","Examples:","Function views","    1. Add an import:  from my_app import views","    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')","Class-based views","    1. Add an import:  from other_app.views import Home","    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')","Including another URLconf","    1. Import the include() function: from django.conf.urls import url, include","    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))","\"\"\"","from django.conf.urls import url","from django.contrib import admin","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","]",""],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":21,"column":1},"action":"insert","lines":["\"\"\"django_todo URL Configuration","The `urlpatterns` list routes URLs to views. For more information please see:","    https://docs.djangoproject.com/en/1.11/topics/http/urls/","Examples:","Function views","    1. Add an import:  from my_app import views","    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')","Class-based views","    1. Add an import:  from other_app.views import Home","    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')","Including another URLconf","    1. Import the include() function: from django.conf.urls import url, include","    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))","\"\"\"","from django.conf.urls import url","from django.contrib import admin","from todo.views import say_hello","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'message$', say_hello)","]"],"id":3}],[{"start":{"row":15,"column":32},"end":{"row":16,"column":0},"action":"remove","lines":["",""],"id":4}],[{"start":{"row":15,"column":32},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":5}],[{"start":{"row":0,"column":0},"end":{"row":21,"column":1},"action":"remove","lines":["\"\"\"django_todo URL Configuration","The `urlpatterns` list routes URLs to views. For more information please see:","    https://docs.djangoproject.com/en/1.11/topics/http/urls/","Examples:","Function views","    1. Add an import:  from my_app import views","    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')","Class-based views","    1. Add an import:  from other_app.views import Home","    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')","Including another URLconf","    1. Import the include() function: from django.conf.urls import url, include","    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))","\"\"\"","from django.conf.urls import url","from django.contrib import admin","from todo.views import say_hello","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'message$', say_hello)","]"],"id":6},{"start":{"row":0,"column":0},"end":{"row":21,"column":1},"action":"insert","lines":["\"\"\"django_todo URL Configuration","The `urlpatterns` list routes URLs to views. For more information please see:","    https://docs.djangoproject.com/en/1.11/topics/http/urls/","Examples:","Function views","    1. Add an import:  from my_app import views","    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')","Class-based views","    1. Add an import:  from other_app.views import Home","    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')","Including another URLconf","    1. Import the include() function: from django.conf.urls import url, include","    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))","\"\"\"","from django.conf.urls import url","from django.contrib import admin","from todo.views import get_todo_list","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', get_todo_list)","]"]}],[{"start":{"row":0,"column":0},"end":{"row":21,"column":1},"action":"remove","lines":["\"\"\"django_todo URL Configuration","The `urlpatterns` list routes URLs to views. For more information please see:","    https://docs.djangoproject.com/en/1.11/topics/http/urls/","Examples:","Function views","    1. Add an import:  from my_app import views","    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')","Class-based views","    1. Add an import:  from other_app.views import Home","    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')","Including another URLconf","    1. Import the include() function: from django.conf.urls import url, include","    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))","\"\"\"","from django.conf.urls import url","from django.contrib import admin","from todo.views import get_todo_list","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', get_todo_list)","]"],"id":7},{"start":{"row":0,"column":0},"end":{"row":23,"column":1},"action":"insert","lines":["    ","\"\"\"django_todo URL Configuration","The `urlpatterns` list routes URLs to views. For more information please see:","    https://docs.djangoproject.com/en/1.11/topics/http/urls/","Examples:","Function views","    1. Add an import:  from my_app import views","    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')","Class-based views","    1. Add an import:  from other_app.views import Home","    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')","Including another URLconf","    1. Import the include() function: from django.conf.urls import url, include","    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))","\"\"\"","from django.conf.urls import url","from django.contrib import admin","from todo.views import get_todo_list, create_an_item","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', get_todo_list),","    url(r'^add$', create_an_item)","]"]}],[{"start":{"row":0,"column":4},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":8},{"start":{"row":0,"column":0},"end":{"row":0,"column":4},"action":"remove","lines":["    "]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":0,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1562160368369,"hash":"09c9e8ad386a865acab43314e54325c075286b20"}