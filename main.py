from extractors import (
    extract_text_from_csv , 
    extract_text_from_doc , 
    extract_text_from_docx , 
    extract_text_from_image , 
    extract_text_from_pdf , 
    extract_text_from_pptx , 
    extract_text_from_txt , 
    extract_text_from_audio
)

seg_wrapper = {
    'txt' : lambda path : extract_text_from_txt(path) ,
    'pdf' : lambda path : extract_text_from_pdf(path) , 
    'doc' : lambda path : extract_text_from_doc(path) ,
    'csv' : lambda path : extract_text_from_csv(path) ,
    'xls' : lambda path : extract_text_from_csv(path) ,  
    'png' : lambda path : extract_text_from_image(path) , 
    'jpg' : lambda path : extract_text_from_image(path) ,
    'docx' : lambda path : extract_text_from_docx(path) , 
    'pptx' : lambda path : extract_text_from_pptx(path) , 
    'xlsx' : lambda path : extract_text_from_csv(path) , 
    'jpeg' : lambda path : extract_text_from_image(path) , 
    'wav' : lambda path : extract_text_from_audio(path) , 
    'mp3' : lambda path : extract_text_from_audio(path)
}

def extractor(paths) : 

    text = ''

    for path in paths : text += seg_wrapper[path.split('.')[-1]]

    return text