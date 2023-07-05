from frappe import redirect, session

def get_context(context):
    if session.user != 'Guest' and not session.data.get('redirected'):
        # Redirect to the desired page
        redirect('/landingpage')
        # Set a session flag to indicate that the user has been redirected
        session.data['redirected'] = True
