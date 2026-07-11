import pypdf

class DocumentProcessingService:
    @staticmethod
    def extract_text_chunks_from_pdf(file_obj, max_chars: int = 1000, overlap: int = 200) -> list[dict]:
        pdf_reader = pypdf.PdfReader(file_obj)
        processed_chunks = []
        global_chunk_idx = 0
        
        for page_idx, page in enumerate(pdf_reader.pages):
            page_num = page_idx + 1
            text = page.extract_text() or ""
            
            # Simple clean sliding character window splitting technique
            start = 0
            while start < len(text):
                end = start + max_chars
                chunk_content = text[start:end].strip()
                if chunk_content:
                    processed_chunks.append({
                        "chunk_index": global_chunk_idx,
                        "page_number": page_num,
                        "content": chunk_content
                    })
                    global_chunk_idx += 1
                start += (max_chars - overlap)
                
        return processed_chunks