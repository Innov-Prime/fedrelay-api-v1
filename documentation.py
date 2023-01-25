import requests

'''
##============ CREATION DE COMPTE D'UN USER ==========##

    url = http://api.fedrelay.com/user/create ## ON DOIT LUI ENVOYER UN JSON DATA VOIR LE POINT 

    FORME DU DATA JSON à ENVOYER

    user = {
        "username": "gogochristian009@gmail.com",## ICI LE USER NE RENSEIGNE PAS SON USERNAME DANS LE FORMULAIRE. C'EST NOUS QUI LUI EN CREONS UN SOIT AVEC SON MAIL OU SON PHONE=====##
        "email": "gogochristian009@gmail.com",
        "phone":"6589654521",
        "password": "Password@123"
    }

    EXEMPLE DE REQUEST:

    requests.post(http://api.fedrelay.com/user/create,json=user)

'''

'''
##============ CONNEXION D'UN USER à UN COMPTE ==========##

    url = http://api.fedrelay.com/user/login ## ON DOIT LUI ENVOYER UN JSON DATA VOIR LE POINT 

    FORME DU DATA JSON à ENVOYER

    user_login = {
        "username": "gogochristian009@gmail.com",
        "password": "Password@123"
    }

    EXEMPLE DE REQUEST:

    requests.post(http://api.fedrelay.com/user/login,json=user_login)

'''

'''
##============ DECONNEXION D'UN USER à UN COMPTE ==========##

    url = http://api.fedrelay.com/user/logout ## ON DOIT LUI ENVOYER UN TOKEN DANS LE HEADERS ## ça marche sur postman


    EXEMPLE DE REQUEST:

    requests.post(http://api.fedrelay.com/user/logout)

'''

'''
##============ REINITIALISATION DE MOT DE PASSE ==========##

    url = http://api.fedrelay.com/user/password_reset/ ## ON DOIT LUI ENVOYER UN JSON DATA 

    FORME DU DATA JSON à ENVOYER

    reset_password ={
        "email": "gogochristian009@gmail.com"##Ici l'utilisateur doit entrer l'email avec lequel il avait créer son  compte,
    }

    EXEMPLE DE REQUEST:

    requests.post(http://api.fedrelay.com/user/password_reset/,json=reset_password)


    RETURN: 
    ====== UN MAIL EST RENVOYE AU CLIENT POUR QU'IL CONFIRME LA REINITIALISATION DU MOT DE PASSE.   ========
                ENSUITE IL RENVOIE CE JSON LORSQUE LE MAIL EST BIEN ENVOYE
    {
        'status':'OK'   
    }

'''

'''
##============ CONFIRMATION DE LA REINITIALISATION DU MOT DE PASSE ==========##

    url = http://api.fedrelay.com/user/password_reset/confirm/ ## ON DOIT LUI ENVOYER UN JSON DATA 

    FORME DU DATA JSON à ENVOYER

    confirm_reset_password ={
        "token": "2348492e2042c945d028bcc116e64a124be",## Ici l'utilisateur doit entrer le Token qui lui a été envoyer par mail
        "password":"gogo@123" ## Ici l'utilisateur doit entrer son nouveau password qu'il veut utiliser désormais
    }

    EXEMPLE DE REQUEST:

    requests.post(http://api.fedrelay.com/user/password_reset/confirm/,json=confirm_reset_password)

'''

'''
##============ CREATION DU PROFIL D'UN USER ==========##

    url = http://api.fedrelay.com/dashbord/<str:user_token>/profil ## ON DOIT LUI ENVOYER UN JSON DATA 

    FORME DU DATA JSON à ENVOYER

    profil = {
        'user':1, ## Ici il nous utilisons l'ID du user## Cet ID se retouve dans le JSON data renvoyé au client lors de la creation de compte 
        "nom":"GOGO",
        "prenom":"Christian",
        "telephone":"6589654521",
        "email":'florent@gmail.com',
        "profession":'Ingénieur',
        "pays":'Bénin',
        "ville":'Cotonou',
        "quartier":"Finanfa"
    }

    EXEMPLE DE REQUEST:

    requests.post(http://api.fedrelay.com/dashbord/<str:user_token>/profil,json=profil)

'''


