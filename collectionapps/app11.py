employee={
    'id':1,
    'name':'Ajay',
    'sallary':45000,
    'hobbies':['swimming','dancing'],
    'identitymarks':('A mole on right eye','A mole on left leg'),
    'phonenumbers':{9461846584,9854628756},
    'maritalstatus':True,
    'account':{
        'accno':101,
        'bankname':'SBI',
        'ifsc':'SBIN000123'
    },
    'address':{
        'hno':'1/2/543-54',
        'city':'mumbai',
        'pincode':410210,
        'location':{
            'let':12.65,
            'lan':65.87
        }
    }
}
print(employee['name'],employee.get('name'))
print(employee['hobbies'])
print(employee['hobbies'][0])
print(employee['identitymarks'])
print(employee['phonenumbers'])
print(employee['account'])
print(employee['account']['ifsc'])
print(employee['address'])
print(employee['address']['location'])
print(employee['address']['location']['let'])
employees=[{
    'id':2,
    'name':'arun',
    'sallary':45000,
    'hobbies':['swimming','dancing'],
    'identitymarks':('A mole on right eye','A mole on left leg'),
    'phonenumbers':{9461846584,9854628756},
    'maritalstatus':True,
    'account':{
        'accno':101,
        'bankname':'SBI',
        'ifsc':'SBIN000123'
    },
    'address':{
        'hno':'1/2/543-54',
        'city':'mumbai',
        'pincode':410210,
        'location':{
            'let':12.65,
            'lan':65.87
        }
    }
},
{
    'id':2,
    'name':'rohan',
    'sallary':45000,
    'hobbies':['swimming','dancing'],
    'identitymarks':('A mole on right eye','A mole on left leg'),
    'phonenumbers':{9461846584,9854628756},
    'maritalstatus':True,
    'account':{
        'accno':101,
        'bankname':'SBI',
        'ifsc':'SBIN000123'
    },
    'address':{
        'hno':'1/2/543-54',
        'city':'mumbai',
        'pincode':410210,
        'location':{
            'let':12.65,
            'lan':65.87
        }
    }
}
]
print(employee)
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print(employees)