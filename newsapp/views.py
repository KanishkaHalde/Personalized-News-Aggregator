from django.shortcuts import render
import requests

def index(request):
    # Get selected interests from the GET request
    selected_interests = request.GET.getlist('interest')

    # Join selected interests for API
    if selected_interests:
        categories = ','.join(selected_interests)
    else:
        categories = 'general'  # Fallback category

    # Call the news API
    api_url = f'http://api.mediastack.com/v1/news?access_key=2dfcecb461670b1ef5835be7637b42c4&countries=in&categories={categories}'
    r = requests.get(api_url)
    res = r.json()

    # Parse API response
    data = res.get('data', [])
    title = []
    description = []
    image = []
    url = []

    for i in data:
        title.append(i.get('title', 'No Title'))
        description.append(i.get('description', 'No Description'))
        image.append(i.get('image', 'https://via.placeholder.com/150'))
        url.append(i.get('url', '#'))

    news = zip(title, description, image, url)

    return render(request, 'newsapp/index.html', {'news': news})



def interest(request):
    return render(request, 'newsapp/interest.html')


