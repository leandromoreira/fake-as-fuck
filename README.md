# Reinventing the wheel while fighting bot dection

Last week a friend of mine planted (without noticing) a doubt in my brain that got me hooked to study and learn! Essentially when you're automating a web tsak (like going to site www.example.com, log in, enter a query, submit it, and click on the first results) 

I never learn, I always start by reinventing the wheel then I got bored and search for what I'm building and 💡 someone did that 1000x better than me 🤡!

```mermaid
graph TD;
    step1([Stumble upon a problem X])-->step2[Think about X];
    step2-->step2;
    
    subgraph fun_loop
    step2-->step3(Magnify many possible sub problems to X)
    step3-->step2;
    step3-->step4[[Write some code to tackle a sub problem of X]]
    step4-->step5(Get excited)
    step5-->step3;
    end
    
    step5-->step6[[Realize someone probably won this batle already :clown:]]
    
    subgraph wisdom_moment
    step6-- Search on -->step7[(Internet)]
    step7-- There's a 1000x better solution available :clown: -->step6
    end
    
```

# Install

pip3.10 install undetected-chromedriver Faker

# Download the driver within the same version of your running browser

http://chromedriver.storage.googleapis.com/index.html

# Avoid site detection https://stackoverflow.com/questions/33225947/can-a-website-detect-when-you-are-using-selenium-with-chromedriver

https://github.com/ultrafunkamsterdam/undetected-chromedriver

https://bot.sannysoft.com/
https://bot.incolumitas.com/

https://github.com/soumilshah1995/Preventing-Selenium-from-being-detected/blob/main/master.py
https://newbedev.com/selenium-webdriver-modifying-navigator-webdriver-flag-to-prevent-selenium-detection
vim %s/cdc_/lhe_/g

# Run

for i in `seq 1 5`; do sleep $((6+RANDOM % (12-6))) && python3.10 usage.py ; done

# Proxies

curl https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt
