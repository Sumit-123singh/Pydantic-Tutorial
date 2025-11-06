from pydantic import BaseModel, EmailStr, AnyUrl,Field
from typing import List, Dict, Optional,Annotated

class Patient(BaseModel):
    name: str=Field(max_length=50,title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Nitish', 'Amit'])

    email: EmailStr
    linkedin_url: AnyUrl
    age: int
    weight: float=Field(gt=0,lt=108)
    married:  Annotated[bool, Field(default=None, description='Is the patient married or not')]
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]=Field(max_length =10)

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

# FIXED: email and linkedin_url moved to top level
patient_info = {
    'name': 'nitish',
    'email': 'abc@gmail.com',
    'linkedin_url': 'http://linkedin.com/1322',
    'age': 30,
    'weight': 104,
    # 'married': True,  # optional
    'contact_details': {
        'phone': '23455'
    }
}

patient1 = Patient(**patient_info)
update_patient_data(patient1)
