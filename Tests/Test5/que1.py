D = [2000, 500, 200, 100, 50, 20, 10, 5]

amount = int(input("Enter the amount: "))

print("\nBreakdown of notes:")
total_notes = 0

for note in D:
    if amount >= note:
        count = amount // note 
        amount = amount % note  
        total_notes += count
        print(f"{note} x {count}")

print(f"\nMinimum total number of notes needed: {total_notes}")