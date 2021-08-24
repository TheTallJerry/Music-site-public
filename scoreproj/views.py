from django.shortcuts import render
from django.views import View
from .models import ScoreProject
# Create your views here.
class ScoreprojLookupView(View):
    model = ScoreProject

    def get(self, request, *args, **kwargs):
        return render(request, "scoreproj/scoreproj_lookup.html", {})

# not using a form as my clean method is completely different from what django has by default
def scoreproj_searched_view(request):
    default = {"brass", "saxophone", "woodwinds", "auxpercussion", "drumset", "piano"}
    if request.method == "POST":
        temp, n = request.POST.getlist("instrumentation-include"), len(request.POST.getlist("instrumentation-include"))
        res = []
        for sub in temp:
            if sub not in default:
                # executes only if client-side html is changed. Used to prevent hacking. 
                return render(request, "invalid_input.html", {"input": temp})
        sql_qeury_finale = ""
        has_include = False
        has_exclude = False

        # projects that do include at least one of the includes
        if n > 0:
            sql_query_include = "SELECT * FROM scoreproj_ScoreProject WHERE "
            for i in range(0, n - 1):
                sql_query_include += "{} = True OR ".format(temp[i])
            sql_query_include += "{} = True".format(temp[n - 1])
            has_include = True

        temp2, n2 = request.POST.getlist("instrumentation-exclude"), len(request.POST.getlist("instrumentation-exclude"))
        # projects that do not include any of the excludes
        if n2 > 0:
            sql_query_exclude = "SELECT * FROM scoreproj_ScoreProject WHERE "
            for i in range(0, n2 - 1):
                sql_query_exclude += "{} = False And ".format(temp2[i])
            sql_query_exclude += "{} = False".format(temp2[n2 - 1])
            has_exclude = True

        # construct the resulting query
        if not (has_exclude or has_exclude):
            res = ScoreProject.objects.all()
        elif has_exclude and has_include:
            sql_qeury_finale = sql_query_include + " INTERSECT " + sql_query_exclude + ";"
            res = ScoreProject.objects.raw(sql_qeury_finale)
        elif has_exclude: 
            sql_qeury_finale = sql_query_exclude + ";"
            res = ScoreProject.objects.raw(sql_qeury_finale)
        elif has_include:
            sql_qeury_finale = sql_query_include + ";"
            res = ScoreProject.objects.raw(sql_qeury_finale)
        context = {"object_list": res, "included": temp, "excluded": temp2} 
    else:
        context = {"object_list": ScoreProject.objects.all()}
    return render(request, "scoreproj/scoreproj_searched.html", context)