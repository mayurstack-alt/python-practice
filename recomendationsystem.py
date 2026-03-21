n=int(input("Enter the number of Users:"))
users={}
for i in range(n):
    user=str(input("Enter User:"))
    productId=set(str(input("Enter product ID:")).split())
    users[user]=productId
target_user=str(input("Enter the target User:"))

def jaccard_similarity(set1,set2):
    if(len(set1.union(set2))==0): return
    score=len(set1.intersection(set2))/len(set1.union(set2))
    return score

def find_most_similar_user(users,target_user):
    targeted_products=users[target_user]
    max_similarity=-1
    most_similar_user=None
    for user,products in users.items():
        if(user==target_user): continue
        similarity=jaccard_similarity(targeted_products,products)
        if(similarity>max_similarity):
          max_similarity=similarity
          most_similar_user=user
        print(f"Similarity with {user}:{similarity:.2f}")
    return most_similar_user,max_similarity

def recommend_products(users,target_user,similar_user):
    targeted_products=users[target_user]
    similar_products=users[similar_user]
    recommended_products= similar_products.difference(targeted_products)
    return recommended_products

most_similar_user,max_similarity=find_most_similar_user(users,target_user)
print("Most Similar User:",most_similar_user)

if (max_similarity==0):
   print("No similar user found.No recommendation")
else:
   recommended_products=recommend_products(users,target_user,most_similar_user)
   print("Recommended Products:",recommended_products)


    