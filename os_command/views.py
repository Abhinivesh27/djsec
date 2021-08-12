from django.shortcuts import render
import subprocess, shlex

def search(request):
    if request.method == "POST":
        host_name = request.POST.get("host_name")
        try:
            sanitizer = shlex.quote(host_name)
            to_execute = "ping -c1 {}".format(sanitizer)
            output =  subprocess.check_output(to_execute, shell=True, encoding='UTF-8')
            return render(request, 'os_command_search.html', {'output':output,'host_name':host_name})
        except subprocess.CalledProcessError:
            return render(request, 'os_command_search.html', {'output':"Invalid Input",'host_name':host_name})

    else:
        return render(request,'os_command_search.html')
























#sanitizer = shlex.split(host_name)
#return render(request, 'app/dns_lookup.html', {'output':"Invalid Input", 'host_name':host_name})