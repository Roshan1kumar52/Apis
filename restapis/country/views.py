from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.urls import reverse

# Example of using reverse in a view
#url = reverse('countries_list')

# Create your views here.
def countries_list(request):
    urls = "https://restcountries.com/v3.1/all"
    response =requests.get(urls)
    if response.status_code == 200:
        countries_data = response.json()
    
        #cty = countries_data.objects.filter(alpha3Code__isnull=False).exclude(alpha3Code='')
        ctry =[
            
            {
            "name": county["name"]["common"], 
            "capital": county.get("capital", ["N/A"])[0],
            "alpha3Code": county["cca3"]
            
            }
            for county in countries_data
        ]
        total_count = len(ctry)
        print(total_count)
        return render(request, 'country.html', {'ctry': ctry})
        
        
    
    return JsonResponse({"error": "Unable to fetch data from REST Countries API"}, status=500)
def country_detail(request,country_code):
    url = f"https://restcountries.com/v3.1/alpha/{country_code}"
    response = requests.get(url)
    
    if response.status_code == 200:
        country_data = response.json()[0]  # There will be only one country for this code
        
        country = {
            "name": country_data["name"]["common"],
            "capital": country_data.get("capital", ["N/A"])[0],
            "region": country_data.get("region", "N/A"),
            "subregion": country_data.get("subregion", "N/A"),
            "population": country_data.get("population", "N/A"),
            "area": country_data.get("area", "N/A"),
            "languages": ', '.join(country_data["languages"].values()) if "languages" in country_data else "N/A",
            "flag": country_data["flags"]["png"]
        }

        return render(request, 'cntrydetail.html', {'country': country})

    return JsonResponse({"error": "Country not found"}, status=404)




