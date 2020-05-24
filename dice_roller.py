def main():
    import random
    dice_sum=0 
    dice_rolls=2
    for i in range(0,dice_rolls):
        roll=random.randint(1,6)
        dice_sum+=roll
        print(f'You rolled a {roll}')
    print(f'You rolled a total of {dice_sum}')
    if roll==1:
        print(f'You rolled{roll}! Critical Fail!')
    elif roll==6:
        print(f'You rolled a {roll}! Critical Success!')
    else:
        print(f'You rolled a {roll}')
if __name__== "__main__":
  main()
