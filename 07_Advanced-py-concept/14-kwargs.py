def the_kwargs(**kwargs):
    for item in kwargs.keys():
        print(f"The marks {item} obtained is : {kwargs[item]}")
        
the_kwargs(albey = 50, hebatle=60, killer=70, soloong=80)