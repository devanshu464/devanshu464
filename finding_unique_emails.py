#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 23:06:51 2022

@author: devanshu
"""

#Rule1 --> while sending email '.' will be ignored and it will remove . and 
# send the email.
#Rule2 --> after first + everything will be ignored from email.
def unique_emails(arr,select_email):
    #used to store the processed email with thier count values
    email_dict = {}
    
    for each in arr:
        email_entry = 0
        # splitting each email means separating local name and domain name
        email_list = each.split('@')
        
        email_part = email_list[0]
        # checking if local name has + or not
        if '+' in email_part:
            count = 0
            count = count + 1
            # rule 2 says split it from first + so count is 1
            if count == 1:
                email_local_name = email_part.split('+')
        # check if local name has . or not, replace .        
        if '.' in email_local_name[0]:
            email_local_name = email_local_name[0].replace('.','')
        # if . in not local name then store email directly in email_dictionary    
        else:
            if email_dict.get(email_local_name[0]):
                email_entry = email_entry + 1
                
                email_dict[email_local_name[0]] = email_entry
                
            else:
                email_dict[email_local_name[0]] = 1
                
        
        if email_dict.get(email_local_name[0]):
            email_entry = email_entry + 1
            
            email_dict[email_local_name[0]] = email_entry
            
        else:
            email_dict[email_local_name] = 1
    if select_email in email_dict:
        return email_dict[select_email]
            
            
            
            
    print(email_dict.values())
if __name__ == '__main__':
    arr = ['test.email+alex@leetcode.com','test.e.mail+bob.catchy@leetcode.com',
           'testemail+david@leetcode.com']
    select_email = 'test.email+alex@leetcode.com'
    select_email_local = select_email.split('@')[0].split('+')[0].replace('.','')
    print("select_email_local",select_email_local)
    
    
    print(unique_emails(arr,select_email_local))
            
            
            