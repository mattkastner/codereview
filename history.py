from catalog import models as cmod

class LastFiveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # idlist= []
        # try:
        #     idlist=request.session['lastfive'] #doesn't get only return one object?
        # #convert product ids into objects- how do I do that?
        # except:
        #     "Error"

        idlist=request.session.get('lastfive',[])

        request.last_five =[]
        for items in idlist:
            request.last_five.append(cmod.Product.objects.get(id=items))

        response = self.get_response(request)
        request.session['lastfive']=[]

        for item in request.last_five:
            request.session['lastfive'].append(item.id)
        #save back into the session
        # convert request.last_five into a list of ids
        # request.session['...']=list of ids

        return response
