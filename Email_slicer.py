try:
    u=input("Enter Email : ").strip()
    email=u.split('@')
    username=email[0]
    domain=email[1]
    print("Your USERNAME is",username,"and your DOMAIN is",domain)
except:
    print("Enter Valid Email")
