from dev2il_devops_app.mountains import highest_mountain

def test_get_mountains():
    mountains = [
        {"name": "Kilimanjaro", "height": 5895},
        {"name": "Everest", "height": 8848},
        {"name": "Denali", "height": 6190},
        {"name": "K2", "height": 8611},
    ]
    
    assert highest_mountain(mountains) == mountains[1]