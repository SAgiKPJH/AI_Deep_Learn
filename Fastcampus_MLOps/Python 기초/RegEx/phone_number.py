import re

def mask_phone_numbers(match):
    return f"{match.group(1)}-****-{match.group(3)}"

def mask_ssm(match):
    return f"{match.group(1)}-{match.group(2)}******"

def remove_html_tags(input):
    pattern = re.compile(r'<.*?>')
    result = re.sub(pattern, '', input)
    return result

phone_number_pattern = re.compile(r'(01[016789])-(\d{3,4})-(\d{4})')
ssn_pattern = re.compile(r'(\d{6})-(\d)\d{6}')

personal_info = """
이름 : 홍길동
역대 주소 : 서울-대구-대전-부산
전화번호 : 010-1234-5678
주민번호 : 010101-1234567
Body : <p>This is <b>Python</b> and <i>Reqular Expression</i>.</p>
"""

match = phone_number_pattern.search(personal_info)
if match:
    print(f"핸드폰 번호 : {match.group()}")

masked_info = phone_number_pattern.sub(mask_phone_numbers, personal_info)
masked_info = ssn_pattern.sub(mask_ssm, masked_info)
masked_info = remove_html_tags(masked_info)

print(re.sub(r'(\w+)-(\w+)-(\w+)-(\w+)', r'\1-\3-\2-\4', masked_info))


def generate_birthday(matches):
    return f"{'19' if matches[4] in ('1', '2') else '20'}{matches[1]}. {matches[2]}. {matches[3]}"

ssn = "900101-4234567"
pattern = re.compile(r'(\d{2})(\d{2})(\d{2})-(\d)\d{6}')
print(pattern.sub(generate_birthday, ssn))