valid_credentials = [
    ('qa.ajax.app.automation@gmail.com', 'qa_automation_password',
     'Add your first hub to start managing the security system'),
    ('Qa.Ajax.App.AutOmaTion@Gmail.Com', 'qa_automation_password',
     'Add your first hub to start managing the security system'),
    (' qa.ajax.app.automation@gmail.com ', 'qa_automation_password',
     'Add your first hub to start managing the security system'),

 ]

invalid_credentials = [
    ('qa.ajax.app.automation1@gmail.com', 'qa_automation_password', 'Wrong login or password'),
    ('', '', 'false'),
    ('qa.ajax.app.automation@gmail.com', '', 'false'),
    ('', 'qa_automation_password', 'false'),
    ('oleh@gmail.com', 'qa_automation_password', 'Wrong login or password'),
    ('qa.ajax.app.automation@gmail.com', 'oleh12345', 'Wrong login or password'),
    ('oleh@gmail.com', 'oleh12345', 'Wrong login or password'),
    ('qa_automation_password', 'qa.ajax.app.automation@gmail.com', 'Invalid email format'),
    ('<script>alert("Hello")</script>', 'qa_automation_password', 'Invalid email format'),
    ('SELECT * FROM user', 'qa_automation_password', 'Invalid email format'),
    ('qa.ajax.app.automation@gmail.com', ' qa_automation_password ',  'Wrong login or password'),
    ('qa.ajax.app.automation@gmail.com', 'Qa_Automation_Password', 'Wrong login or password'),
    ('qa.ajax.app.automation@gmail.com', 'Qa_automation_Password!@#$%^&*()_+={}[]":/|<>', 'Wrong login or password'),
    ('qa.ajax.app.automation@@gmail.com', 'qa_automation_password', 'Invalid email format'),
    ('qa.ajax.app.automation@gmail.com.com', 'qa_automation_password', 'Wrong login or password'),
    ('qa.ajax.app.automationgmail.com', 'qa_automation_password', 'Invalid email format'),
    ('qa.ajax.app.automation@gmail', 'qa_automation_password', 'Invalid email format'),
    ('qa.ajax.app.automation@[216.58.209.5]', 'qa_automation_password', 'Wrong login or password'),
]
