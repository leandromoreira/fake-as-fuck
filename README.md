# Reinventing the wheel while fighting bot dection

Last week a friend planted a seed of doubt in my mind! How do we write an automated browser task without getting noticed by a bot detector?

> By no means I'm a anti bot specialist, I'm just describing and reflecting my journey during this endeavour.

It's been Essentially when you're automating a web tsak (like going to site www.example.com, log in, enter a query, submit it, and click on the first results) 

I never learn, I'm always reinventing the wheel and then I got bored, search for what I was building to find out 💡 someone did a 1000x better solution than mine 🤡!

```mermaid
graph TD;
    step1([Finding a problem X])-->step2[Thinking about X];
    step2-->step2;
    
    subgraph fun_loop
    step2-->step3(Magnifying possible subproblems to X)
    step3-->step2;
    step3-->step4[[Writing code to tackle a subproblem of X]]
    step4-->step5(Getting excited)
    step5-->step3;
    end
    
    step5-. Eventually .->step6[[Realize someone probably won this batle already]]
    
    subgraph wisdom_moment
    step6-- Searching on -->step7[(Internet)]
    step7-- Finding out a 1000x better solution available -->step6
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
