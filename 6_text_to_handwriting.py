import pywhatkit as pw

txt="""this is the paragraph text created by me with the help of w3scube and also i am learning how to do project in python 
as well as in django for better purpose of practice in future to work in an company it will needed that we know something about the python syntax"""

pw.text_to_handwriting(txt,'demo.png',[255,0,0])
print(" END ")