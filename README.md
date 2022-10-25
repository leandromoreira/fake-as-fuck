# Reinventing the wheel while learning about bot detection

Last week a friend planted a seed of doubt in my mind! How do we write an automated browser task without getting noticed by a bot detector?

Well, I started raising questions about the problem and its subproblems:
* How does a bot detector works?
  * Identifying repeated/predictable input values?
  * Looking at HTTP metadata like headers `User-Agent`?
  * Detecting bot behavior by traits such as typing speed, lack of mouse movement, and etc?
  * Noticing a lot of actions from a single actor? (same IP/user agent)
  * And so on...

Once I had thought about a bunch of subproblems, I started writing code to solve each one of them. 

To fight the predictability on the input values, I wrote a small function to randomly generate data based on some arbibrary rules (for instance name):
```python
import random

us_first_names  = ["Alice", "Bob"]
us_middle_names = ["L.", "N."]
us_last_names   = ["Smith", "Johnson"]

br_first_names  = ["Maria", "Ana"]
br_middle_names = ["Paula", "A."]
br_last_names   = ["Oliveira", "Santos"]

name_provider = {
 "us": {
    "first_names": us_first_names,
    "middle_names": us_middle_names,
    "last_names": us_last_names,
  },
   "br": {
    "first_names": br_first_names,
    "middle_names": br_middle_names,
    "last_names": br_last_names,
  }
}

def generate_name():
  lucky_factor = random.randint(1,100)
  name_country = "us" # 95% of time we'll use "us"
  if lucky_factor > 95: # 5% of time we'll use "br"
    name_country = "br"
    
  lucky_factor = random.randint(1,100)
  middle_name = "" # 80% of time we won't use a middle name
  if lucky_factor > 80:  # 20% of time we'll have a middle name
    middle_name = random.choice(name_provider[name_country]["middle_names"]) + " "
  
  first_name = random.choice(name_provider[name_country]["first_names"])
  last_name = random.choice(name_provider[name_country]["last_names"])
  full_name = f"{first_name} {middle_name}{last_name}"
  
  lucky_factor = random.randint(1,100)
  if lucky_factor > 95: # 5% of time we'll use lowercase
    full_name = full_name.lower()
    
  lucky_factor = random.randint(1,100)
  if lucky_factor > 98: # 2% of time we'll drop the last character
    full_name = full_name[:-1]
    
  return full_name
```

I run a quick test to see it working

```python
[generate_name() for _ in range(100)]
```

I could keep adding extra layers to it but I decided to move on.

```python
def failure(lucky, str):
    if lucky < 33:
        str = str[:-1] # drop last char
    elif lucky < 66:
        str = str[:len(str)//2] + str[len(str)//2] + str[len(str)//2:] # dup mid char
    else
        str = str + " " # add extra trailing space
    return str
``` 

> By no means I'm a anti bot specialist, I'm just describing and reflecting my journey during this endeavour.

It's been Essentially when you're automating a web tsak (like going to site www.example.com, log in, enter a query, submit it, and click on the first results) 

I never learn, I'm always reinventing the wheel and then I got bored, search for what I was building to find out 💡 someone did a 1000x better solution than mine 🤡!

# The vicious, maybe necessary, think->experiment->do->use loop
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