'''
##============ MODIFICATION D'UN AVATAR POUR UN USER ==========##

    url = http://api.fedrelay.com/dashbord/<int:user_id>/<str:user_token>/avatar ## ON DOIT LUI ENVOYER UN JSON DATA 

    FORME DU DATA JSON à ENVOYER

    avatar = {
        "avatar":"https://www.shutterstock.com/image-photo/portrait-positive-guy-specialist-sit-600w-1836307192.jpg" ## Renseigner ici l'URL de votre nouvelle image
    }
    EXEMPLE DE REQUEST:

    requests.patch(http://api.fedrelay.com/dashbord/<int:user_id>/<str:user_token>/avatar)

    NB: ICI LA METHODE PATCH EST REQUISE. CETTE REQUETE NE MARCHE PAS AVEC LA METHODE PUT
'''



'''
##============ ENREGISTREMENT D'UNE LIVRAISON==========##

    url = http://api.fedrelay.com/delivery/<str:user_token>/create ## ON DOIT LUI ENVOYER UN JSON DATA VOIR LE POINT 

    FORME DU DATA JSON à ENVOYER

    delivery = {
        "user":1, ##ICI IL FAUT RENSEIGNER L'ID DE L'UTILISATEUR QUI EST CONNECTE
        "client_id":1, ##ICI IL FAUT AUSSI RENSEIGNER L'ID DE L'UTILISATEUR QUI EST CONNECTE
        "nomEmetteur": "SEDEGNAN",
        "prenomEmetteur": "Victoire",
        "telephoneEmetteur": "61765590",
        "lieuColis": "Ahelawadjè",
        "detailLocalisation": "Non loin du carrefour les trois bandes",

        "villeReception": "Togo",
        "pointRelais": "Lomè",
        "notification": "Ce colis des trucs",

        "nomDestinataire": "PAPA",
        "prenomDestinataire": "Lomè",
        "telephoneDestinataire": "617955600",
        "emailDestinataire": "azizvorrez8@gmail.com",
        "typeColis": "Du gari à l'intérieur",
        "poids": "54 kg",
        "description": "Trois sacs de riz et de banane"
    }

    EXEMPLE DE REQUEST:

    requests.post(http://api.fedrelay.com/delivery/<str:user_token>/create,json=delivery)

'''

'''
##============ RECUPERATION DE TOUTE LES LIVRAISONS D'UN USER==========##

    url = http://api.fedrelay.com/delivery/<user_id>/<str:user_token>/deliveries ## ON DOIT LUI ENVOYER UN JSON DATA VOIR LE POINT 

    EXEMPLE DE REQUEST:

    requests.GET(http://api.fedrelay.com/delivery/deliverys/<user_id>/<str:user_token>/)
'''

'''
##============ SUIVI D'UNE LIVRAISON ==========##

    url = http://api.fedrelay.com/delivery/<int:user_id>/<str:user_token>/followup ## ON DOIT LUI ENVOYER UN JSON DATA VOIR LE POINT 

    FORME DU DATA JSON à ENVOYER

    follow_code = {
        'follow_code':"R17345W"
    }

    EXEMPLE DE REQUEST:

    requests.post(http://api.fedrelay.com/delivery/<int:user_id>/<str:user_token>/followup,json=follow_code)

    RETURN:

    EN CAS DE SUCCES::
    {
        'success': True,
        'command_status': 'En cours',##Ici C'est l'etat de la commande qui est renvoyé
    }

    EN CAS D'ECHEC::

    {
        'success': False, ## Ceci veut dire que la commande n'existe meme pas
    }

    EN CAS DE NON AUTHENTIFICATION:

    {
        "detail":"Veuillez vous authentifier"
    }

'''



