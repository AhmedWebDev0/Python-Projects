people ={ 
    "Ahmed" : {
       "Haml" : "90%",
       "Css" : "80%",
       "Js" : "90%"
    },

     "Moustafa" : {
       "Haml" : "70%",
       "Css" : "80%",
       "Js" : "90%"
    },
       
    "Joury" :{
       "Haml" : "80%",
       "Css" : "90%",
       "Js" : "70%"
    }
}


for name in people :

    print(f"Skills and Progress For {name} Is :")
    
    for skill in people[name] :

        print(f"- {skill} => {people[name][skill]}")
