#convert the pdfs to images
#steps to install poppler on windows follow the link "https://stackoverflow.com/questions/18381713/how-to-install-poppler-on-windows"
#pdf to images
from pdf2image import convert_from_path
poppler_path=r'C:\Users\DataScience02\Desktop\CPI\poppler-0.68.0\bin'
images = convert_from_path(r'C:\Users\DataScience02\Downloads\sample_pdf_github.pdf',poppler_path=poppler_path)

for i in range(len(images)):
   
      # Save pages as images in the pdf
    images[i].save('page'+ str(i) +'.jpg', 'JPEG')
