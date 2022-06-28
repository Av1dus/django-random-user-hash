import django_random_user_hash.user as HashUser
import random
import tqdm

def get_possible_seeds(min=0,max=10000000):
    seeds = []
    wanted = [0,1,2,3,4,5]
    for i in tqdm.tqdm(range(min,max)):
        random.seed(a=i,version=2)
        listed = []
        for j in range(0,6):
            listed.append(random.randint(0,5))
        if wanted == listed:
            seeds.append(i)
    return seeds

print(get_possible_seeds())


user = HashUser.User(
    "1qay1qay",
    "2wsx2wsx",
    "3edc3edc",
    "4rfv4rfv",
    "5tgb5tgb",
    "6zhn6zhn",
)
print(user.as_attr_list())
print(user.gen_sha1(level=2,salt=45))
print(user.test())