from PyPDF2 import PdfWriter

merger = PdfWriter
pdf = []
n=int(input("Enter how many pdf do you want to merge? \n"))

for i in range(0,n):
    name = input(f"Enter the name of the pdf{i+1} : ")