'''
##============ ENVOIE DE MESSAGE DANS LE CHAT PAR UN CLIENT ==========##

    url = http://api.fedrelay.com/chat/<user_token>/client ## ON DOIT LUI ENVOYER UN JSON DATA 

    FORME DU DATA JSON à ENVOYER

    chat_client = {
        "user": 1, ## Ici il faut renseigner l'ID du USER en question
        "message":"Le lorem ipsum est, en imprimerie, une suite de mots sans signification utilisée à titre provisoire pour calibrer une mise en page, le texte définitif venant remplacer le faux-texte dès qu'il est prêt ou que la mise en page est achevée"
    }
    EXEMPLE DE REQUEST:

    requests.post(http://api.fedrelay.com/chat/<user_token>/client,json=chat_client)
'''


'''
##============ RECUPERATION DE TOUT LES CHATS D'UN USER ==========##

    url = http://api.fedrelay.com/chat/<user_id>/<user_token>/client

    EXEMPLE DE REQUEST:

    requests.post(http://api.fedrelay.com/chat/<user_id>/<user_token>/client)
'''


'''
##============ CREATION D'UN NEWSLETTER ==========##

    url = http://api.fedrelay.com/newsletter ## ON DOIT LUI ENVOYER UN JSON DATA 

    FORME DU DATA JSON à ENVOYER

    newsletter = {
        'email':'gogochristian009@gmail.com'
    }

    EXEMPLE DE REQUEST:

    requests.post(http://api.fedrelay.com/newsletter,json=newsletter)

    NB: Le mail renseigné par le client sera envoyer dans DATABASE puis ensuite dans le compte MAILCHIMP

'''

'''
##============ SIMULATION DU PRIX DE LA LIVRAISON ==========##

    url = http://api.fedrelay.com/simulator ## ON DOIT LUI ENVOYER UN JSON DATA 

    FORME DU DATA JSON à ENVOYER

    simulation = {
        "localisation":'cotonou',
        "product_type":'Lourd',
        "delivery_point":'Parakou',
        "delivery_delay":'3 jours',
    }

    EXEMPLE DE REQUEST:

    requests.post(http://api.fedrelay.com/simulator,json=simulation)

'''

'''
##============ ENREGISTREMENT D'UN PARTENARIAT ==========##

    url = http://api.fedrelay.com/partenariat ## ON DOIT LUI ENVOYER UN JSON DATA 

    FORME DU DATA JSON à ENVOYER

    partenariat = {
        "nom":"Bobo",
        "prenom":"Deg",
        "denomination":"Chine",
        "email":"bobmanou@gmail.com",
        "typ":"Signalisation",
        "object":"porto-novo",
        "lettre":"Le lorem ipsum est, en imprimerie, une suite de mots sans signification utilisée à titre provisoire pour calibrer une mise en page, le texte définitif venant remplacer le faux-texte dès qu'il est prêt ou que la mise en page est achevée. Généralement, on utilise un texte en faux latin, le Lorem ipsum ou Lipsum",
    }


    EXEMPLE DE REQUEST:

    requests.post(http://api.fedrelay.com/partenariat,json=partenariat)

'''



'''
##============ ENREGISTREMENT D'UN CONTACT ==========##

    url = http://api.fedrelay.com/contact ## ON DOIT LUI ENVOYER UN JSON DATA 

    FORME DU DATA JSON à ENVOYER

    contact = {
        "nom":"Bobo Contact",
        "prenom":"Deg contact",
        "telephone":"Chine contact",
        "message":"Le lorem ipsum est, en imprimerie, une suite de mots sans signification utilisée à titre provisoire pour calibrer une mise en page, le texte définitif venant remplacer le faux-texte dès qu'il est prêt ou que la mise en page est achevée. Généralement, on utilise un texte en faux latin, le Lorem ipsum ou Lipsum",
    }


    EXEMPLE DE REQUEST:

    requests.post(http://api.fedrelay.com/contact,json=contact)

'''

















