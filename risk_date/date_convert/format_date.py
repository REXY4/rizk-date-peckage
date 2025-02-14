import re

def get_format_date_py(format_value):
    # Mapping format custom ke format strftime
    format_mapping = {
        "yyyy": "Y",
        "yy": "y",
        "mmmm": "B",
        "mmm": "b",
        "mm": "m",
        "dd": "d",
        "hh": "H",
        "h": "I",
        "MM": "M",
        "ss": "S",
        "a": "p"
    }
    
    # Split berdasarkan "-", ":", atau spasi " "
    format_parts = re.split(r'([-:/\s])', format_value)  # Menyertakan delimiter dalam hasil split
    
    # Konversi format yang dikenali
    converted_parts = [f"%{format_mapping.get(part, part)}" if part.strip() and part not in "-: " else part for part in format_parts]
    
    # Gabungkan kembali
    return "".join(converted_parts)