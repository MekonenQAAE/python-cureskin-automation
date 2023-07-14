from behave import given, when, then


@then('Verify user is taken to the cart page')
def verify_cart_page(context):
    context.app.cart_page.verify_cart_page()
