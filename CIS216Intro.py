def calc_bmi(ttlheight, height_ft, height_in):
  ttlheight = height_ft * 12 + (height_in)
  bmi = (weight / ttlheight ** 2) * 703
  return bmi

def bmi_category(bmi):
  if bmi < 18.5:
    return "Underweight"
  elif 18.5 <= bmi < 24.9:
    return "Normal Weight"
  elif 24.9 <= bmi < 29.9:
    return "Overweight"
  else:
    return "Obese"

weight = float(input("Enter weight"))
height_ft = float(input("Enter height in feet"))
height_in = float(input("Enter height in inches"))

bmi = calc_bmi(weight, height_ft, height_in)
category = bmi_category(bmi)

print("Your BMI is: {: .1f}".format(bmi))
print("BMI Category: {}".format(category))

print("\nBMI categorys:")
print("Underweight: Less than 18.5")
print("Normal weight: 18.5 - 24.9")
print("Overweight: 25 - 29.9")
print("Obese: 30 or more")




