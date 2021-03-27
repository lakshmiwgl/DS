import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
def extract_text_by_page(pdf_path):
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                     caching=True,
                                     check_extractable=True):
            resource_manager = PDFResourceManager()
            fake_file_handle = io.StringIO()
            laparams=LAParams()
            laparams.char_margin = float(50)
            converter = TextConverter(resource_manager, fake_file_handle, laparams=laparams)
            interpreter = PDFPageInterpreter(resource_manager, converter)
#             converter = TextConverter(resource_manager, fake_file_handle)
#             page_interpreter = PDFPageInterpreter(resource_manager, converter)
            interpreter.process_page(page)
            text = fake_file_handle.getvalue()
            yield text
           # close open handles
            converter.close()
            fake_file_handle.close()
def extract_text(pdf_path):
    for page in extract_text_by_page(pdf_path):
        page = page.replace("\n\n\x0c21\n\n","")
        print(page)
        page_content.append(page)
    return page_content
if __name__ == '__main__':
    
        try:
                page_content = []

                Text = extract_text(r'C:\Users\DataScience02\Downloads\sample_pdf_github.pdf')
        except:
            
                bio.append(np.nan)


# In[65]:
