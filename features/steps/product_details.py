from behave import given, when, then


@when('Click to add product to cart')
def click_add_to_cart(context):
    context.app.product_details_page.click_add_to_cart()


@when('Click "View my cart"')
def click_view_my_cart(context):
    context.app.product_details_page.click_view_my_cart()


@then('Verify "added to your cart" confirmation is shown')
def verify_confirmation(context):
    context.app.product_details_page.verify_confirmation()
