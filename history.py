from catalog import models as cmod



class LastFiveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self,request):
        prods = request.session.get('lastFive', [])
        request.last_five = []
        for items in prods:
            request.last_five.append(cmod.Product.objects.get(id=items))

        response = self.get_response(request)

        request.session['lastFive'] = []

        for item in request.last_five:
            request.session['lastFive'].append(item.id)

        return response
