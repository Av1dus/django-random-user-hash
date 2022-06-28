import requests
import django_random_user_hash.user as HashUser


user = HashUser.User(
    f="Charlie",
    l="Sheen",
    e="somesupercooltext@google.com",
    p1="glowing4ever",
    p2="glowing4ever",
    u="tHeRealSharLieSheen",
)
crypt_key = user.gen_sha1(level=2,salt=776)
print(crypt_key)
res = requests.get(url="http://0.0.0.0:8010/signup/")

token = res.cookies['csrftoken']
print(token)
data={
    "username": user.username,
    "password1": user.password1,
    "password2": user.password2,
    "first_name": user.first,
    "last_name": user.last,
    "email": user.email,
    "cryptographic_key": crypt_key,
    "next/": "shop/",
    "csrfmiddlewaretoken": token,
    
}
print(data)
headers = {
    'Referer': 'signup/',
}

get_ans_post = requests.post(url="http://0.0.0.0:8010/signup/",data=data)
print(get_ans_post.status_code)
