# An online retailer sells two products: widgets and gizmos. Each widget weighs 75
# grams. Each gizmo weighs 112 grams. Write a program that reads the number of
# widgets and the number of gizmos in an order from the user. Then your program
# should compute and display the total weight of the order

widgets = input("Enter value of widgets: ")
gizmos = input("Enter value of gizmos: ")
weight_widgets = 75*int(widgets)
weight_gizmos = 112*int(gizmos)
total_weight = weight_widgets + weight_gizmos
print("Total weight = ",total_weight,"gram")