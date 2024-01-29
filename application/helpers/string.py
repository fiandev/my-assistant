import re

def str_to_list (text: str, separator: str = ",") -> list:
    return list(map(lambda item: item.strip(), text.split(separator)))

def create_slug(text):
    # Remove special characters
    cleaned_text = re.sub(r'[^\w\s-]', '', text)
    
    # Replace spaces with hyphens
    slug = re.sub(r'\s+', '-', cleaned_text).strip('-')
    
    # Convert to lowercase
    slug = slug.lower()
    return slug