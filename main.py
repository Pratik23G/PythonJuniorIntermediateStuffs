print("hello we will add more stuffs later in next 15-20 mins")

userRepo ={
    "name": "Pratik23G",
    "project": "Junior Python role",
    "target_days": 14,
}

userRepo["email"] = "pratikgurung022@gmail.com"

print(userRepo.get("phone", "n/a"))

print(userRepo)

view = list(userRepo.keys()), list(userRepo.values())

print(view)