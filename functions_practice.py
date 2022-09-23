def hello():
    print("Hail and well met!")

def pack(one,two,three):
    return [one,two,three]
    
def eat_lunch(food):
    if len(food) == 0:
        print("My lunchbox is empty.")
    else:
        for i in range(len(food)):
            if i == 0:
                print(f"First I eat eat {food[0]}.")
            else:
                print(f"Next I eat {food[i]}.")

hello()
print(pack("one","two","three"))
eat_lunch(["chicken nuggets", "apple", "brownie"])