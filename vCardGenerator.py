import vobject
import qrcode

def generate_vcard(first_name, last_name, phone, email, organization, title, address):
    vcard = vobject.vCard()

    vcard.add('n')
    vcard.n.value = vobject.vcard.Name(family=last_name, given=first_name)

    vcard.add('fn')
    vcard.fn.value = f"{first_name} {last_name}"

    vcard.add('tel')
    vcard.tel.value = phone
    vcard.tel.type_param = 'CELL'

    vcard.add('email')
    vcard.email.value = email
    vcard.email.type_param = 'INTERNET'

    vcard.add('org')
    vcard.org.value = [organization]

    vcard.add('title')
    vcard.title.value = title

    vcard.add('adr')
    vcard.adr.value = vobject.vcard.Address(
        street=address.get('street'),
        city=address.get('city'),
        region=address.get('region'),
        code=address.get('code'),
        country=address.get('country')
    )

    vcard_str = vcard.serialize()

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    

    print(f"vCard for {first_name} {last_name} has been created.")
    print(f"QR code has been saved as {qr_filename}.")
    print(f"vCard has been saved as {vcard_filename}.")

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
phone = input("Enter phone number: ")
email = input("Enter email: ")
organization = input("Enter organization: ")
title = input("Enter title: ")
address = {
    'street': input("Enter street address: "),
    'city': input("Enter city: "),
    'region': input("Enter state/region: "),
    'code': input("Enter postal code: "),
    'country': input("Enter country: ")
}

# Call the function with user input
generate_vcard(
    first_name = first_name,
    last_name = last_name,
    phone = phone,
    email = email,
    organization = organization,
    title = title,
    address = address
)
