from fedora.client import FasProxyClient


class FasClient(FasProxyClient):

    def __init__(self, *args, **kwargs):
        # initialization; if debug mode is desired, add set debug to True in the below call
        super(FasClient, self).__init__(*args, **kwargs)

    def auth_prompt(self):
        while True:
            print "Please input your own FAS credentials:"
            username = raw_input('Username:')
            password = raw_input('Password:')
            auth_status = self.verify_password(username=username, password=password)
            print ""
            if auth_status:
                print "You have logged in successfully!"
                break
            else:
                print "Username, password, or both were incorrect"
        return {
            'username': username,
            'password': password,
            'session_id': self.login(username=username, password=password)[0]
        }

    def id_query(self, auth_params):
        try:
            print "Please input an FAS ID:"
            person_id = int(raw_input("ID:"))
            print ""
            return self.person_by_id(person_id=person_id, auth_params=auth_params)
        except ValueError:
            return False

    def auth_logout(self, auth_params):
        self.logout(session_id=auth_params['session_id'])
        print "You have been logged out."


try:
    login_check = False
    fas = FasClient()
    auth_params = fas.auth_prompt()
    login_check = True
    person_info = fas.id_query(auth_params=auth_params)
    if person_info:
        print "Query successful!"
        print "Email:"
        print person_info[1]['email']
    else:
        pass
except:
    print "Error encountered"
finally:
    if login_check:
        fas.auth_logout(auth_params=auth_params)
    else:
        pass

#selfInfoTotal = f.get_user_info(auth_params=auth_params)
#selfInfo = selfInfoTotal[1]
#print selfInfo['id']



#if f1.verify_password(username='ethanparab', password='EthuLaddoo$01'):
#    print "password is valid"
#else:
#    print "password is invalid"