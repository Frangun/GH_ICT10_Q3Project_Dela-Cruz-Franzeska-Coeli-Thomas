# LOOPS FOR PROJECT
from pyscript import document, display

def display_p(e):
    document.getElementById('output').InnerHTML = ' '

    players = ['1. Abayon', '2. Antes', '3. Apostol', '4. Banaag', '5. Barrientos', '6. Casal', '7. Coeli', '8. David', '9. De Mata', '10. Dela Cruz F.', '11. Dela Cruz J.', '12. Dellejero', '13. Fukuda', '14. Gozum', '15. Ibay', '16. Lim', '17. Lozano', '18. Mamauag', '19. Navarro', '20. Precones', '21. Ramos', '22. Sidhu', '23. Tiu', '24. Villamayor', '25. Zaragoza']


    for player in players:
        display(f'#{player}', target='output')

# LOGIN ----------------------------------

def validate_form(e):
    document.getElementById("output").innerHTML = ' '  
    name = document.getElementById("user").value
    pass_ = document.getElementById("pass").value

    i = name
    p = pass_

    uca = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # uppercase
    num = '0123456789' # numbers

    if len(i) >= 7:  # 7 characters long
        nval = True
    else:
        nval = False

    p2 = False
    p3 = False
    plen = False
    
    if len(p) >= 10:  # 10 characters long
        plen = True
        for char in p:
            if char in uca:   # password --> one uppercase letter
                p2 = True
            if char in num:   # password --> one number
                p3 = True

    if p2 == False and plen == True:
        display(f' **Password must contain at least one UPPERCASE letter! ', target='output')
    if p3 == False and plen == True:
        display(f' Password must contain at least ONE NUMBER  !', target='output')
    if plen == False:
        display(f' Password must be at least 10 CHARACTERS long! ', target='output')
        
    pval = p2 and  p3  and  plen    # combination


# PASSWORD
    if pval == True:
        display(f' VALID Password! ', target='output')
    else:
        display(f'INVALID Password, please try again! ', target='output')
    
# USERNAME
    if nval == True:
        display(f'VALID Username! ', target='output')
    else:
        display(f' INVALID Username, please try again! ', target='output')

    if pval == True and nval == True:    #if both are correct 
        display(f' Account Created! ', target='output')

# TEAM CHECKER ---------------------------

def teams(e):
    document.getElementById("output1").innerHTML = ""
    document.getElementById("output").innerHTML = ""
    registration = document.querySelector('input[name="registration"]:checked').value
    clearance = document.querySelector('input[name="clearance"]:checked').value
    grade = document.getElementById("grade").value
    section = document.getElementById("section").value

    if registration is None or clearance is None:
        display('Please select both registration and medical status.', target='output')
        return

    regis = registration.value
    medi = clearance.value
    grade = document.getElementById("grade").value
    section = document.getElementById("section").value

    eligible = "You are not eligible for registration."
    if grade in ["7", "8", "9", "10"]:
        if regis == "yes" and medi == "yes":
            eligible = "Yes"
        elif regis == "no" and medi == "yes":
            display('register online first', target='output')
            return
        elif regis == "yes" and medi == "no":
            display('clearance is required', target='output')
            return
    eligibility = eligible

    if eligibility == "Yes" and section in ["ruby"]:
        team="Red Team"
    elif eligibility == "Yes" and section in ["sapphire"]:
        team="Blue Team"
    elif eligibility == "Yes" and section in ["emerald"]:
        team="Green Team"
    elif eligibility == "Yes" and section in ["topaz"]:
        team="Yellow Team"
    elif eligibility == "You are not eligible for registration.":
        team="none"

    # TEAMS & IMG

    if team == "Red Team":
        display(f'You are part of the Red Bulldogs!', target='output')
        document.getElementById("output1").innerHTML = "<img src='r.jpeg' alt='Red Team' height='40%' width='40%'>"
    elif team == "Blue Team":
        display(f'You are part of the Blue bears!', target='output')
        document.getElementById("output1").innerHTML = "<img src='b.jpg' alt='Blue Team' height='40%' width='40%'>"
    elif team == "Green Team":
        display(f'You are part of the green hornets!', target='output')
        document.getElementById("output1").innerHTML = "<img src='g.jpeg' alt='Green Team' height='40%' width='40%'>"  
    elif team == "Yellow Team":
        display(f'You are part of the Yellow Tigers!', target='output')
        document.getElementById("output1").innerHTML = "<img src='y.jpeg' alt='Yellow Team' height='40%' width='40%'>"
    elif team == "none":
        display(f'Sorry, but you are not registered.', target='output')














