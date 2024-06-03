from django.shortcuts import render,redirect

def home(response):
    if response.method == "GET":
        if response.GET.get("local"):
            return redirect("/local/")
        if response.GET.get("national"):
            return redirect("/national/")
        if response.GET.get("international"):
            return redirect("/international/")
    return render(response,"home.html")

def lnews(response):
    local_news={
        "Money fraud in Jamnagar":"Police of AlO has found a case of money fraud in ALO. The famous businessman Ramesh Baltiwala Bartanwala has been allegedly accussed of hiding black money in his buckets and utensils.The police is toroughly invertigating the matter.",
        "Sewer: the royal swimming pool":"The sewers of ALO are always overflowing and the ducks and dogs are seen having swimming races in the water. The people have asked the Municipal Corporation to take adequate steps."
    }
    return render(response,"local.html",{"local":local_news})

def nnews(response):
    nation_news={
        "The Jewel of Jabeli":"Rahul de Silva, the recent Guiness world Record holder for making 100 perfectly circular jalebis in 1 min, has used all his money to ny jewels to decorate his certificate. People are questing if that was a 100 IQ move or a move worth the IQ of the room temperature. de Silva has replied that he prefers Celsius over Kelvin, not because he is not a scientise, but because he likes drawing degrees, and Fahrenheit is too long to write or pronounce."
    }
    return render(response,"nation.html",{"nation":nation_news})

def inews(response):
    inter_news={
        "Togo wins the gold":"Togo has made history by becoming the first gold medallist in the gadha-gadha racing fever tournament"
    }
    return render(response,"inter.html",{"inter":inter_news})