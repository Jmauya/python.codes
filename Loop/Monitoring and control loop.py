accuracy = 95 
# for i in range(20):
#     accuracy += 1 
#     print(accuracy)
#     if accuracy == 100:
#         break 

changed_or_not = True

while True: 
    if changed_or_not == False and accuracy == 100:
        break 
    
    if prev > accuracy:  # Error: prev is not defined!
        changed_or_not = False
