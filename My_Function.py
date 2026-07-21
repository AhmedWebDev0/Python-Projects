tiple =("css" ,"html" ,"Js")

progress ={
    "Css" : "90%",
    "html" : "80%",
    "Js" : "90%"
}

def type (name ,*skills ,**skillwithprogers) :

    print(f"Hello {name}\nYour skills is :")
    
    for skill in skills :
        
        print(f"- {skill}")
    
    for skill_key ,skill_value in skillwithprogers.items() :
    
        print(f"{skill_key} => {skill_value}")
    

type(input("Please your name :\n"),*tiple ,**progress )